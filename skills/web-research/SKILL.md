---
name: web-research
description: Web research and information gathering, search strategies, content extraction, real-time data access and effective research techniques.
---

# Web Research Patterns

Web research principles and decision-making for effective information gathering.
**Learn to THINK strategically about research, not just use tools blindly.**

---

## ⚠️ How to Use This Skill

This skill teaches **research strategy principles**, not just tool usage patterns.

- ASK user about research goals and context before choosing tools
- Select search approach based on information type needed
- Chain tools strategically for comprehensive research
- Consider reliability and freshness of sources

---

## Overview

The Web Research Skill enables access to multiple research tools including web
search, location geocoding, weather data retrieval, content extraction, and
domain-specific research. It provides integrated real-world data access through
a standardized interface.

---

## Tool Selection Framework (2025)

### Decision Tree

```text
What information do you need?
│
├── General knowledge / news / trending topics
│   └── search_web (comprehensive, broad search)
│
├── Technical documentation / specific domain info
│   └── search_domain (focused on specific sites)
│
├── Physical location data / coordinates
│   └── geocode_location (convert addresses to lat/long)
│
├── Weather data for specific location
│   └── get_weather (requires coordinates from geocoding)
│
└── Detailed content from specific URLs
    └── fetch_page (extract content with formatting options)
```

### Tool Comparison Principles

| Capability | search_web | geocode_location | get_weather | fetch_page | search_domain |
|------------|------------|------------------|-------------|------------|---------------|
| **Best for** | Broad topics | Addresses to coords | Weather | Specific pages | Site-limited |
| **Scope** | Global | Geographic | Geographic | Single URL | Specific domain |
| **Real-time** | Yes | No | Current/forecast | No | Yes |
| **Parameters** | Rich | Simple | Rich | Rich | Simple |

### Selection Questions to Ask

1. What type of information are you seeking?
2. Do you need specific geographic data?
3. Is this about current conditions or historical facts?
4. Do you have a specific website in mind?

---

## Research Strategy Decision-Making

### When to Chain Tools Together

```text
Multi-tool research is better when:
├── Need location-specific information
│   └── geocode_location → get_weather / search_web
├── Need authoritative documentation
│   └── search_domain → fetch_page
├── Need comprehensive topic analysis
│   └── search_web → fetch_page → analyze
└── Need verification across sources
    └── search_web + search_domain + fetch_page

Single-tool usage is sufficient when:
├── Quick fact-checking
├── General topic exploration
├── Specific URL content extraction
└── Simple location lookup
```

### The Golden Rule of Web Research

```text
Strategy first → tools second:
├── Define research goal clearly
├── Identify the best tool(s) for the job
├── Consider source reliability
└── Plan verification approach

Don't:
├── Use default parameters without consideration
├── Trust first result without verification
├── Skip location context when relevant
└── Chain tools unnecessarily
```

### Research Tool Parameters Decision Guide

| Need | Tool + Parameter Choice |
|------|------------------------|
| Recent information | search_web(time_range='w' or 'm') |
| Specific region data | search_web(region='us-en', 'uk-en', etc.) |
| News vs general info | search_web(search_type='news' vs 'text') |
| Content in specific format | fetch_page(output_format='markdown', 'json', etc.) |
| Multiple location results | geocode_location(limit=N) |
| Forecast vs current | get_weather(mode='forecast' vs 'current') |

---

## Tool-Specific Strategies

### search_web Strategy

```text
When to use search_web:
├── Exploring broad topics
├── Finding recent news
├── Looking for multiple sources
├── Researching trending topics
└── Need diverse perspectives

Parameter optimization:
├── max_results: 5 (default, usually sufficient)
├── time_range: 'd','w','m','y' (for timely info)
├── search_type: 'news' vs 'text' (for specific contexts)
└── region: for location-specific results
```

### geocode_location Strategy

```text
When to use geocode_location:
├── Converting addresses to coordinates
├── Planning location-based research
├── Getting coordinates for weather
└── Normalizing location formats

Best practices:
├── Be specific with addresses
├── Check response quality (# of results)
├── Store coordinates for reuse
└── Handle multiple results appropriately
```

### get_weather Strategy

```text
When to use get_weather:
├── Current conditions for specific location
├── Forecasts for planning
├── Historical weather patterns
└── Climate research

Workflow:
├── Always geocode first (accuracy)
├── Specify mode (current/forecast)
├── Set appropriate day range
└── Consider timezone implications
```

### fetch_page Strategy

```text
When to use fetch_page:
├── Extracting detailed content from URLs
├── Converting web content to usable formats
├── Mining structured data from pages
└── Archiving content for later processing

Format selection:
├── markdown: Human-readable content
├── json: Structured data extraction
├── csv: Tabular data
└── txt: Simple text extraction

Quality considerations:
├── include_metadata: For provenance
├── include_tables: For data extraction
├── max_length: For performance
└── timeout: For reliability
```

