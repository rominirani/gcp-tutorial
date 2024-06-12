# How to run the Release Notes Application

## Google Release Notes Application 
This Flask application fetches and displays the latest Google Cloud release notes from the official RSS feed. The official RSS feed is here: https://cloud.google.com/feeds/gcp-release-notes.xml. 

### Features

 - **Fetches release notes:** Retrieves the latest release notes from the Google Cloud RSS feed.
 - **Parses RSS feed:** Extracts relevant information like title, link, published date, and summary from each release note entry.
 - **Displays release notes:** Presents the release notes in a user-friendly format on a web page.
 - **Handles CDATA:** Correctly extracts content from CDATA sections within the RSS feed.
 - **Escapes HTML:** Prevents HTML tags from being rendered literally in the web page.

### Prerequisites

 - You have a Google account and a Google Cloud Platform Project.

## Install Python dependencies

In the Cloud Shell Terminal, give the following command:

```bash
   pip3 install -r requirements.txt
```
## Run the application

Once the dependencies are installed, use the following command to run the application 

```bash
   python main.py
```

## Access the application

Use the Cloud Shell Web Preview and visit http://localhost:8080/ in the browser

## Source Code

Let us go through the Python file to understand the source code. 

Click here: `walkthrough editor-open-file "gcp-tutorial/main.py" "Open main.py"`

## (Optional) Source Deploy to Cloud Run

Provide the following command in Cloud Shell. Follow the instructions, go with the defaults, select the appropriate Google Cloud Region and say `Y` to unauthenticated invocations of the service.

```bash
   gcloud run deploy --source .
```

## Conclusion

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

Thanks for completing this tutorial. I hope you enjoyed the power of the Google Natural Language API.

### Next Steps:

 - Check out more information on [Open in Cloud Shell](https://cloud.google.com/shell/docs/open-in-cloud-shell) 
 
