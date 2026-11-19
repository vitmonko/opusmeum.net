---
title: "Agent 365 auf der Ignite 2026: ein Register für Agenten aller Plattformen"
summary: Microsoft erweitert Agent 365 auf Agenten, die auf Salesforce, Google, OpenAI, Anthropic und anderen Plattformen gebaut sind, sowie auf lokale Agenten auf Windows- und macOS-Geräten. Einige Kontrollen sind allgemein verfügbar, viele in der Vorschau.
image: /news/images/ignite-2026-agent-365-governance.svg
image_alt: Illustration: ein weißes zentrales Feld mit Schildumriss, mit dicken Linien verbunden mit einem Ring aus Kreisen, Quadraten und Dreiecken unterschiedlicher Größe auf schwarzem Hintergrund.
---
Am 17. November 2026 hat Microsoft auf der Ignite ein großes Update für Agent 365 angekündigt, seine Steuerungsebene für KI-Agenten. Laut Microsoft haben Organisationen seit dem Start im Mai 2026 mehr als 50 Millionen Agenten in Agent 365 registriert. Das Update soll Agenten anderer Anbieter und Agenten auf den Geräten der Mitarbeitenden unter dieselbe Verwaltung, Governance und Sicherheit bringen.

## Was neu ist

- **Agenten anderer Plattformen erhalten Entra Agent IDs.** Agenten von Salesforce Agentforce, Amazon AgentCore, Google Vertex AI, Databricks, Snowflake, Anthropic Claude Managed Agents, OpenAI, Oracle, SAP, ServiceNow und UiPath erhalten Microsoft Entra Agent IDs. Laut Microsoft ist der Rollout im Dezember abgeschlossen.
- **Die Erkennung lokaler Agenten ist allgemein verfügbar.** Microsoft Defender findet Agenten auf verwalteten Windows- und macOS-Geräten. Die Erkennung auf Netzwerkebene und die Erkennung von Schatten-KI im Agent registry sind in der Vorschau.
- **Die Governance für Plugins und Skills ist allgemein verfügbar.** Auch die Tools Registry ist allgemein verfügbar. Die MCP-Server-Governance für Azure AI Gateway und LiteLLM ist in der Vorschau.
- **Der Laufzeitschutz für lokale Agenten ist allgemein verfügbar**, in Microsoft Defender unter Windows. Purview Data Loss Prevention für Microsoft-Agenten und wichtige lokale Agenten ist in der Vorschau.
- **Das Action center kommt im Dezember als Vorschau.** Es zeigt zunächst inaktive Agenten und Agenten ohne Besitzer zur Prüfung und Bereinigung an.
- **Dynamic agent risk ist in der Vorschau.** Es verbindet Laufzeitsignale, Sicherheitsstatus und mögliche Schadensreichweite zu einer Risikobewertung pro Agent.
- **Die mandantenübergreifende Agentenverwaltung** im Microsoft 365 Admin Center ist in der öffentlichen Vorschau.
- **Business Analytics und Cost Management.** Agent 365 Business Analytics wird in Frontier ausgerollt. Cost Management ergänzt Ausgabenlimits, Warnungen, Modellkontrollen und delegierten Zugriff, wobei Ausgabentransparenz, Richtlinien und Warnungen in der Vorschau sind.

## Lizenzierung

Nutzungseinblicke für Microsoft-Agenten sind jetzt mit qualifizierenden Microsoft-365-Abonnements verfügbar. Für die Verwaltung von Nicht-Microsoft-Agenten und die erweiterten Governance- und Sicherheitsfunktionen ist weiterhin eine Agent-365- oder ME7-Lizenz nötig. Business Analytics für Microsoft-Dienste setzt mindestens eine Microsoft-365-Copilot-Lizenz im Mandanten voraus.

## Warum das wichtig ist

Die meisten Organisationen haben Agenten bereits an mehreren Stellen: in Copilot Studio, im CRM, auf dem Laptop einer Entwicklerin. Bisher hatte jede Stelle ihre eigene Konsole oder gar keine. Ein gemeinsames Register mit Identitäten und Besitzern beantwortet die Grundfragen: Welche Agenten gibt es, wem gehören sie, worauf greifen sie zu und was kosten sie.

## Wie Sie sich vorbereiten

1. **Öffnen Sie das Agent registry und sehen Sie nach, was dort schon steht.** Die kostenlosen Nutzungseinblicke eignen sich für eine erste Bestandsaufnahme.
2. **Weisen Sie jedem Agenten einen Besitzer zu.** Agenten ohne Besitzer markiert das Action center als Erstes.
3. **Aktivieren Sie die Erkennung lokaler Agenten**, wenn Sie Defender auf verwalteten Geräten nutzen.
4. **Erfassen Sie Ihre Nicht-Microsoft-Agentenplattformen** und prüfen Sie, ob Sie für deren Verwaltung Agent-365- oder ME7-Lizenzen brauchen.
5. **Prüfen Sie MCP-Server, Plugins und Skills**, die Ihre Maker nutzen, und legen Sie fest, welche freigegeben sind. Warum Agentenidentität wichtig ist, erklärt unser Beitrag zu [Copilot-Studio-Agenten mit eigenen Konten](/de/news/copilot-studio-agents-own-accounts/).

Quellen: [What's new in Microsoft Agent 365: Ignite 2026](https://techcommunity.microsoft.com/blog/agent-365-blog/whats-new-in-microsoft-agent-365-ignite-2026/4571753), Microsoft Agent 365 Blog, 17. November 2026; [Microsoft Ignite 2026 Book of News](https://news.microsoft.com/events/ignite/2026/book-of-news/), Microsoft, 17. November 2026.
