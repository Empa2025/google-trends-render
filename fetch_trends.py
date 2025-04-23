import json
import feedparser
from datetime import datetime
import os
import subprocess

# Make sure the 'static' folder exists
os.makedirs("static", exist_ok=True)

# Fetch Google Trends
feed = feedparser.parse("https://trends.google.com/trends/trendingsearches/realtime/rss?geo=US&category=all")
top_keywords = [entry.title for entry in feed.entries[:10]]

# Save data to static/trends_data.json
data = {
    "timestamp": datetime.utcnow().isoformat(),
    "top_keywords": top_keywords
}
with open("static/trends_data.json", "w") as f:
    json.dump(data, f, indent=2)

# Git config
subprocess.run(["git", "config", "--global", "user.email", os.environ["GITHUB_EMAIL"]])
subprocess.run(["git", "config", "--global", "user.name", os.environ["GITHUB_NAME"]])

# Commit and push
subprocess.run(["git", "add", "static/trends_data.json"])
subprocess.run(["git", "commit", "-m", "Update trends_data.json"])
subprocess.run(["git", "remote", "set-url", "origin", f"https://{os.environ['GITHUB_TOKEN']}@github.com/{os.environ['GITHUB_REPO']}"])
subprocess.run(["git", "push", "origin", "main"])
