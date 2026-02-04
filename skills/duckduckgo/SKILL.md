# Web Search MCP Skill

## Overview

The Web Search MCP Skill enables Claude to leverage the web-search-mcp Model Context Protocol (MCP) server, which provides integrated access to multiple research tools including web search, location geocoding, weather data retrieval, content extraction, and domain-specific research. This MCP server extends Claude's capabilities with real-world data access through a standardized interface.

## Available Tools

### search_web

Perform comprehensive web searches using DuckDuckGo with support for both text and news searches.

Parameters:

- `query`: Search query string
- `search_type`: 'text' or 'news' (default: 'text')
- `max_results`: Max number of results (default: 5)
- `time_range`: Time filter ('d', 'w', 'm', 'y') or None
- `region`: Geographic region (e.g. 'us-en', 'uk-en') or None
- `safesearch`: Safe search level ('moderate', 'off', 'on')
- `page`: Page number for pagination (default: 1)
- `backend`: Backend to use ('auto', 'legacy', 'api')

### get_weather

Retrieve current weather or forecast for any location using latitude and longitude.

Parameters:

- `latitude`: Latitude of the location
- `longitude`: Longitude of the location
- `mode`: 'current' or 'forecast' (default: 'current')
- `days`: Number of days for forecast (1-16, default: 7)

### fetch_page

Extract content from web pages with configurable output formats.

Parameters:

- `url`: The URL to fetch and extract content from
- `output_format`: Format for extracted content ('csv', 'html', 'json', 'markdown', 'python', 'txt', 'xml', 'xmltei')
- `include_metadata`: Include document metadata (default: False)
- `include_tables`: Include table content (default: False)
- `include_comments`: Include comment content (default: False)
- `include_images`: Include image descriptions (default: False)
- `deduplicate`: Remove duplicated content (default: True)
- `max_length`: Maximum content length (default: 15000)
- `timeout`: Request timeout in seconds (default: 30)

### search_domain

Search specifically for content within a given domain (useful for documentation).

Parameters:

- `query`: What you're searching for
- `domain`: The domain to search (default: 'docs.python.org')

### geocode_location

Convert location names/addresses to geographic coordinates.

Parameters:

- `query`: Location name or address to geocode
- `limit`: Maximum number of results (default: 5, max: 40)

## Usage Examples

### Web Search

```
search_web(query="Python asyncio tutorial", search_type="text", max_results=5)
```

### Weather Information

```
geocode_location(query="Paris, France")
get_weather(latitude=48.8566, longitude=2.3522, mode="current")
```

### Content Extraction

```
fetch_page(url="https://docs.python.org/3/library/asyncio.html", output_format="markdown", include_metadata=True)
```

### Domain-Specific Search

```
search_domain(query="pandas DataFrame methods", domain="pandas.pydata.org")
```

### Comprehensive Research Example

```
# Find location coordinates
location_result = geocode_location(query="Tokyo, Japan")
coords = location_result['results'][0]

# Get weather for the location
weather_result = get_weather(latitude=coords['latitude'], longitude=coords['longitude'])

# Search for current news about Tokyo
news_result = search_web(query="Tokyo Japan", search_type="news", max_results=3)
```

## How It Works

This skill connects Claude to the web-search-mcp MCP server, which acts as a bridge between Claude and multiple data sources:

1. **MCP Protocol**: Standardized interface for Claude to access external services
2. **Tool Invocation**: Claude calls specific tools via the MCP server
3. **Data Processing**: The server processes requests using appropriate APIs
4. **Response Formatting**: Structured responses returned to Claude
5. **Integration**: Seamless experience as if the capabilities were native to Claude

## Best Practices

- Use specific and clear queries for better results
- Take advantage of parameter options to refine results
- Chain related tools together for comprehensive research
- For weather data, first geocode the location to get accurate coordinates
- For content extraction, consider the output format that best suits your needs

## Error Handling

- If geocoding fails, verify location names are properly formatted
- Weather data requires valid coordinates (typically obtained via geocode_location)
- For content extraction, ensure URLs are publicly accessible
- If searches return no results, try broader or alternative search terms

This MCP server enhances Claude's research capabilities by providing direct access to real-time data sources through a standardized protocol.
