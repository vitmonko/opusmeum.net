---
title: "Power Platform's November update: business apps in Copilot and an admin plugin in Cowork"
summary: Microsoft's October/November Power Platform update brings model-driven app data into Work IQ, adds AI summaries to data grids and gives admins a governance plugin in Cowork. Most of it is in public preview.
image: /news/images/power-platform-november-2026-update.svg
image_alt: Illustration of a table with one highlighted row, linked by a dotted line to a chat bubble with a check mark, next to a ringing bell.
---
On 10 November 2026, Microsoft published its October/November Power Platform feature update, which also covers the news from the Power Platform Community Conference. Several items bring Power Apps data and administration into Copilot. Almost everything below is in public preview.

## What is new

- **Business apps in Work IQ (public preview).** Users can ask for records from a model-driven app view, look at record details, and create or update records in a conversation, without opening the app. Work IQ uses the app's existing views, forms and Dataverse data, respects permissions and applies supported business rules. Users review and explicitly confirm every change before it is submitted.
- **AI row summary in the modern data grid (public preview).** Users can generate a short AI summary of an eligible Dataverse row directly from the grid. It is opt-in and off by default.
- **Agentic authoring of canvas apps with GitHub (public preview).** Makers sign in with a GitHub account and an agent works beside the canvas in Power Apps studio. An admin must first turn on a tenant setting in the Power Platform admin center.
- **Power Platform admin plugin in Cowork (public preview).** Admins ask questions in plain language and get answers grounded in their tenant about environments, ownership, policy impact and governance posture.
- **Better monitoring (public preview).** Monitor alerts can be routed to any connector-backed destination, and monitor metrics can be exported through an API and kept in your own storage.
- **Desktop flows (public preview).** Scheduled triggers run desktop flows on a recurring schedule, and a new flowchart mode adds a visual canvas.

## Why it matters

Business apps in Work IQ change who touches your Dataverse data and how. Someone who never opens the app may now update a record from a chat. The confirmation step and existing security roles still apply, which is exactly why your security roles and business rules need to be right before you switch it on.

The admin plugin and metrics export make governance easier: fewer portals, and monitoring data you keep yourself.

## What to do now

1. **Review security roles on key model-driven apps.** Work IQ follows them, so any oversharing in Dataverse becomes easier to reach.
2. **Pilot Work IQ business apps with one team** and one app with clear business rules before wider use.
3. **Decide on the GitHub tenant setting.** Agree who may use agentic authoring and how app source is governed, then turn the setting on for that group only.
4. **Try the admin plugin in Cowork** in a test tenant or with read-focused questions first, alongside the [Copilot admin controls we covered earlier](/news/copilot-governance-controls/).
5. **Route monitor alerts to where your team works**, such as a Teams channel or your ticketing system.

Source: [What's new in Power Platform: October/November 2026 feature update](https://www.microsoft.com/en-us/power-platform/blog/power-apps/whats-new-in-power-platform-october-2026-feature-update/), Microsoft Power Platform Blog, 10 November 2026.
