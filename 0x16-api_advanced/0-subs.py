#!/usr/bin/python3
""" a Python script that, using this REST API, returns the number of subscribers subreddit. """

import requests

def number_of_subscribers(subreddit):
  subreddit_url = f"https://www.reddit.com/r/{subreddit}/about.json"

  headers = {'User-Agent': 'Mozilla/5.0'}

  response = requests.get(subreddit_url, headers=headers)

  if response.status_code != 200:
    return 0

  data = response.json()
  return data.get("data", {}).get("subscribers", 0)
