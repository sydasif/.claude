---
name: research
description: Strategic web research, content extraction, and real-time data access.
---

# Web Research Reference

Strategic information gathering using specialized `duck` (DuckDuckgo) MCP tools.

## 1. Tool Mapping

| Goal                         | Tool               | Key Parameter                  |
| :--------------------------- | :----------------- | :----------------------------- |
| Broad search / News          | `search_web`       | `search_type='news' \| 'text'` |
| Official Documentation       | `search_domain`    | `domain='docs.example.com'`    |
| Deep Page Reading            | `fetch_page`       | `output_format='markdown'`     |
| Address $\rightarrow$ Coords | `geocode_location` | `query='Address, City'`        |
| Local Weather                | `get_weather`      | `latitude`, `longitude`        |

## 2. API Reference

### `search_web`

- **Use**: Broad topics, trending news.
- **Params**: `query`, `search_type` ('text'/'news'), `time_range` ('d','w','m','y'), `region`.

### `search_domain`

- **Use**: Authoritative documentation, specific site search.
- **Params**: `query`, `domain`.

### `fetch_page`

- **Use**: Extracting full content from a specific URL.
- **Params**: `url`, `output_format` ('markdown','json','txt'), `include_tables` (bool).

### `geocode_location` $\rightarrow$ `get_weather`

- **Workflow**: Use `geocode_location` to get `lat/long` $\rightarrow$ Pass to `get_weather`.
- **Weather Params**: `latitude`, `longitude`, `mode` ('current'/'forecast'), `days`.

## 3. Verification Checklist

- [ ] **Authority**: Is the source official or a primary provider?
- [ ] **Currency**: Check publication date; is the info outdated?
- [ ] **Cross-Ref**: Verify critical claims across $\ge 2$ independent sources.
- [ ] **Objectivity**: Identify promotional bias or conflicts of interest.
- [ ] **Completeness**: Did the `fetch_page` capture all relevant tables/sections?

> This MCP skill is designed for strategic research tasks. For real-time data, ensure to use the latest search parameters and verify results against multiple sources.