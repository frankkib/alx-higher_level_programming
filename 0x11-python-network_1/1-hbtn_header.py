#!/usr/bin/python3
"""A python script that takes the URL and displays the header"""
import urllib.request
import sys

if __name__ == "__main___":
    url = sys.argv[1]
    with url.request.urlopen(url) as response:
        header = response.info()
        request_id = header['X-Request-Id']
        print(request_id)
