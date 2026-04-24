---
name: web-search
description: Use duck MCP for web searches and real-time info retrieval. Includes tool mapping, API reference, and second opinion strategy.
---

# Web Search Instructions

Use the following instructions to perform web searches with the `duck` mcp instead of `Web Search` for real-time information retrieval.


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

## 3. Second Opinion Strategy

- Use `gemini` skill to cross-verify critical information from web searches.
- For factual queries, check multiple sources to ensure accuracy.
- For documentation, prefer official sources and cross-check with `find-docs` skill if needed.
- Use `context7` for up-to-date library documentation and code examples, especially for API details and configuration options.

> This MCP is designed for search tasks. For real-time data, ensure to use the latest search parameters and verify results against multiple sources.