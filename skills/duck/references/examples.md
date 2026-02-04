# Web Search MCP Skill - Examples

## MCP Tool Usage Examples

### Location & Weather Research

```json
MCP Tool Calls:
geocode_location(query="Tokyo, Japan", limit=1)
Response: {"query": "Tokyo, Japan", "total_results": 1, "results": [{"display_name": "Tokyo", "latitude": 35.6895, "longitude": 139.6917, ...}]}

get_weather(latitude=35.6895, longitude=139.6917, mode="current")
Response: {"current": {"temperature_2m": 15.2, "relative_humidity_2m": 65, ...}}

search_web(query="important landmarks in Tokyo", max_results=5)
Response: {"query": "important landmarks in Tokyo", "results": [...]}
```

### Technical Documentation Research

```json
MCP Tool Calls:
search_domain(query="requests library", domain="requests.readthedocs.io")
Response: {"query": "site:requests.readthedocs.io requests library", "results": [{"title": "Requests documentation", "href": "https://requests.readthedocs.io/en/latest/", ...}]}

fetch_page(url="https://requests.readthedocs.io/en/latest/", output_format="markdown", include_metadata=True)
Response: {"content": "# Requests: HTTP for Humans...", "metadata": {...}}
```

### News & Trending Topics Research

```json
MCP Tool Calls:
search_web(query="renewable energy news Germany", search_type="news", max_results=3)
Response: {"query": "renewable energy news Germany", "search_type": "news", "results": [...]}

geocode_location(query="Berlin, Germany")
Response: {"query": "Berlin, Germany", "results": [{"latitude": 52.5200, "longitude": 13.4050, ...}]}

get_weather(latitude=52.5200, longitude=13.4050, mode="current")
Response: {"current": {"temperature_2m": 8.5, "weather_code": 3, ...}}
```

### Multi-location Comparison

```json
MCP Tool Calls:
geocode_location(query="New York, USA")
Response: {"results": [{"latitude": 40.7128, "longitude": -74.0060}]}

geocode_location(query="London, UK")
Response: {"results": [{"latitude": 51.5074, "longitude": -0.1278}]}

get_weather(latitude=40.7128, longitude=-74.0060, mode="current")
Response: {"current": {"temperature_2m": 12.3, ...}}

get_weather(latitude=51.5074, longitude=-0.1278, mode="current")
Response: {"current": {"temperature_2m": 7.8, ...}}
```

## Real-World Research Workflows

### Academic Research

```json
1. search_web(query="machine learning applications in healthcare", max_results=10, time_range="y")
2. scan results for authoritative sources (university sites, journals)
3. fetch_page(url=selected_article_url, output_format="markdown")
4. extract key findings and citations
```

### Technical Problem Solving

```text
1. search_domain(query="Python pandas groupby", domain="pandas.pydata.org")
2. fetch_page(url=documentation_url, output_format="html", include_code=True)
3. search_web(query="pandas groupby best practices", max_results=5)
4. synthesize examples and recommendations
```

### Location-Based Analysis

```text
1. geocode_location(query="San Francisco, CA")
2. get_weather(latitude=37.7749, longitude=-122.4194, mode="forecast", days=7)
3. search_web(query="tech companies in San Francisco", max_results=10)
4. fetch_page(url=investor_relations_url, output_format="markdown", include_tables=True)
```

## Error Handling in Practice

### Location Not Found

```text
Input: geocode_location(query="Small Town XY")
If response['total_results'] == 0:
  Solution: geocode_location(query="XY Country") or geocode_location(query="XY Region")
```

### Weather Data Unavailable

```text
Input: get_weather(latitude=invalid_lat, longitude=invalid_lon)
If response contains "error":
  Solution: Verify coordinates with geocode_location first
```

### Content Extraction Failure

```text
Input: fetch_page(url=blocked_site)
If response contains "error" about access:
  Solution: search_web for cached versions or alternative sources
```

## Skill Integration Examples

### Research Assistant Workflow

1. User: "Research solar panel efficiency trends in California"
2. Claude: Use geocode_location to get California centroid coordinates
3. Claude: Use search_web for recent articles on solar efficiency
4. Claude: Use fetch_page to extract technical details from top results
5. Claude: Use get_weather for climate data relevant to solar power generation
6. Claude: Synthesize all information into a comprehensive report

### Documentation Helper Workflow

1. User: "Help me understand Python asyncio"
2. Claude: Use search_domain to find Python official documentation on asyncio
3. Claude: Use fetch_page to extract key concepts and examples
4. Claude: Use search_web for community examples and tutorials
5. Claude: Combine official and community resources for comprehensive explanation
