# System Architecture – News Summarization and Clustering System

## 1. Architecture Overview

The project follows a four-layer architecture that collects news articles, processes them using Natural Language Processing techniques, and displays the results through a Flask web application.

## 2. Architecture Layers

### Layer 1: News Source

**Source:** Bing News RSS Feed

Provides news headlines, article links, snippets, sources and publication dates for the selected topics.

### Layer 2: Data Collection

**File:** news.py

Responsibilities:
- Fetches news articles from RSS feeds.
- Removes duplicate headlines.
- Extracts the original article links.
- Downloads full article content using Trafilatura.
- Downloads multiple articles in parallel.
- Uses the headline and snippet as a fallback when full-text extraction fails or returns insufficient content.

### Layer 3: NLP Processing

**File:** nlp.py

Responsibilities:
- Text preprocessing.
- Tokenization and stop-word removal.
- TF-IDF vectorization.
- Extractive text summarization.
- Cosine similarity calculation.
- K-Means clustering.
- Automatic cluster labelling.

### Layer 4: Web Application

**File:** app.py

Responsibilities:
- Defines the five news topics.
- Handles home and topic page routes.
- Executes the news processing pipeline.
- Stores processed results in an in-memory cache for 30 minutes.
- Supports refreshing news results.

### Presentation Layer

**Files:** templates/ and static/

Responsibilities:
- Displays the home page and topic pages.
- Presents overall summaries and article summaries.
- Displays article clusters and their labels.
- Provides a user-friendly interface using HTML and CSS.

## 3. Overall Data Flow

Bing News RSS Feed
        |
        v
news.py – News Collection
        |
        v
nlp.py – NLP Processing
        |
        v
app.py – Flask Application
        |
        v
HTML Templates + CSS
        |
        v
User's Web Browser

## 4. Application Workflow

1. User opens the News Aggregator website.
2. User selects one of the five available news topics.
3. The Flask application checks whether cached results are available.
4. If fresh results are unavailable, news.py fetches articles from Bing News RSS.
5. Article text is extracted and cleaned.
6. nlp.py performs TF-IDF-based summarization and K-Means clustering.
7. app.py stores the processed results in the cache.
8. The topic page displays the summaries and clusters.

## 5. Caching Mechanism

The application uses an in-memory cache with a 30-minute duration to avoid repeatedly downloading and processing the same topic.

The refresh option bypasses the cached results and retrieves the latest news.

## 6. Architecture Benefits

- Modular separation of data collection, NLP processing and web presentation.
- Automatic news collection without a manually maintained dataset.
- Parallel article downloads to improve loading time.
- Reusable NLP processing functions.
- Reduced repeated processing through caching.

## 7. Conclusion

The architecture combines live news collection, Natural Language Processing and Flask-based web development into a single application. Each layer performs a specific responsibility and contributes to generating summarized and clustered news articles for users.