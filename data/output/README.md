# Output Data – News Summarization and Clustering

## Overview

The application displays the processed news articles through a Flask-based web interface.

The output is generated dynamically whenever a user opens a news topic or refreshes the page.

## 1. Individual Article Summaries

Each collected article is displayed with:

- Article headline
- Original article link
- News source
- Publication date
- Automatically generated summary

The summary contains the two highest-scoring sentences selected using TF-IDF-based extractive summarization.

## 2. Overall Topic Summary

The application generates an overall summary for each selected topic by combining the individual article summaries.

The four highest-scoring sentences are selected and displayed as the topic summary.

## 3. Clustering Results

The application groups related news articles using K-Means clustering.

Each cluster displays:

- Automatically generated cluster label
- Related news articles
- Article headlines and links
- Individual article summaries

Clusters are displayed from largest to smallest.

## 4. Website Output

The application provides the following pages:

### Home Page

Displays five news topic cards:
- T20 Cricket World Cup
- American Trade Wars
- Quantum Computing
- Space News
- Nobel Prizes

### Topic Page

Displays the overall topic summary, number of clusters, cluster labels and related news articles.

### Refresh Option

The refresh option downloads and processes the latest news again instead of using the cached result.

## 5. Example Clustering Output

The project report demonstrates clustering with three sample headlines:

- India wins the T20 World Cup cricket final.
- Cricket World Cup final won by India.
- NASA launches new Mars space mission.

The first two headlines are grouped into a cricket-related cluster, while the NASA headline forms a separate space-related cluster.

## Important Note

The application currently generates summaries and clustering results dynamically. These results are displayed on the website and are not automatically saved as permanent output dataset files.