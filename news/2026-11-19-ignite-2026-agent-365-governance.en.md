---
title: "Agent 365 at Ignite 2026: one registry for agents from every platform"
summary: Microsoft is extending Agent 365 to agents built on Salesforce, Google, OpenAI, Anthropic and other platforms, and to local agents on Windows and macOS devices. Some controls are generally available, many are in preview.
image: /news/images/ignite-2026-agent-365-governance.svg
image_alt: Illustration of a white central panel with a shield outline, connected by thick lines to a ring of circles, squares and triangles of different sizes on a black background.
---
On 17 November 2026, at Microsoft Ignite, Microsoft announced a large update to Agent 365, its control plane for AI agents. Microsoft says organizations have registered more than 50 million agents in Agent 365 since its launch in May 2026. The update aims to bring agents from other vendors and agents running on employees' devices under the same management, governance and security.

## What is new

- **Agents from other platforms get Entra Agent IDs.** Agents from Salesforce Agentforce, Amazon AgentCore, Google Vertex AI, Databricks, Snowflake, Anthropic Claude Managed Agents, OpenAI, Oracle, SAP, ServiceNow and UiPath receive Microsoft Entra Agent IDs. Microsoft says the rollout completes in December.
- **Local agent discovery is generally available.** Microsoft Defender finds agents on managed Windows and macOS devices. Network-level discovery and shadow AI discovery in the Agent registry are in preview.
- **Plugins and skills governance is generally available.** The Tools Registry is also generally available. MCP server governance for Azure AI Gateway and LiteLLM is in preview.
- **Runtime protection for local agents is generally available** in Microsoft Defender on Windows. Purview data loss prevention for Microsoft and key local agents is in preview.
- **Action center arrives in December as a preview.** It starts by surfacing inactive and ownerless agents for review and cleanup.
- **Dynamic agent risk is in preview.** It combines runtime signals, posture and blast radius into a risk assessment for each agent.
- **Multi-tenant agent management** in the Microsoft 365 admin center is in public preview.
- **Business Analytics and Cost Management.** Agent 365 Business Analytics is rolling out in Frontier. Cost Management adds spending limits, alerts, model controls and delegated access, with spend visibility, policies and alerts in preview.

## Licensing

Usage insights for Microsoft agents are now available with qualifying Microsoft 365 subscriptions. Management of non-Microsoft agents and the advanced governance and security features still need an Agent 365 or ME7 license. Business Analytics for Microsoft services needs at least one Microsoft 365 Copilot license in the tenant.

## Why it matters

Most organizations already have agents in more than one place: Copilot Studio, a CRM, a developer's laptop. Until now each had its own console, or none. A single registry with identities and owners makes it possible to answer basic questions: which agents exist, who owns them, what they can reach and what they cost.

## How to prepare

1. **Open the Agent registry and see what is already there.** The free usage insights are a good first inventory.
2. **Assign an owner to every agent.** Ownerless agents are the first thing the Action center will flag.
3. **Turn on local agent discovery** if you use Defender on managed devices.
4. **List your non-Microsoft agent platforms** and check whether you need Agent 365 or ME7 licenses to manage them.
5. **Review MCP servers, plugins and skills** your makers use, and decide which are approved. Our post on [Copilot Studio agents with their own accounts](/news/copilot-studio-agents-own-accounts/) covers why agent identity matters.

Sources: [What's new in Microsoft Agent 365: Ignite 2026](https://techcommunity.microsoft.com/blog/agent-365-blog/whats-new-in-microsoft-agent-365-ignite-2026/4571753), Microsoft Agent 365 Blog, 17 November 2026; [Microsoft Ignite 2026 Book of News](https://news.microsoft.com/events/ignite/2026/book-of-news/), Microsoft, 17 November 2026.
