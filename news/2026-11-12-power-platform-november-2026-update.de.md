---
title: "Das November-Update für Power Platform: Business-Apps in Copilot und ein Admin-Plug-in in Cowork"
summary: Das Oktober/November-Update für Power Platform bringt Daten aus modellgesteuerten Apps in Work IQ, ergänzt KI-Zusammenfassungen im Datenraster und gibt Administratoren ein Governance-Plug-in in Cowork. Das meiste ist in der öffentlichen Vorschau.
image: /news/images/power-platform-november-2026-update.svg
image_alt: Illustration: eine Tabelle mit einer hervorgehobenen Zeile, über eine gepunktete Linie mit einer Sprechblase mit Häkchen verbunden, daneben eine läutende Glocke.
---
Am 10. November 2026 hat Microsoft das Oktober/November-Feature-Update für Power Platform veröffentlicht, das auch die Neuigkeiten der Power Platform Community Conference zusammenfasst. Mehrere Neuerungen bringen Power-Apps-Daten und die Administration in Copilot. Fast alles im Folgenden befindet sich in der öffentlichen Vorschau.

## Was neu ist

- **Business-Apps in Work IQ (öffentliche Vorschau).** Benutzer können im Chat Datensätze aus einer Ansicht einer modellgesteuerten App abrufen, Details ansehen und Datensätze anlegen oder aktualisieren, ohne die App zu öffnen. Work IQ nutzt die vorhandenen Ansichten, Formulare und Dataverse-Daten der App, beachtet Berechtigungen und wendet unterstützte Geschäftsregeln an. Jede Änderung prüfen und bestätigen die Benutzer ausdrücklich, bevor sie übermittelt wird.
- **KI-Zusammenfassung von Zeilen im modernen Datenraster (öffentliche Vorschau).** Benutzer können direkt im Raster eine kurze KI-Zusammenfassung einer geeigneten Dataverse-Zeile erzeugen. Die Funktion ist optional und standardmäßig deaktiviert.
- **Agentische Erstellung von Canvas-Apps mit GitHub (öffentliche Vorschau).** Maker melden sich mit einem GitHub-Konto an, und ein Agent arbeitet neben dem Canvas in Power Apps Studio. Zuvor muss ein Administrator eine Mandanteneinstellung im Power Platform Admin Center aktivieren.
- **Power Platform Admin-Plug-in in Cowork (öffentliche Vorschau).** Administratoren stellen Fragen in natürlicher Sprache und erhalten auf ihren Mandanten bezogene Antworten zu Umgebungen, Besitzern, Auswirkungen von Richtlinien und Governance-Status.
- **Besseres Monitoring (öffentliche Vorschau).** Monitor-Warnungen lassen sich an jedes über einen Connector erreichbare Ziel weiterleiten, und Monitor-Metriken können per API exportiert und im eigenen Speicher aufbewahrt werden.
- **Desktop-Flows (öffentliche Vorschau).** Geplante Trigger führen Desktop-Flows nach Zeitplan aus, und ein neuer Flussdiagramm-Modus bietet einen visuellen Canvas.

## Warum das wichtig ist

Business-Apps in Work IQ verändern, wer mit Ihren Dataverse-Daten arbeitet und wie. Wer die App nie öffnet, kann nun einen Datensatz im Chat aktualisieren. Der Bestätigungsschritt und die vorhandenen Sicherheitsrollen gelten weiterhin, deshalb müssen Sicherheitsrollen und Geschäftsregeln stimmen, bevor Sie die Funktion einschalten.

Das Admin-Plug-in und der Metrik-Export erleichtern die Governance: weniger Portale und Monitoring-Daten, die bei Ihnen bleiben.

## Was Sie jetzt tun sollten

1. **Prüfen Sie die Sicherheitsrollen wichtiger modellgesteuerter Apps.** Work IQ richtet sich danach, daher werden zu weit gefasste Berechtigungen in Dataverse leichter erreichbar.
2. **Testen Sie Business-Apps in Work IQ mit einem Team** und einer App mit klaren Geschäftsregeln, bevor Sie sie breiter einsetzen.
3. **Entscheiden Sie über die GitHub-Mandanteneinstellung.** Legen Sie fest, wer die agentische Erstellung nutzen darf und wie der App-Quellcode verwaltet wird, und aktivieren Sie die Einstellung nur für diese Gruppe.
4. **Testen Sie das Admin-Plug-in in Cowork** zunächst in einem Testmandanten oder mit reinen Abfragen, zusammen mit den [Copilot-Admin-Kontrollen, über die wir berichtet haben](/de/news/copilot-governance-controls/).
5. **Leiten Sie Monitor-Warnungen dorthin, wo Ihr Team arbeitet**, etwa in einen Teams-Kanal oder Ihr Ticketsystem.

Quelle: [What's new in Power Platform: October/November 2026 feature update](https://www.microsoft.com/en-us/power-platform/blog/power-apps/whats-new-in-power-platform-october-2026-feature-update/), Microsoft Power Platform Blog, 10. November 2026.
