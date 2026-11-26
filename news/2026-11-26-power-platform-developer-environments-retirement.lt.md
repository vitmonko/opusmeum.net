---
title: "Power Platform: nevaldomų kūrėjų aplinkų veikla stabdoma nuo gruodžio 15 d."
summary: Microsoft nutraukia nevaldomų kūrėjų aplinkų kartu su Power Apps Developer Plan ir Dataverse for Teams aplinkų palaikymą. Nevaldomos kūrėjų aplinkos bus sustabdytos nuo 2026 m. gruodžio 15 d., todėl patikrinkite, kas jose veikia, jau dabar.
image: /news/images/power-platform-developer-environments-retirement.svg
image_alt: Iliustracija: baltas programos langas su kodo skliaustais ir juodu pauzės ženklu, punktyrine rodykle sujungtas su juodu skydeliu, kuriame yra baltas skydas su varnele.
---
Microsoft atnaujino svarbių artėjančių Power Platform pakeitimų sąrašą (paskutinį kartą 2026 m. lapkričio 23 d.), o lapkričio 20 d. atnaujino Message center pranešimą apie Dataverse for Teams. Du pakeitimai paliečia daugumą organizacijų, kuriančių su Power Apps: nevaldomos kūrėjų aplinkos kartu su Power Apps Developer Plan ir Dataverse for Teams aplinkos. Pirmasis terminas – po mažiau nei trijų savaičių.

## Kas naujo

- **Naujų nevaldomų kūrėjų aplinkų nebebus.** Nuo 2026 m. lapkričio 15 d. nevaldomų kūrėjų aplinkų sukurti nebegalima. Kūrėjų aplinkos tipas lieka tik kaip valdoma kūrėjų aplinka, po vieną kiekvienam naudotojui.
- **Pirmiausia sustabdymas, vėliau ištrynimas.** Esamos nevaldomos kūrėjų aplinkos stabdomos nuo 2026 m. gruodžio 15 d., o trinamos nuo 2027 m. sausio 15 d. Valdomoms aplinkoms tai įtakos neturi.
- **Dataverse for Teams nutraukiamas.** Nuo 2026 m. lapkričio 15 d. naujų Dataverse for Teams aplinkų sukurti nebegalima. Esamos aplinkos, kurios nebus atnaujintos į Dataverse, bus sustabdytos 2027 m. rugsėjo 15 d. ir panaikintos 2027 m. spalio 30 d. Message center pranešime nurodoma, kad neperkeltose aplinkose esančios programos, srautai, agentai ir duomenys ištrinami.
- **Lapkričio 30 d. nutraukiamos dvi Power Automate funkcijos.** Microsoft taip pat nurodo, kad 2026 m. lapkričio 30 d. nutraukiamas Copilot debesies ir agentų srautų dizaino įrankyje bei funkcija „Describe it to design it“.

## Kodėl tai svarbu

Kūrėjų aplinkose kūrėjai eksperimentuoja, ir dažnai būtent ten prototipas nepastebimai tampa tuo, nuo ko priklauso visa komanda. Kai tokia aplinka sustabdoma, darbas sustoja, o jos naudotojai gali net nežinoti, kur ji yra.

Išlaikyti aplinką veikiančią kainuoja. Valdomoms aplinkoms (Managed Environments) reikia premium licencijų, o Developer Plan neapima teisių naudoti Managed Environments. Dataverse for Teams aplinkoms atnaujinti reikia Dataverse talpos ir tinkamų naudotojų licencijų. Tai biudžeto klausimai, todėl jiems atsakingą asmenį reikia paskirti dabar.

## Ką daryti dabar

1. **Suraskite nevaldomas kūrėjų aplinkas.** Power Platform administravimo centre peržiūrėkite kūrėjų aplinkas, patikrinkite, kuriose neįjungta Managed Environments, ir susisiekite su jų savininkais.
2. **Kiekvienai aplinkai sprendimą priimkite iki gruodžio 15 d.** Arba įjunkite Managed Environments su reikiamomis licencijomis, arba eksportuokite sprendimus ir perkelkite juos į smėlio dėžės (sandbox) ar kitą palaikomą aplinką.
3. **Sukonfigūruokite aplinkų nukreipimą (environment routing)**, kad kūrėjai automatiškai gautų valdomą kūrėjų aplinką, užuot kūrę savo.
4. **Inventorizuokite Dataverse for Teams aplinkas.** Skiltyje Manage > Environments filtruokite pagal tipą Microsoft Teams ir patikrinkite paskutinę veiklą. Naudojamas aplinkas atnaujinkite patikrinę talpą ir licencijas, o likusias panaikinkite.
5. **Informuokite srautų kūrėjus apie lapkričio 30 d.**, kad Copilot dizaino funkcijų dingimas jų nenustebintų.

Inventorizuojant aplinkas, atsakyti į klausimus apie aplinkas ir jų savininkus gali padėti [Power Platform administratoriaus įskiepis Cowork](/lt/news/power-platform-november-2026-update/).

Šaltiniai: [Important changes (deprecations) coming in Power Platform](https://learn.microsoft.com/en-us/power-platform/important-changes-coming), Microsoft Learn, atnaujinta 2026 m. lapkričio 23 d.; Message center pranešimas MC1515294 „Power Apps – Feature retirement of Microsoft Dataverse for Teams: migrate before September 15, 2027“, Microsoft, 2026 m. spalio 19 d., atnaujinta 2026 m. lapkričio 20 d.
