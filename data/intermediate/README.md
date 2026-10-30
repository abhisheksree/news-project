# Intermediate Data – NLP Processing

## Overview

After collecting news articles from Bing News RSS feeds, the application processes the article text using Natural Language Processing techniques.

The intermediate processing includes text preprocessing, TF-IDF calculation, extractive summarization, cosine similarity and K-Means clustering.

## 1. Text Preprocessing

The collected article text is cleaned before further processing.

The following operations are performed:

- Convert text into lowercase.
- Remove numbers and special symbols.
- Extract words containing three or more letters.
- Remove common stop words such as "the", "and", "with" and "from".

## 2. TF-IDF Vectorization

TF-IDF (Term Frequency – Inverse Document Frequency) converts article text into numerical word-weight representations.

The project calculates:

- Term Frequency (TF): Frequency of a word in a document.
- Inverse Document Frequency (IDF): Importance of a word across all documents.
- TF-IDF: Product of TF and IDF.

Formula:

TF-IDF = TF × IDF

The resulting vectors are normalized so that articles of different lengths can be compared fairly.

## 3. Extractive Text Summarization

The application splits article content into sentences.

Each sentence receives a score based on its TF-IDF word weights.

The highest-scoring sentences are selected and displayed in their original order.

- Individual article summary: Top 2 sentences.
- Overall topic summary: Top 4 sentences.

## 4. Cosine Similarity

Cosine similarity measures how similar two article vectors are based on their word-weight representations.

A higher similarity score indicates greater similarity between the articles.

## 5. K-Means Clustering

The application uses K-Means clustering to group related news articles.

Processing steps:

1. Initialize cluster centres using a fixed random seed and a far-apart selection method.
2. Assign articles to their most similar cluster centre.
3. Recalculate cluster centres using the normalized average of assigned article vectors.
4. Repeat assignment and updating until the assignments stop changing or 20 iterations are completed.

The default number of clusters is 3 and is reduced automatically when there are fewer articles.

## 6. Cluster Labelling

Each cluster receives an automatic label based on the three highest-weight words in its cluster centre.

Clusters are displayed from largest to smallest.

## Important Note

These intermediate calculations are performed dynamically during application execution. The current project does not permanently store TF-IDF vectors or clustering calculations as separate dataset files.