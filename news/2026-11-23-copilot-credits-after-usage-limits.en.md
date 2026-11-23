---
title: "Copilot users can keep using premium models with Copilot Credits after their limits"
summary: From December 2026, Microsoft 365 Copilot users who reach their included model limits can continue with Auto at no credit cost, or keep their chosen model and pay with Copilot Credits. Admins control this through spending policies.
image: /news/images/copilot-credits-after-usage-limits.svg
image_alt: Illustration of a horizontal bar filled to a vertical limit line, after which the path splits into two lanes, one plain and one marked with a stack of black coins, next to a dial.
---
On 17 November 2026, Microsoft told admins in the Message center (MC1557754) that Microsoft 365 Copilot users will be able to continue using models after they reach the usage limits included in their license. Microsoft updated the timeline on 20 November. The change runs through usage-based billing with Copilot Credits.

## What is new

- **Two options after the limit.** A user who reaches the included model limit can continue with Auto, which does not use credits, or keep the selected model and consume Copilot Credits, if usage-based billing is enabled for them.
- **Where it applies.** Copilot Chat in the Microsoft Copilot app and Copilot in Word, Excel and PowerPoint, on web, desktop and mobile.
- **A new service in spending policies.** Admins control access through a service called "Models with usage-based billing in Chat and Office" in the Copilot cost management settings of the Microsoft 365 admin center. Policies can target all users or Microsoft Entra ID security groups, with spending limits and alerts.
- **Clear signals for users.** A filled credit icon marks a model that consumes credits, an unfilled icon one that does not. Users can type /cost to see session details. Models a user cannot access are greyed out.
- **Timeline.** Frontier: rolling out in early December 2026. General availability: planned for mid-December 2026 in the Worldwide cloud.

## Why it matters

Microsoft's documentation says the "Auto-apply new services" setting is enabled by default for spending policies. If your organization already has a spending policy for Copilot Credits, for example for Cowork, the new service may be added to it automatically, and users could start consuming credits in Chat and Office without a separate decision. For many organizations that is welcome flexibility, but it should be a choice, not a surprise on the invoice. It also complements the [usage limits for Copilot Chat without a license](/news/copilot-chat-usage-limits/).

## What to do now

1. **Review your spending policies** in the Microsoft 365 admin center under Copilot, Cost Management, Configuration.
2. **Check "Auto-apply new services"** on each policy. Turn it off where new services should be reviewed before they are added.
3. **Decide who gets the new service.** Start with a security group of heavy users rather than all users, and set per-user limits and alerts.
4. **Brief users and the help desk** on Auto versus credit-consuming models, the credit icons and /cost.

Sources: Message center MC1557754, "Microsoft Copilot: Continue using models after reaching usage limits with Copilot Credits", Microsoft, 17 November 2026, updated 20 November 2026; [Usage-based billing and cost management for Copilot Credits](https://learn.microsoft.com/en-us/copilot/plan/usage-based-billing-overview-copilot-credits), Microsoft Learn, updated 17 November 2026.
