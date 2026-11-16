---
title: "Claude in Copilot wird in der EU ab 9. Dezember standardmäßig aktiviert"
summary: Microsoft aktiviert Claude-Modelle in Copilot für EU- und EFTA-Mandanten, die keine Auswahl getroffen haben. Wenn Sie Claude ausschalten oder auf eine Pilotgruppe beschränken möchten, legen Sie das vor dem 9. Dezember 2026 fest.
image: /news/images/claude-copilot-on-by-default-eu.svg
image_alt: Illustration: ein Kalenderblatt mit einem schwarz ausgefüllten Tag, ein gepunkteter Pfeil und ein großer Kippschalter in eingeschalteter Stellung innerhalb eines Grenzkreises.
---
Am 10. November 2026 hat Microsoft Administratoren im Message Center (MC1546438) mitgeteilt, dass die Claude-Modelle von Anthropic in Copilot für EU- und EFTA-Mandanten standardmäßig aktiviert werden. Das knüpft an die Ankündigung an, dass Claude in die EU Data Boundary kommt, über die [wir letzte Woche berichtet haben](/de/news/claude-copilot-eu-data-boundary/). Damals hieß es noch, Claude bleibe in der EU standardmäßig ausgeschaltet. Das hat sich nun geändert: Die Meldung ist mit „Action may be required“ gekennzeichnet, Stichtag ist der 9. Dezember 2026.

## Was neu ist

- **Die Verarbeitung wandert Anfang Dezember 2026 in die EU Data Boundary.** Bis dahin gilt die Verarbeitungszusage der EU Data Boundary nicht für Claude-Modelle.
- **Standardaktivierung am 9. Dezember 2026.** Für Mandanten, die für Anthropic keine Auswahl getroffen haben, werden Claude-Modelle für alle Benutzer aktiviert.
- **Ihre bisherige Entscheidung bleibt bestehen.** Haben Sie Claude bereits aktiviert, bleiben die Zuweisungen gleich. Haben Sie es deaktiviert, wird diese Auswahl respektiert.
- **Die Option nur für Apps entfällt.** Mandanten, die Claude nur in Copilot in Microsoft-365-Apps zugelassen haben, wechseln am 9. Dezember zu allen Benutzern, sofern ein Administrator die Einstellung nicht vorher ändert.
- **Größere Reichweite.** Nach der Änderung stehen Claude-Modelle in allen Microsoft-Copilot-Erlebnissen und in Copilot Studio zur Verfügung.
- **Modelle mit Datenaufbewahrung sind getrennt geregelt.** Für Anthropic-Modelle mit Datenaufbewahrung gilt eine eigene Einstellung, die von der Änderung nicht betroffen ist.

## Warum das wichtig ist

Viele europäische Organisationen haben die Anthropic-Einstellung nie angefasst, weil sie ausgeschaltet war. Genau diese Mandanten werden nun eingeschaltet. Wenn Ihre Datenschutz-Folgenabschätzung, Ihre Betriebsvereinbarung oder Ihre KI-Richtlinie Claude noch nicht abdeckt, ist die Standardänderung schneller als Ihre Dokumentation.

Umgekehrt gilt: Wenn Sie auf die Verarbeitung innerhalb der EU Data Boundary gewartet haben, müssen Sie Claude nicht länger ausgeschaltet lassen. Treffen Sie die Entscheidung bewusst, statt sie dem Standardwert zu überlassen.

## Was Sie jetzt tun sollten

1. **Entscheiden Sie vor dem 9. Dezember.** Legen Sie fest, ob Claude für alle Benutzer, eine Pilotgruppe oder niemanden gelten soll, und dokumentieren Sie, wer das warum entschieden hat.
2. **Setzen Sie die Einstellung ausdrücklich.** Öffnen Sie im Microsoft 365 Admin Center **Copilot**, **Settings**, **View all**, **AI providers operating as Microsoft subprocessors**, **Anthropic**, wählen Sie **No users** oder **Specific users and groups** und speichern Sie. Dafür benötigen Sie die Rolle AI Administrator oder Global Administrator.
3. **Prüfen Sie die Option nur für Apps.** Wenn Sie sie nutzen, wird diese Gruppe am 9. Dezember auf alle Benutzer erweitert.
4. **Prüfen Sie Copilot Studio.** Kontrollieren Sie die Anthropic-Einstellungen im Power Platform Admin Center, damit die Modellwahl der Maker zu Ihrer Richtlinie passt.
5. **Informieren Sie Helpdesk und Compliance-Team.** Benutzer sehen Claude nach dem 9. Dezember möglicherweise als Modelloption.
6. **Mandanten im Vereinigten Königreich:** Microsoft hat dazu eine eigene Message-Center-Meldung veröffentlicht, MC1546435. Das Vereinigte Königreich gehört nicht zur EU Data Boundary, prüfen Sie sie daher gesondert.

Quellen: Microsoft 365 Message Center, Meldung MC1546438, 10. November 2026; [Bringing Claude models in Microsoft Copilot into the EU Data Boundary](https://www.microsoft.com/en-us/copilot/blog/2026/11/05/bringing-claude-models-in-microsoft-copilot-into-the-eu-data-boundary/), Microsoft Copilot Blog, 5. November 2026; [Claude models from Anthropic in Microsoft Online Services](https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor), Microsoft Learn.
