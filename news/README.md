# News posts

Each post is one file per language in this folder. When you push to `main`, the site rebuilds:
the newest 3 posts appear in the News section of that language's homepage, and each post gets its own page.

## File name

```
YYYY-MM-DD-short-name.LANG.md
```

- `YYYY-MM-DD` is the publish date shown on the site.
- `short-name` becomes the address, e.g. `opusmeum.net/news/short-name/`. Use lowercase letters, digits and hyphens.
- `LANG` is `en`, `lt` or `de`. Use the same date and short name for translations of one post, so the language switcher links them.

A post can exist in only one language. It then appears only on that language's pages.

## File content

```
---
title: The headline of the post
summary: One or two sentences shown in the list and in search results.
image: /news/images/my-cover.svg
image_alt: What the cover image shows, for screen readers.
---
First paragraph of the post.

## A subheading

- a bullet point
- another one

1. **Bold start.** A numbered point with a [link](https://example.com).
```

Supported formatting: paragraphs, `##` and `###` subheadings, `-` and `1.` lists, `> quotes`,
`**bold**`, `*italic*` and `[links](url)`.

## Cover image (optional)

`image:` is shown at the top of the post and next to it in the news list. Use a 1200 × 630 image in
`news/images/`. LinkedIn and other sites can't show SVG previews, so if the cover is an `.svg`, put a
`.png` with the same name next to it and that is used for link previews. `image_alt:` is required with an image.

## Images inside a post

Put images in `news/images/` and add them on a line of their own:

```
![Short description of the image](/news/images/file.png)
```

## Preview locally

```
python3 tools/build.py
```

The finished site is written to `_site/`. A broken post (missing title, wrong file name) stops the build with a message saying which file to fix, and the live site stays as it was.
