#!/usr/bin/python3
""" Request top 10 posts from a subreddit """
import requests


def top_ten(subreddit):
    """ Queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit"""
    header = {'User-Agent': 'Basset'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, allow_redirects=False, headers=header)
    if response.status_code == 200:
        for i in range(0, 10):
            print(response.json()['data']['children'][i]['data']['title'])
    else:
        print(None)
