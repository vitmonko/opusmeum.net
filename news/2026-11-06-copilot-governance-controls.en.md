---
title: "New Copilot controls for admins: what shipped this autumn"
summary: DLP for Cowork, retention for Copilot memory, an agent usage report and an oversharing report. The governance toolkit is catching up with agents.
image: /news/images/copilot-governance-controls.svg
image_alt: Illustration of agents inside three nested boundaries, with documents outside that they cannot reach.
---
As Copilot takes on more work by itself, the question for IT shifts from "who can use Copilot?" to "what are Copilot and its agents doing, and with which data?". Microsoft's October update and the latest Microsoft 365 Copilot release notes add several controls that answer exactly that.

## Data protection

- **Purview DLP now covers Cowork.** One data loss prevention policy applies across Copilot Chat and Cowork. It can block references to content with sensitivity labels, block sensitive prompts, and stop sensitive prompts from being sent to Bing. It is in public preview.
- **Retention for Copilot memory.** Purview retention policies can now preserve Copilot's saved memories, which matters for investigations and regulatory requirements.

## Visibility

- **Agents usage report.** A new report in the Microsoft 365 admin center shows active agents and agent users, split by licensed and unlicensed users and by publisher type.
- **"Everyone except external users" report.** Part of SharePoint Advanced Management, this item-level report shows exactly what is shared with the whole organization, the most common source of oversharing.
- **Authoritative content.** Admins can choose up to 100 SharePoint sites whose content gets ranking priority in Copilot Search, so answers come from the official policy rather than an old draft.

## Agents that work on their own

Microsoft also introduced Autopilot, a persistent personal agent with its own account, mailbox and files, governed through Agent 365. It reaches the Frontier program in November. Agents with their own identities make the controls above more important, not less.

## What to do now

1. **Run the oversharing report** and fix sites shared with everyone before you expand Copilot.
2. **Pilot DLP for Cowork** with a small group while it is in preview, then roll it out.
3. **Review the agents usage report monthly**, so you know which agents exist and who owns them.
4. **Choose your authoritative sites**, such as HR policies, IT guides and price lists.

This builds on the five steps in our earlier post on [why Copilot governance comes before Copilot rollout](/news/copilot-governance/).

Sources: [What's New in Microsoft Copilot, October 2026](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/what%E2%80%99s-new-in-microsoft-copilot--october-2026/4568528), Microsoft Copilot Blog, 30 October 2026; [Release notes for Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes), Microsoft Learn.
