import json
import feedparser
from datetime import datetime
import os

# Ensure the 'static' directory exists
os.makedirs('static', exist_ok=True)

# Fetch Google Trends data
feed = feedparser.parse("https://trends.google.com/trends/trendingsearches/realtime/rss?geo=US&category=all")
top_keywords = [entry.title for entry in feed.entries[:10]]

data = {
    "timestamp": datetime.utcnow().isoformat(),
    "top_keywords": top_keywords
}

# Write the data to 'static/trends_data.json'
with open("static/trends_data.json", "w") as f:
    json.dump(data, f)
