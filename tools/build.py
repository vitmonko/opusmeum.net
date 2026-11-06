"""Build the deployable site into _site/.

Copies the static pages, then turns news/*.md posts into:
  - the "News" list on each language's homepage (latest 3 posts)
  - a page per post:        /news/<slug>/, /lt/news/<slug>/, /de/news/<slug>/
  - an archive per language: /news/, /lt/news/, /de/news/
  - RSS feeds:               /feed.xml, /lt/feed.xml, /de/feed.xml
  - /sitemap.xml

Standard library only. Run locally with:  python3 tools/build.py
See news/README.md for how to write a post.
"""
import datetime as dt
import html
import os
import re
import shutil
import sys
from email.utils import format_datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_site")
SITE = "https://opusmeum.net"
LANGS = ("en", "lt", "de")
BASE = {"en": "/", "lt": "/lt/", "de": "/de/"}
LATEST = 3
SKIP = {".git", ".github", "tools", "news", "_site", ".gitignore"}

L10N = {
    "en": {"news": "News", "all": "All news", "feed": "Opus Meum news",
           "archive_intro": "Notes from our projects on Power Platform, Copilot and AI governance.",
           "cta_title": "Want to talk about this for your organization?",
           "cta": "Book a free consultation", "locale": "en_GB"},
    "lt": {"news": "Naujienos", "all": "Visos naujienos", "feed": "Opus Meum naujienos",
           "archive_intro": "Pastabos iš mūsų projektų apie Power Platform, Copilot ir DI valdyseną.",
           "cta_title": "Norite aptarti, kaip tai pritaikyti jūsų organizacijoje?",
           "cta": "Užsakyti nemokamą konsultaciją", "locale": "lt_LT"},
    "de": {"news": "Aktuelles", "all": "Alle Beiträge", "feed": "Opus Meum Aktuelles",
           "archive_intro": "Erfahrungen aus unseren Projekten zu Power Platform, Copilot und KI-Governance.",
           "cta_title": "Möchten Sie darüber für Ihr Unternehmen sprechen?",
           "cta": "Kostenloses Erstgespräch buchen", "locale": "de_DE"},
}
MONTHS = {
    "en": ["January", "February", "March", "April", "May", "June", "July",
           "August", "September", "October", "November", "December"],
    "lt": ["sausio", "vasario", "kovo", "balandžio", "gegužės", "birželio", "liepos",
           "rugpjūčio", "rugsėjo", "spalio", "lapkričio", "gruodžio"],
    "de": ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli",
           "August", "September", "Oktober", "November", "Dezember"],
}


def fail(msg):
    sys.exit(f"build error: {msg}")


def fmt_date(d, lang):
    m = MONTHS[lang][d.month - 1]
    if lang == "lt":
        return f"{d.year} m. {m} {d.day} d."
    if lang == "de":
        return f"{d.day}. {m} {d.year}"
    return f"{d.day} {m} {d.year}"


# ---------- minimal Markdown ----------
def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)",
                  lambda m: f'<img src="{html.escape(m.group(2))}" alt="{html.escape(m.group(1))}" loading="lazy">', text)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",
                  lambda m: f'<a href="{html.escape(m.group(2))}">{m.group(1)}</a>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)
    return text


def markdown(src):
    """Paragraphs, ## / ### headings, - and 1. lists, > quotes, **bold**, *italic*, [links](url)."""
    out, para, lst = [], [], None

    def flush_para():
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para.clear()

    def flush_list():
        nonlocal lst
        if lst:
            tag, items = lst
            out.append(f"<{tag}>" + "".join(f"<li>{inline(i)}</li>" for i in items) + f"</{tag}>")
            lst = None

    for raw in src.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush_para(); flush_list(); continue
        h = re.match(r"^(#{2,3})\s+(.*)$", line)
        ul = re.match(r"^\s*[-*]\s+(.*)$", line)
        ol = re.match(r"^\s*\d+[.)]\s+(.*)$", line)
        bq = re.match(r"^>\s?(.*)$", line)
        if h:
            flush_para(); flush_list()
            n = len(h.group(1))
            out.append(f"<h{n}>{inline(h.group(2))}</h{n}>")
        elif ul or ol:
            flush_para()
            tag = "ul" if ul else "ol"
            if lst and lst[0] != tag:
                flush_list()
            if not lst:
                lst = (tag, [])
            lst[1].append((ul or ol).group(1))
        elif bq:
            flush_para(); flush_list()
            out.append(f"<blockquote><p>{inline(bq.group(1))}</p></blockquote>")
        elif lst and raw.startswith(("   ", "\t")):
            lst[1][-1] += " " + line.strip()
        else:
            flush_list()
            para.append(line.strip())
    flush_para(); flush_list()
    return "\n".join(out)


