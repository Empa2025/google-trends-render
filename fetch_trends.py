import json
import feedparser
from datetime import datetime

# Real-time trending feed for the US
feed = feedparser.parse("https://trends.google.com/trends/trendingsearches/realtime/rss?geo=US&category=all")

top_keywords = [entry.title for entry in feed.entries[:10]]

data = {
    "timestamp": datetime.utcnow().isoformat(),
    "top_keywords": top_keywords
}

import os
os.makedirs("static", exist_ok=True)  # Ensure folder exists

with open("static/trends_data.json", "w") as f:
    json.dump(data, f)

