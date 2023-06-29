import feedparser
import json
import requests
import ssl

# Define the RSS feed URL
rss_feed_url = "https://www.bleepingcomputer.com/startups/feed/"

# Define the list of keywords to check
keywords = ["Put,key,words"]

# Define the Slack webhook URL
slack_webhook_url = 'https://hooks.slack.com/xxxxxxx'

# Disable SSL certificate verification temporarily
ssl._create_default_https_context = ssl._create_unverified_context

# Create a session
session = requests.Session()

# Set a User-Agent header
session.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"

# Parse the RSS feed
feed = feedparser.parse(rss_feed_url)

# Iterate over the entries in the feed
for entry in feed.entries:
    # Extract relevant information from the entry
    title = entry.get("title", "")
    link = entry.get("link", "")
    published_date = entry.get("published", "")
    summary = entry.get("summary", "")

    # If content is empty, fetch the content from the URL
    if not summary:
        try:
            response = session.get(link)
            response.raise_for_status()
            content = response.text
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch content for {title}: {e}")
            continue
    else:
        content = summary

    # Check if the article content or summary contains any of the keywords
    matched_keywords = [keyword for keyword in keywords if keyword.lower() in content.lower()]
    if matched_keywords:
        # Define the message payload
        message_payload = {
            "attachments": [
                {
                    "fallback": title,
                    "pretext": "New article",
                    "title": title,
                    "title_link": link,
                    "text": f"Published Date: {published_date}\nMatched Keywords: {', '.join(matched_keywords)}"
                }
            ]
        }

        # Convert the payload dictionary to JSON string
        json_payload = json.dumps(message_payload)

        # Set the headers for the POST request
        headers = {
            "Content-Type": "application/json"
        }

        # Send the message to Slack
        response = requests.post(slack_webhook_url, data=json_payload, headers=headers)

        # Check the response
        if response.status_code == 200:
            print("Message sent successfully!")
        else:
            print("Failed to send message. Status Code:", response.status_code)
            print("Response:", response.text)