### search_domain Strategy

```text
When to use search_domain:
├── Looking for specific documentation
├── Searching within trusted domains
├── Finding authoritative sources
└── Technical documentation discovery

Best practices:
├── Use official documentation domains
├── Verify domain relevance
├── Combine with fetch_page for deep reading
└── Check for updated versions
```

---

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

---

## Usage Examples

### Web Search

```python
search_web(query="Python asyncio tutorial", search_type="text", max_results=5)
```

### Weather Information

```python
geocode_location(query="Paris, France")
get_weather(latitude=48.8566, longitude=2.3522, mode="current")
```

### Content Extraction

```python
fetch_page(url="https://docs.python.org/3/library/asyncio.html", output_format="markdown", include_metadata=True)
```

### Domain-Specific Search

```python
search_domain(query="pandas DataFrame methods", domain="pandas.pydata.org")
```

### Comprehensive Research Example

```python
# Find location coordinates
location_result = geocode_location(query="Tokyo, Japan")
coords = location_result['results'][0]

# Get weather for the location
weather_result = get_weather(latitude=coords['latitude'], longitude=coords['longitude'])

# Search for current news about Tokyo
news_result = search_web(query="Tokyo Japan", search_type="news", max_results=3)
```

---

## Research Best Practices

### Source Evaluation Strategy

```text
Evaluate sources by:
├── Authority (who published it?)
├── Accuracy (does it cite reliable sources?)
├── Currency (when was it last updated?)
├── Coverage (is it comprehensive?)
└── Objectivity (is it biased or promotional?)
```

### Effective Query Construction

```text
Query optimization principles:
├── Be specific (avoid vague terms)
├── Use precise terminology
├── Include relevant context terms
├── Try different phrasings
└── Use advanced search operators when appropriate
```

### Research Verification Approach

```text
Verify information by:
├── Cross-referencing multiple sources
├── Checking publication dates
├── Looking for primary sources
├── Identifying potential biases
└── Confirming technical/scientific claims
```

### Data Freshness Considerations

```text
Consider data timeliness:
├── Some topics change rapidly (news, stock prices)
├── Others remain stable (historical facts)
├── Technical information can become outdated
└── Research what timeframe is acceptable for your use case
```

---

## Research Anti-Patterns to Avoid

### ❌ DON'T

- Accept first search result without scrutiny
- Use poor queries with vague terms
- Skip location context when geographic data is needed
- Chain tools unnecessarily without purpose
- Ignore time sensitivity of information
- Rely on single sources for critical decisions
- Extract content without considering licensing/copyright
- Use default parameters without considering appropriateness

### ✅ DO

- Start with clear research objectives
- Construct specific, thoughtful queries
- Consider geographic and temporal context
- Verify important information across multiple sources
- Evaluate source authority and currency
- Plan tool chaining for maximum effectiveness
- Respect content ownership and usage rights
- Apply appropriate parameters for your use case

---

## Research Decision Checklist

Before conducting research:

- [ ] **Defined clear research objectives?**
- [ ] **Selected appropriate tool(s) for information type?**
- [ ] **Considered geographic and temporal requirements?**
- [ ] **Planned verification approach?**
- [ ] **Set appropriate parameters?**
- [ ] **Considered source reliability?**
- [ ] **Evaluated information freshness needs?**
- [ ] **Reviewed ethical use of extracted content?**

---

## Advanced Research Patterns

### Academic Research Workflow

```text
1. search_web(query="topic", max_results=10, time_range="y")  # Recent academic interest
2. Scan for university sites, journals, academic papers
3. search_domain(query="specific topic", domain="edu/journal-domain")  # Authoritative sources
4. fetch_page(url=academic_paper_url, output_format="markdown")  # Extract content
5. Verify findings across multiple academic sources
```

### Technical Problem-Solving Workflow

```text
1. search_domain(query="problem", domain="official-doc-site")  # Official documentation
2. fetch_page(url=doc_url, output_format="html", include_code=True)  # Detailed examples
3. search_web(query="problem + community solutions", max_results=5)  # Community insights
4. Compare official vs community approaches
```

### Location-Based Research Workflow

```text
1. geocode_location(query="location")  # Get coordinates
2. get_weather(latitude=lat, longitude=lon, mode="current")  # Current conditions
3. search_web(query="location + current events", max_results=5)  # Local news
4. fetch_page(url=local_news_url, output_format="markdown", include_metadata=True)  # Details
5. Synthesize geographic and topical data
```

---

> **Remember**: Web research patterns are about strategic information gathering
> for YOUR specific context. Don't just use tools randomly—think about what
> approach will yield the best, most reliable information for your needs.
