---
title: "Power Platform: unmanaged developer environments are suspended from 15 December"
summary: Microsoft is retiring unmanaged developer environments with the Power Apps Developer Plan, and Dataverse for Teams environments. Unmanaged developer environments are suspended from 15 December 2026, so check what runs in them now.
image: /news/images/power-platform-developer-environments-retirement.svg
image_alt: Illustration of a white app window with code brackets and a black pause badge, connected by a dotted arrow to a black panel with a white shield and a check mark.
---
Microsoft has updated its list of important changes coming to Power Platform, most recently on 23 November 2026, and on 20 November it refreshed its Message center notice about Dataverse for Teams. Two retirements affect most organizations that build with Power Apps: unmanaged developer environments together with the Power Apps Developer Plan, and Dataverse for Teams environments. The first deadline is less than three weeks away.

## What is new

- **No new unmanaged developer environments.** Since 15 November 2026 you can no longer create unmanaged developer environments. The developer environment type continues only as a managed developer environment, one per user.
- **Suspension, then deletion.** Existing unmanaged developer environments are suspended starting 15 December 2026 and deleted starting 15 January 2027. Managed environments are not affected.
- **Dataverse for Teams retires.** New Dataverse for Teams environments cannot be created from 15 November 2026. Existing environments that are not upgraded to Dataverse are suspended on 15 September 2027 and decommissioned on 30 October 2027. The Message center notice says that apps, flows, agents and data in environments that are not migrated are deleted.
- **Two Power Automate features retire on 30 November.** Microsoft also lists the retirement of Copilot in the designer for cloud flows and agent flows, and of "Describe it to design it", on 30 November 2026.

## Why it matters

Developer environments are where makers experiment, and often where a prototype quietly turns into something a team depends on. When such an environment is suspended, that work stops, and the people using it may not know where it lives.

Keeping an environment running is not free. Managed Environments require premium licensing, and the Developer Plan does not include Managed Environments use rights. Upgrading Dataverse for Teams environments needs Dataverse capacity and the right user licences. Both are budget questions, so they need an owner now.

## What to do now

1. **Find the unmanaged developer environments.** In the Power Platform admin center, list your developer environments, check which ones do not have Managed Environments turned on, and contact their owners.
2. **Decide for each one before 15 December.** Either turn on Managed Environments, with the licences that requires, or export the solutions and move them to a sandbox or another supported environment.
3. **Set up environment routing** so that makers get a managed developer environment automatically instead of creating their own.
4. **Take stock of Dataverse for Teams.** Under Manage > Environments, filter by type Microsoft Teams and check the last activity. Upgrade the environments still in use after checking capacity and licences, and retire the rest.
5. **Tell flow makers about 30 November** so they are not surprised when the Copilot designer features disappear.

The [Power Platform admin plugin in Cowork](/news/power-platform-november-2026-update/) can help with questions about environments and ownership while you take stock.

Sources: [Important changes (deprecations) coming in Power Platform](https://learn.microsoft.com/en-us/power-platform/important-changes-coming), Microsoft Learn, updated 23 November 2026; Message center MC1515294, "Power Apps – Feature retirement of Microsoft Dataverse for Teams: migrate before September 15, 2027", Microsoft, 19 October 2026, updated 20 November 2026.
