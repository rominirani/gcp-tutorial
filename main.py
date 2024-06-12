from flask import Flask, render_template
from feedparser import parse


app = Flask(__name__)

@app.route('/')
def index():
    feed_url = 'https://cloud.google.com/feeds/gcp-release-notes.xml'
    feed = parse(feed_url)

    entries = []
    for entry in feed.entries:
        # Extract the content from the entry
        content = entry.content

        # Find the content element with type="html"
        html_content = None
        for item in content:
            if item['type'] == 'text/html':
                html_content = item['value']
                break

        if html_content:
            entries.append({
                'title': entry.title,
                'link': entry.link,
                'summary': html_content
            })

    return render_template('index.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
