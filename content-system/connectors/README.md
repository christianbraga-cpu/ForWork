# Connectors: what's connected and how to add the rest

Checked 2026-10-20. Connectors load when a session **starts**, so start a new session after adding one.

| Need | Tool | Status | Used by |
|---|---|---|---|
| Read any page, site URL inventory, web search, image URLs | **Firecrawl** (Lead_MCP) | ✅ Connected | seo-researcher, planner-sme, visual-curator |
| Google SERP by country/city (fallback) | **Apify** Google Search actor (Lead_MCP) | ✅ Connected (Apify credit) | seo-researcher |
| Reverse image search | **Google Lens via Apify** (`s-r/google-lens`) | ✅ Available (pay per image) | visual-curator |
| Page traffic | **WeddedAdmin** `landing_pages_overview` | ✅ Connected | /wedded-linkmap |
| Image library, GSC exports | **Google Drive** | ✅ Connected | visual-curator, seo-researcher |
| Brand assets | **Canva** | ✅ Connected | visual-curator |
| Permission request drafts | **Gmail** (drafts only) | ✅ Connected | visual-curator |
| Non-place illustrative images | **Higgsfield** | ✅ Connected | visual-curator (rare) |
| CRM for persona calibration | **Zoho CRM** | ✅ Connected | /wedded-calibrate |
| SERP + keyword volume by location | **DataForSEO** | ❌ Not connected | seo-researcher (preferred) |
| Keyword difficulty, backlinks | **Semrush or Ahrefs** | ❌ Not connected | seo-researcher |
| Rankings per page/query | **Google Search Console** | ❌ Not connected | seo-researcher, /wedded-refresh |
| Typing into the CMS | **Claude in Chrome** | ❌ Not in cloud sessions | cms-publisher |

---

## DataForSEO

DataForSEO runs a **hosted MCP server with sign-in** at `https://mcp.dataforseo.com/v3/mcp` (from the official `dataforseo/mcp-server-typescript` README). That makes it the easiest of these to connect.

**Option A: custom connector (recommended)**
1. Create an account at dataforseo.com and add pay-as-you-go credit.
2. Go to https://claude.ai/customize/connectors → **Add custom connector**.
3. Name: `DataForSEO`. URL: `https://mcp.dataforseo.com/v3/mcp`.
4. Click **Connect** and sign in with your DataForSEO account when it asks.
5. Start a new session and ask Claude to "test DataForSEO". It runs one SERP query (Sydney, primary keyword) and reports the cost.

This works in normal Claude chat as well as Claude Code. Connector traffic goes through Claude's connector service, so you don't need to change the environment's network settings.

**Option B: run the server in this repo (if Option A is unavailable to you)**
1. Copy your **API login and API password** from https://app.dataforseo.com/api-access.
2. Environment settings (environment menu in the session title bar → Edit):
   - Network access → Allowed domains: add `api.dataforseo.com` (keep "Allow package managers" ticked)
   - Network secrets / Environment variables: `DATAFORSEO_LOGIN`, `DATAFORSEO_PASSWORD`
3. Copy the `dataforseo` block from `mcp.example.json` into a root `.mcp.json` and commit it (it only names the variables; the values stay in environment secrets). Cloud sessions clone the repo fresh, so an uncommitted `.mcp.json` would be lost.
4. Start a new session and test.

---

## Semrush or Ahrefs (pick one)

Both are in the Claude connector directory.
1. Check your plan includes API/MCP access (Semrush: API units; Ahrefs: a plan with API/MCP access).
2. https://claude.ai/customize/connectors → **Browse** → search "Semrush" or "Ahrefs" → **Connect** → sign in.
3. Start a new session; test with a keyword overview for the primary keyword (AU) and a domain overview of weddedwonderland.com.

---

## Google Search Console

Not in the connector directory.

**Route A: no-code (start here)**
Once a month: GSC → Performance → Search results → last 3 months → **Export → Google Sheets**. Save into Drive folder `Wedded SEO/GSC exports/`. Agents read it through the Google Drive connector.

**Route B: live, with a service account**

> Search Console and Google Cloud Console are **different sites**. Steps 1 to 4 are in Google Cloud Console; only step 5 is in Search Console.

*In Google Cloud Console (https://console.cloud.google.com), signed in with the same Google account you use for Search Console:*
1. Click the **project picker** (top left, next to the Google Cloud logo) → **New Project** → name it `wedded-seo` → Create. No billing needed. Make sure the picker now shows `wedded-seo`.
2. Turn on the API, using any of these:
   - ☰ menu (top left) → **APIs & Services** → **Library** (if it isn't listed, click **View all products** first), then search "Google Search Console API"
   - the search bar at the top of the page: type "Google Search Console API"
   - direct link: https://console.cloud.google.com/apis/library/searchconsole.googleapis.com

   Open **Google Search Console API** and click **Enable**.
3. ☰ menu → **IAM & Admin** → **Service Accounts** → **Create service account** (e.g. `wedded-gsc-reader`). Skip both optional permission steps → Done.
4. Click the new account → **Keys** tab → Add key → Create new key → **JSON** → Create. It downloads once.
   If blocked by `iam.disableServiceAccountKeyCreation`, a Google admin must allow it for this project.

*In Search Console (https://search.google.com/search-console):*

5. Copy the service account email from its Details tab in Cloud Console (`wedded-gsc-reader@wedded-seo.iam.gserviceaccount.com`). In Search Console, select the weddedwonderland.com property → Settings → Users and permissions → **Add user** → paste → **Restricted**. You must be an Owner.

*In this Claude environment:*

6. Environment settings:
   - Network secrets / Environment variables: `GSC_SERVICE_ACCOUNT_JSON` = the whole JSON file (or one-line base64 of it)
   - Allowed domains: `searchconsole.googleapis.com`, `oauth2.googleapis.com`, `www.googleapis.com`
7. Copy the `gsc` block from `mcp.example.json` into the root `.mcp.json`. It runs `start-gsc.sh`, which writes the secret to a private temp file and starts `mcp-server-gsc` (third-party, pinned to 0.3.0; review before upgrading).
8. Start a new session; test with top queries for the last 28 days.
9. Rotate the key every 90 days. If it leaks, delete it in the Keys tab.

---

## Google Lens

Nothing to install. The visual-curator runs the Apify actor `s-r/google-lens` (fallback `gio21/google-lens-scraper`) through Lead_MCP. You only need Apify credit, and the image must be at a public URL.

---

## Claude in Chrome (CMS upload)

The cms-publisher needs a browser on **your** computer, where you're logged into the CMS:
- Run `/wedded-blog` from **Claude Code desktop** with the Claude in Chrome extension, or
- Link this cloud session to your computer (Remote Control / remote devices) so the browser tools appear.

Without it, the pipeline stops at `11-publish-package.json`, ready to upload by hand or on a later run.

**Never paste CMS credentials into the chat.** Log in yourself, then let the agent work in that tab.
