#!/usr/bin/python3
"""Query Reddit API for subreddit subscriber count"""

import requests


def number_of_subscribers(subreddit):
  """
    Queries the Reddit API to retrieve the subscriber count of a subreddit.

    Args:
      subreddit (str): The name of the subreddit.

    Returns:
      int: The number of subscribers of the specified subreddit.
           Returns 0 if the subreddit is invalid or inaccessible.
  """

  subreddit_url = f"https://www.reddit.com/r/{subreddit}/about.json"
  headers = {'User-Agent': 'Mozilla/5.0'}
  response = requests.get(subreddit_url, headers=headers)

  if response.status_code != 200:
    return 0

  data = response.json()
  return data.get("data", {}).get("subscribers", 0)
