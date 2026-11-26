---
title: "Power Platform: Nicht verwaltete Umgebungen für Entwickler werden ab 15. Dezember angehalten"
summary: Microsoft stellt nicht verwaltete Entwicklerumgebungen samt Power Apps Developer Plan sowie Dataverse for Teams ein. Nicht verwaltete Entwicklerumgebungen werden ab dem 15. Dezember 2026 angehalten. Prüfen Sie jetzt, was darin läuft.
image: /news/images/power-platform-developer-environments-retirement.svg
image_alt: Illustration eines weißen App-Fensters mit Code-Klammern und einem schwarzen Pause-Symbol, über einen gepunkteten Pfeil verbunden mit einer schwarzen Fläche mit weißem Schild und Häkchen.
---
Microsoft hat die Liste der wichtigen anstehenden Änderungen in Power Platform aktualisiert, zuletzt am 23. November 2026, und am 20. November die Message-center-Mitteilung zu Dataverse for Teams überarbeitet. Zwei Einstellungen betreffen die meisten Organisationen, die mit Power Apps entwickeln: nicht verwaltete Entwicklerumgebungen zusammen mit dem Power Apps Developer Plan sowie Dataverse-for-Teams-Umgebungen. Die erste Frist endet in weniger als drei Wochen.

## Was neu ist

- **Keine neuen nicht verwalteten Entwicklerumgebungen.** Seit dem 15. November 2026 lassen sich keine nicht verwalteten Entwicklerumgebungen mehr erstellen. Den Umgebungstyp „Entwickler“ gibt es nur noch als verwaltete Entwicklerumgebung, eine pro Benutzer.
- **Erst angehalten, dann gelöscht.** Bestehende nicht verwaltete Entwicklerumgebungen werden ab dem 15. Dezember 2026 angehalten und ab dem 15. Januar 2027 gelöscht. Verwaltete Umgebungen sind nicht betroffen.
- **Dataverse for Teams wird eingestellt.** Ab dem 15. November 2026 können keine neuen Dataverse-for-Teams-Umgebungen erstellt werden. Bestehende Umgebungen, die nicht auf Dataverse aktualisiert werden, werden am 15. September 2027 angehalten und am 30. Oktober 2027 außer Betrieb genommen. Laut Message-center-Mitteilung werden Apps, Flows, Agenten und Daten in nicht migrierten Umgebungen gelöscht.
- **Zwei Power-Automate-Funktionen entfallen am 30. November.** Microsoft führt zudem für den 30. November 2026 die Einstellung von Copilot im Designer für Cloud-Flows und Agent-Flows sowie von „Describe it to design it“ auf.

## Warum das wichtig ist

In Entwicklerumgebungen probieren Maker Neues aus, und oft wird dort aus einem Prototyp unbemerkt etwas, auf das sich ein Team verlässt. Wird eine solche Umgebung angehalten, steht diese Arbeit still, und die Nutzer wissen unter Umständen nicht einmal, wo sie liegt.

Eine Umgebung weiterzubetreiben kostet Geld. Managed Environments setzen Premium-Lizenzen voraus, und der Developer Plan enthält keine Nutzungsrechte für Managed Environments. Für das Upgrade von Dataverse-for-Teams-Umgebungen brauchen Sie Dataverse-Kapazität und passende Benutzerlizenzen. Beides sind Budgetfragen, die jetzt einen Verantwortlichen brauchen.

## Was Sie jetzt tun sollten

1. **Ermitteln Sie die nicht verwalteten Entwicklerumgebungen.** Lassen Sie sich im Power Platform admin center Ihre Entwicklerumgebungen anzeigen, prüfen Sie, bei welchen Managed Environments nicht aktiviert ist, und sprechen Sie die Besitzer an.
2. **Entscheiden Sie für jede Umgebung vor dem 15. Dezember.** Aktivieren Sie entweder Managed Environments mit den erforderlichen Lizenzen, oder exportieren Sie die Lösungen und verschieben Sie sie in eine Sandbox oder eine andere unterstützte Umgebung.
3. **Richten Sie Environment Routing ein**, damit Maker automatisch eine verwaltete Entwicklerumgebung erhalten, statt selbst eine anzulegen.
4. **Erfassen Sie Ihre Dataverse-for-Teams-Umgebungen.** Filtern Sie unter Manage > Environments nach dem Typ Microsoft Teams und prüfen Sie die letzte Aktivität. Aktualisieren Sie genutzte Umgebungen nach einer Prüfung von Kapazität und Lizenzen, und stellen Sie die übrigen ein.
5. **Informieren Sie Flow-Maker über den 30. November**, damit sie vom Wegfall der Copilot-Designer-Funktionen nicht überrascht werden.

Bei Fragen zu Umgebungen und ihren Besitzern kann Ihnen während der Bestandsaufnahme das [Power Platform admin plugin in Cowork](/de/news/power-platform-november-2026-update/) helfen.

Quellen: [Important changes (deprecations) coming in Power Platform](https://learn.microsoft.com/en-us/power-platform/important-changes-coming), Microsoft Learn, aktualisiert am 23. November 2026; Message-center-Mitteilung MC1515294 „Power Apps – Feature retirement of Microsoft Dataverse for Teams: migrate before September 15, 2027“, Microsoft, 19. Oktober 2026, aktualisiert am 20. November 2026.