# ---------- posts ----------
def load_posts():
    posts = []
    folder = os.path.join(ROOT, "news")
    if not os.path.isdir(folder):
        return posts
    for name in sorted(os.listdir(folder)):
        m = re.match(r"^(\d{4}-\d{2}-\d{2})-([a-z0-9-]+)\.(en|lt|de)\.md$", name)
        if not name.endswith(".md") or name == "README.md":
            continue
        if not m:
            fail(f"news/{name}: name must look like 2026-11-06-my-post.en.md")
        text = open(os.path.join(folder, name), encoding="utf-8").read()
        fm = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
        if not fm:
            fail(f"news/{name}: missing the --- header block")
        meta = {}
        for line in fm.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"')
        for key in ("title", "summary"):
            if not meta.get(key):
                fail(f"news/{name}: '{key}:' is required")
        if meta.get("image"):
            img = os.path.join(ROOT, meta["image"].lstrip("/"))
            if not meta["image"].startswith("/news/images/") or not os.path.isfile(img):
                fail(f"news/{name}: image must be a file in news/images/, got {meta['image']}")
            if not meta.get("image_alt"):
                fail(f"news/{name}: 'image_alt:' is required when 'image:' is set")
        posts.append({
            "date": dt.date.fromisoformat(m.group(1)), "slug": m.group(2), "lang": m.group(3),
            "title": meta["title"], "summary": meta["summary"],
            "image": meta.get("image", ""), "image_alt": meta.get("image_alt", ""),
            "body": markdown(fm.group(2)),
        })
    posts.sort(key=lambda p: (p["date"], p["slug"]), reverse=True)
    return posts


def post_url(p):
    return f"{BASE[p['lang']]}news/{p['slug']}/"


