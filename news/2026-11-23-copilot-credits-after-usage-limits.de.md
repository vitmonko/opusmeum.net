---
title: "Copilot-Nutzer können nach Erreichen ihrer Limits mit Copilot Credits weiterarbeiten"
summary: Ab Dezember 2026 können Nutzer von Microsoft 365 Copilot nach Erreichen der enthaltenen Modelllimits mit Auto ohne Credits weiterarbeiten oder ihr gewähltes Modell behalten und mit Copilot Credits bezahlen. Admins steuern das über Ausgabenrichtlinien.
image: /news/images/copilot-credits-after-usage-limits.svg
image_alt: Illustration: ein waagerechter Balken, gefüllt bis zu einer senkrechten Grenzlinie, hinter der sich der Weg in zwei Spuren teilt, eine schlicht, eine mit einem Stapel schwarzer Münzen markiert, daneben eine Messskala.
---
Am 17. November 2026 hat Microsoft Admins im Message center (MC1557754) informiert, dass Nutzer von Microsoft 365 Copilot Modelle auch nach Erreichen der in ihrer Lizenz enthaltenen Nutzungslimits weiter verwenden können. Am 20. November hat Microsoft den Zeitplan aktualisiert. Die Änderung läuft über die nutzungsabhängige Abrechnung mit Copilot Credits.

## Was neu ist

- **Zwei Optionen nach dem Limit.** Wer das enthaltene Modelllimit erreicht, kann mit Auto weiterarbeiten, das keine Credits verbraucht, oder das gewählte Modell behalten und Copilot Credits verbrauchen, sofern die nutzungsabhängige Abrechnung für ihn aktiviert ist.
- **Wo es gilt.** Copilot Chat in der Microsoft Copilot App sowie Copilot in Word, Excel und PowerPoint, im Web, auf dem Desktop und mobil.
- **Ein neuer Dienst in Ausgabenrichtlinien.** Admins steuern den Zugriff über den Dienst „Models with usage-based billing in Chat and Office“ in den Copilot-Kosteneinstellungen des Microsoft 365 Admin Centers. Richtlinien können für alle Nutzer oder für Sicherheitsgruppen in Microsoft Entra ID gelten, mit Ausgabenlimits und Warnungen.
- **Klare Signale für Nutzer.** Ein gefülltes Credit-Symbol kennzeichnet ein Modell, das Credits verbraucht, ein leeres Symbol eines ohne Verbrauch. Mit /cost sehen Nutzer Details zur Sitzung. Modelle ohne Zugriff erscheinen ausgegraut.
- **Zeitplan.** Frontier: Rollout Anfang Dezember 2026. Allgemeine Verfügbarkeit: geplant für Mitte Dezember 2026 in der Worldwide-Cloud.

## Warum das wichtig ist

Laut Microsofts Dokumentation ist die Einstellung „Auto-apply new services“ in Ausgabenrichtlinien standardmäßig aktiviert. Hat Ihre Organisation bereits eine Ausgabenrichtlinie für Copilot Credits, etwa für Cowork, kann der neue Dienst automatisch aufgenommen werden. Nutzer könnten dann in Chat und Office Credits verbrauchen, ohne dass jemand gesondert entschieden hat. Für viele Organisationen ist das eine willkommene Flexibilität, es sollte aber eine bewusste Entscheidung sein und keine Überraschung auf der Rechnung. Es ergänzt außerdem die [Nutzungslimits für Copilot Chat ohne Lizenz](/de/news/copilot-chat-usage-limits/).

## Was Sie jetzt tun sollten

1. **Prüfen Sie Ihre Ausgabenrichtlinien** im Microsoft 365 Admin Center unter Copilot, Cost Management, Configuration.
2. **Kontrollieren Sie „Auto-apply new services“** in jeder Richtlinie. Deaktivieren Sie die Einstellung dort, wo neue Dienste vor der Aufnahme geprüft werden sollen.
3. **Legen Sie fest, wer den neuen Dienst erhält.** Beginnen Sie mit einer Sicherheitsgruppe von Vielnutzern statt mit allen Nutzern, und setzen Sie Limits und Warnungen pro Nutzer.
4. **Informieren Sie Nutzer und Helpdesk** über Auto im Vergleich zu Modellen mit Credit-Verbrauch, die Credit-Symbole und /cost.

Quellen: Message center MC1557754, „Microsoft Copilot: Continue using models after reaching usage limits with Copilot Credits“, Microsoft, 17. November 2026, aktualisiert am 20. November 2026; [Usage-based billing and cost management for Copilot Credits](https://learn.microsoft.com/en-us/copilot/plan/usage-based-billing-overview-copilot-credits), Microsoft Learn, aktualisiert am 17. November 2026.
