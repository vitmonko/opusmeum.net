---
title: "Claude in Copilot will be switched on by default in the EU on 9 December"
summary: Microsoft will enable Claude models in Copilot for EU and EFTA tenants that have not made a choice. If you want Claude off or limited to a pilot group, set it before 9 December 2026.
image: /news/images/claude-copilot-on-by-default-eu.svg
image_alt: Illustration of a calendar page with one day filled in black, a dotted arrow, and a large toggle switch in the on position inside a boundary circle.
---
On 10 November 2026, Microsoft told admins in the Message center (MC1546438) that Claude models from Anthropic in Copilot will be enabled by default for EU and EFTA tenants. This follows the announcement that Claude is coming into the EU Data Boundary, which [we covered last week](/news/claude-copilot-eu-data-boundary/). At that point Claude was set to stay off by default in the EU. That has now changed, and the post is marked "Action may be required", with an act-by date of 9 December 2026.

## What is new

- **Processing moves into the EU Data Boundary in early December 2026.** Until then, Claude models are not covered by the EU Data Boundary processing commitment.
- **Default enablement on 9 December 2026.** Tenants that have not made a selection for Anthropic get Claude models enabled for all users.
- **Your existing choice is kept.** If you already enabled Claude, assignments stay the same. If you disabled it, that selection is respected.
- **The apps-only option is retired.** Tenants that allowed Claude only in Copilot in Microsoft 365 apps move to all users on 9 December, unless an admin changes the setting first.
- **Wider reach.** After the change, Claude models are available across Microsoft Copilot experiences and in Copilot Studio.
- **Data retention models are separate.** Anthropic models with data retention are governed by a separate setting and are not affected.

## Why it matters

Many European organizations never touched the Anthropic setting because it was off. Those tenants are exactly the ones that will be switched on. If your data protection assessment, works council agreement or AI policy does not yet cover Claude, the default change will move faster than your paperwork.

The opposite is also true. If you were waiting for EU Data Boundary processing, you no longer need to keep Claude off. Make the decision on purpose rather than letting the default make it for you.

## What to do now

1. **Decide before 9 December.** Agree on all users, a pilot group, or no users, and record who made the decision and why.
2. **Set it explicitly.** In the Microsoft 365 admin center, go to **Copilot**, **Settings**, **View all**, **AI providers operating as Microsoft subprocessors**, **Anthropic**, then choose **No users** or **Specific users and groups** and save. You need the AI Administrator or Global Administrator role.
3. **Check the apps-only setting.** If you use it, that group will widen to all users on 9 December.
4. **Review Copilot Studio.** Check the Anthropic controls in the Power Platform admin center so makers' model choices match your policy.
5. **Brief the help desk and compliance team.** Users may see Claude as a model option after 9 December.
6. **UK tenants:** Microsoft published a separate Message center post, MC1546435. The UK is not part of the EU Data Boundary, so review it separately.

Sources: Microsoft 365 Message center post MC1546438, 10 November 2026; [Bringing Claude models in Microsoft Copilot into the EU Data Boundary](https://www.microsoft.com/en-us/copilot/blog/2026/11/05/bringing-claude-models-in-microsoft-copilot-into-the-eu-data-boundary/), Microsoft Copilot Blog, 5 November 2026; [Claude models from Anthropic in Microsoft Online Services](https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor), Microsoft Learn.