# ---------- page shell borrowed from each homepage ----------
def chrome(lang):
    page = open(os.path.join(ROOT, BASE[lang].strip("/"), "index.html") if lang != "en"
                else os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    head = re.search(r"<head>(.*?)</head>", page, re.S).group(1)
    header = re.search(r'<header class="site-header">.*?</header>', page, re.S).group(0)
    footer = re.search(r'<footer class="site-footer">.*?</footer>', page, re.S).group(0)
    skip = re.search(r'<a class="skip"[^>]*>.*?</a>', page).group(0)
    keep = [l for l in head.splitlines() if re.search(
        r'charset|viewport|Content-Security-Policy|referrer|theme-color|rel="icon"|preconnect|fonts.googleapis.com/css2|styles.css|main.js', l)]
    return page, "\n".join(keep), header, footer, skip


def localize_links(fragment, lang, switch):
    fragment = fragment.replace('href="#', f'href="{BASE[lang]}#')
    for code in LANGS:
        fragment = fragment.replace(f'href="{BASE[code]}" hreflang="{code}"',
                                    f'href="{switch[code]}" hreflang="{code}"')
    return fragment


def shell(lang, *, title, description, canonical, switch, alternates, og_type, extra_head, main):
    _, head, header, footer, skip = chrome(lang)
    alt = "\n".join(f'  <link rel="alternate" hreflang="{c}" href="{SITE}{u}">' for c, u in alternates.items())
    if "en" in alternates:
        alt += f'\n  <link rel="alternate" hreflang="x-default" href="{SITE}{alternates["en"]}">'
    e = html.escape
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
{head}
  <title>{e(title)}</title>
  <meta name="description" content="{e(description)}">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="{e(description)}">
  <meta property="og:type" content="{og_type}">
  <meta property="og:locale" content="{L10N[lang]['locale']}">
  <meta property="og:url" content="{SITE}{canonical}">
  <link rel="canonical" href="{SITE}{canonical}">
{alt}
  <link rel="alternate" type="application/rss+xml" title="{e(L10N[lang]['feed'])}" href="{BASE[lang]}feed.xml">
{extra_head}
</head>
<body>
  {skip}

  {localize_links(header, lang, switch)}

  <main id="main">
{main}
  </main>

  {localize_links(footer, lang, switch)}
</body>
</html>
"""


def og_image(p):
    """Social previews need a raster image: use a .png next to the cover if there is one."""
    if not p["image"]:
        return ""
    png = os.path.splitext(p["image"])[0] + ".png"
    return png if os.path.isfile(os.path.join(ROOT, png.lstrip("/"))) else p["image"]


def news_list(items, lang, heading="h3"):
    rows = []
    for p in items:
        thumb = (f'<img src="{html.escape(p["image"])}" alt="" width="1200" height="630" loading="lazy">'
                 if p["image"] else "")
        rows.append(
            f'<li><a class="news-item" href="{post_url(p)}">'
            f'<span class="news-meta">{thumb}<time datetime="{p["date"].isoformat()}">{fmt_date(p["date"], lang)}</time></span>'
            f'<span class="news-text"><{heading}>{html.escape(p["title"])}</{heading}>'
            f'<span class="news-summary">{html.escape(p["summary"])}</span></span></a></li>')
    return '<ul class="news-list">\n' + "\n".join(rows) + "\n</ul>"


def write(path, text):
    full = os.path.join(OUT, path.lstrip("/"))
    if full.endswith("/"):
        full += "index.html"
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(text)


def build():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    for name in os.listdir(ROOT):
        if name in SKIP or name.startswith("."):
            continue
        src = os.path.join(ROOT, name)
        (shutil.copytree if os.path.isdir(src) else shutil.copy2)(src, os.path.join(OUT, name))
    if os.path.isdir(os.path.join(ROOT, "news", "images")):
        shutil.copytree(os.path.join(ROOT, "news", "images"), os.path.join(OUT, "news", "images"))

    posts = load_posts()
    by_lang = {l: [p for p in posts if p["lang"] == l] for l in LANGS}
    by_slug = {}
    for p in posts:
        by_slug.setdefault(p["slug"], {})[p["lang"]] = p
    sitemap = []
    today = dt.date.today().isoformat()

    for lang in LANGS:
        t = L10N[lang]
        items = by_lang[lang]
        home_rel = "index.html" if lang == "en" else f"{lang}/index.html"
        home = open(os.path.join(OUT, home_rel), encoding="utf-8").read()
        if items:
            home = home.replace("<!-- news:latest -->", news_list(items[:LATEST], lang))
            home = home.replace("</head>", f'  <link rel="alternate" type="application/rss+xml" '
                                f'title="{html.escape(t["feed"])}" href="{BASE[lang]}feed.xml">\n</head>')
        else:
            home = re.sub(r"\s*<!-- news:section:start -->.*?<!-- news:section:end -->", "", home, flags=re.S)
            home = re.sub(r'\s*<a href="#news">[^<]*</a>', "", home)
        open(os.path.join(OUT, home_rel), "w", encoding="utf-8").write(home)
        sitemap.append((BASE[lang], items[0]["date"].isoformat() if items else today))
        if not items:
            continue

        # archive
        archive = f"{BASE[lang]}news/"
        switch = {c: (f"{BASE[c]}news/" if by_lang[c] else BASE[c]) for c in LANGS}
        main = f"""    <section class="page-head">
      <div class="wrap">
        <h1>{t['news']}</h1>
        <p>{t['archive_intro']}</p>
      </div>
    </section>
    <section class="news news-archive">
      <div class="wrap">
        {news_list(items, lang, heading="h2")}
      </div>
    </section>"""
        write(archive, shell(lang, title=f"{t['news']} | Opus Meum", description=t["archive_intro"],
                             canonical=archive, switch=switch,
                             alternates={c: f"{BASE[c]}news/" for c in LANGS if by_lang[c]},
                             og_type="website", extra_head="", main=main))
        sitemap.append((archive, items[0]["date"].isoformat()))

        # posts
        for p in items:
            url = post_url(p)
            tr = by_slug[p["slug"]]
            switch = {c: (post_url(tr[c]) if c in tr else (f"{BASE[c]}news/" if by_lang[c] else BASE[c]))
                      for c in LANGS}
            ld = ('  <script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting",'
                  f'"headline":{_json(p["title"])},"description":{_json(p["summary"])},'
                  f'"datePublished":"{p["date"].isoformat()}","inLanguage":"{lang}",'
                  f'"mainEntityOfPage":"{SITE}{url}",'
                  '"author":{"@type":"Organization","name":"Opus Meum","url":"https://opusmeum.net/"},'
                  + (f'"image":"{SITE}{og_image(p)}",' if p["image"] else "") +
                  '"publisher":{"@type":"Organization","name":"Opus Meum","logo":{"@type":"ImageObject","url":"https://opusmeum.net/logo.svg"}}}</script>')
            og = (f'  <meta property="og:image" content="{SITE}{og_image(p)}">\n'
                  f'  <meta property="og:image:alt" content="{html.escape(p["image_alt"])}">\n'
                  '  <meta name="twitter:card" content="summary_large_image">\n') if p["image"] else ""
            cover = (f'<figure class="post-cover"><img src="{html.escape(p["image"])}" '
                     f'alt="{html.escape(p["image_alt"])}" width="1200" height="630"></figure>') if p["image"] else ""
            main = f"""    <article class="post">
      <div class="wrap">
        <p class="post-crumb"><a href="{archive}">{t['news']}</a></p>
        <header class="post-head">
          <time datetime="{p['date'].isoformat()}">{fmt_date(p['date'], lang)}</time>
          <h1>{html.escape(p['title'])}</h1>
          <p class="post-lede">{html.escape(p['summary'])}</p>
        </header>
        {cover}
        <div class="post-body">
{p['body']}
        </div>
        <aside class="post-cta">
          <p>{t['cta_title']}</p>
          <a class="btn btn-solid" href="{BASE[lang]}#contact">{t['cta']}</a>
        </aside>
      </div>
    </article>"""
            write(url, shell(lang, title=f"{p['title']} | Opus Meum", description=p["summary"],
                             canonical=url, switch=switch,
                             alternates={c: post_url(tr[c]) for c in LANGS if c in tr},
                             og_type="article", extra_head=og + ld, main=main))
            sitemap.append((url, p["date"].isoformat()))

        # RSS
        e = html.escape
        rss_items = "".join(
            f"<item><title>{e(p['title'])}</title><link>{SITE}{post_url(p)}</link>"
            f"<guid>{SITE}{post_url(p)}</guid>"
            f"<pubDate>{format_datetime(dt.datetime(p['date'].year, p['date'].month, p['date'].day, 9, 0, tzinfo=dt.timezone.utc))}</pubDate>"
            f"<description>{e(p['summary'])}</description></item>" for p in items[:20])
        write(f"{BASE[lang]}feed.xml",
              '<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel>'
              f"<title>{e(t['feed'])}</title><link>{SITE}{archive}</link>"
              f"<description>{e(t['archive_intro'])}</description><language>{lang}</language>"
              f"{rss_items}</channel></rss>\n")

    write("/sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{d}</lastmod></url>\n" for u, d in sitemap)
          + "</urlset>\n")
    print(f"built {len(posts)} post file(s) into _site/")


def _json(s):
    import json
    return json.dumps(s, ensure_ascii=False).replace("</", "<\\/")


if __name__ == "__main__":
    build()
