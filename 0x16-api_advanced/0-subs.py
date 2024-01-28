#!/usr/bin/env python3
""" a Python script that, using this REST API, returns the number of subscribers subreddit. """
import requests
import sys

def number_of_subscribers(subreddit):

  subreddit_url = f"https://www.reddit.com/r/{subreddit}/about.json"

  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

  try:
    response = requests.get(subreddit_url, headers=headers)
    data = response.json()
    subscribers = data["data"]["subscribers"]
    return subscribers
  except KeyError:
    return 0
  except requests.exceptions.RequestException as e:
    print("Error:", e)
    return 0

