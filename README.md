# RSS Feed Keyword Monitor

This Python script monitors an RSS feed for specific keywords and posts relevant articles to a Slack channel using a webhook.

## Features

- Fetches the latest articles from an RSS feed
- Checks the article content for specified keywords
- Posts matching articles to a Slack channel using a webhook
- Supports fetching article content using the Requests library

## Requirements

- Python 3.x
- `feedparser` library: Install using `pip install feedparser`
- `requests` library: Install using `pip install requests`

## Usage

1. Clone the repository or download the script file.

2. Install the required libraries by running the following command:
   ```
   pip install feedparser requests
   ```

3. Update the script with your specific configuration:
   - Set the `rss_feed_url` variable to the URL of your desired RSS feed.
   - Modify the `keywords` list with the keywords you want to monitor.
   - Set the `slack_webhook_url` variable to the URL of your Slack webhook.

4. Run the script:
   ```
   python rss_keyword_monitor.py
   ```

5. The script will fetch the latest articles from the RSS feed, check them for the specified keywords, and post the matching articles to the configured Slack channel.

## Customization

- You can customize the behavior of the script by modifying the variables at the beginning of the script.
- You can adjust the list of keywords to monitor by adding or removing keywords from the `keywords` list.
- Feel free to enhance the script with additional functionalities as per your requirements.

## Notes

- Ensure you have the necessary permissions to access the RSS feed and the target Slack channel.
- Make sure to comply with the terms of service of the RSS feed and Slack.

## License

This project is licensed under the [MIT License](LICENSE).

