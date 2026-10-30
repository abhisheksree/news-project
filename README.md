# 📰 News Aggregator & Intelligent Summarization System

A Python-based web application that collects news articles from different topics, generates concise summaries using Natural Language Processing (NLP), and groups related articles using text clustering techniques.

## 📌 Project Overview

The **News Aggregator & Intelligent Summarization System** is designed to make it easier for users to explore news and understand important information without reading multiple lengthy articles.

The application fetches news articles from Bing News RSS feeds, extracts article content when available, generates automatic summaries, and organizes related articles into meaningful groups.

It provides a simple web interface where users can browse different news categories and explore summarized articles.

## ✨ Features

- **News Aggregation:** Fetches news articles using Bing News RSS feeds.
- **Multiple News Categories:** Supports T20 Cricket World Cup, American Trade Wars, Quantum Computing, Space News, and Nobel Prizes.
- **Automatic Text Summarization:** Uses TF-IDF-based sentence scoring to generate concise summaries.
- **Article Clustering:** Groups related news articles using TF-IDF vectors and K-Means clustering.
- **Full Article Extraction:** Attempts to extract full article content using Trafilatura, with a fallback to article snippets.
- **Caching Mechanism:** Stores fetched results for 30 minutes to reduce repeated requests.
- **Refresh Option:** Allows users to refresh topic results.
- **Web Interface:** Provides a user-friendly interface built with Flask, HTML, and CSS.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Flask | Web application framework |
| Natural Language Processing (NLP) | Text summarization and article grouping |
| TF-IDF | Text feature extraction |
| K-Means Clustering | Grouping similar news articles |
| Feedparser | Reading RSS news feeds |
| Trafilatura | Extracting article text |
| HTML | Webpage structure |
| CSS | Webpage styling |

## 📂 Project Structure

```text
news_project/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── topic.html
│
├── app.py
├── news.py
├── nlp.py
├── requirements.txt
├── .gitignore
└── README.md
```

### File Description

- **app.py:** Main Flask application. Handles website routes, news topics, summaries, caching, and page rendering.
- **news.py:** Fetches news articles from RSS feeds and attempts to extract their full content.
- **nlp.py:** Implements text preprocessing, TF-IDF vectorization, automatic summarization, and article clustering.
- **templates/:** Contains HTML templates used to display the website.
- **static/style.css:** Contains the styling of the web application.
- **requirements.txt:** Lists the Python dependencies required to run the project.
- **.gitignore:** Specifies files and folders that should not be tracked by Git.

## ⚙️ Installation and Setup

Follow these steps to run the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/abhisheksree/news-project.git
```

### 2. Navigate to the Project Directory

```bash
cd news-project
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

### 6. Open the Application

The application automatically attempts to open your default browser.

If it does not, open the following address manually:

```text
http://127.0.0.1:5000
```

**Note:** An active internet connection is required to retrieve news feeds and article content.

## 🧠 NLP Techniques Used

### 1. Text Summarization

The application uses TF-IDF-based sentence scoring to identify important sentences from news articles and generate concise summaries.

### 2. Article Clustering

TF-IDF vectors represent article text numerically. A K-Means clustering algorithm then groups articles based on their textual similarity.

### 3. Text Preprocessing

The application performs tokenization and stop-word removal to prepare text for summarization and clustering.

## 🎯 Project Objectives

- Simplify access to news from multiple subject areas.
- Reduce the time required to read lengthy news articles.
- Automatically identify important information.
- Group similar news articles for easier exploration.
- Demonstrate practical applications of NLP and machine learning concepts.

## 🚀 Future Enhancements

- Add more news categories and sources.
- Implement sentiment analysis for news articles.
- Improve summarization accuracy.
- Add user authentication and personalized news preferences.
- Develop a responsive mobile-friendly interface.
- Deploy the application to a cloud platform.

## 👨‍💻 Author

**Abhishek Sree**

GitHub: [@abhisheksree](https://github.com/abhisheksree)

Project Repository: [News Aggregator & Intelligent Summarization System](https://github.com/abhisheksree/news-project)

---

*Developed as a Python-based project demonstrating web development, Natural Language Processing, text summarization, and clustering techniques.*