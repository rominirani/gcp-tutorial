# Google Cloud Release Notes Web App

This Flask application fetches and displays the latest Google Cloud release notes from the official RSS feed.

The official RSS feed is here: https://cloud.google.com/feeds/gcp-release-notes.xml 

## Features

* **Fetches release notes:** Retrieves the latest release notes from the Google Cloud RSS feed.
* **Parses RSS feed:** Extracts relevant information like title, link, published date, and summary from each release note entry.
* **Displays release notes:** Presents the release notes in a user-friendly format on a web page.
* **Handles CDATA:** Correctly extracts content from CDATA sections within the RSS feed.
* **Escapes HTML:** Prevents HTML tags from being rendered literally in the web page.

Click on the button below to open up the application in Google Cloud Shell in your Google Account and Google Cloud project of choice. Once Cloud Shell opens up, follow the steps in the **Getting Started** section.

[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://shell.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fusername%2Freponame)

## Getting Started

1. **Install dependencies:**
   ```bash
   pip install Flask feedparser

2. **Run the application**
   ```bash
   python main.py

3. **Access the application**

   Visit http://localhost:8080/ in the browser

4. **Deploy on Cloud Run**

   Provide the following command in Cloud Shell. Follow the instructions, go with the defaults, select the appropriate Google Cloud Region and say `Y` to unauthenticated invocations of the service

   ```bash
   gcloud run deploy --source .

