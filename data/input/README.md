# Input Data – Live News Articles

## Data Source

This project collects news articles automatically from public Bing News RSS feeds.

No manually uploaded dataset or paid news API key is required.

## News Topics and Search Queries

| Topic | Search Query |
|---|---|
| T20 Cricket World Cup | T20 Cricket World Cup |
| American Trade Wars | US tariffs trade war |
| Quantum Computing | quantum computing |
| Space News (ISRO, NASA) | ISRO NASA space mission |
| Nobel Prizes | Nobel Prize |

## Input Information

The RSS feed provides:
- Article headline
- Article URL
- Short description or snippet
- News source
- Publication date

The application attempts to download the full article text using Trafilatura.

If the full article cannot be extracted or contains fewer than 300 characters, the system uses the headline and snippet as a fallback.

## Data Collection

- Approximately 15 unique recent articles are collected per topic.
- Duplicate headlines are removed.
- Articles are downloaded in parallel.

## Important Note

News data is fetched dynamically when a user opens a topic or refreshes the page. The project does not depend on a permanently stored dataset.