#!/usr/bin/python3
"""A Python script that takes in a URL, sends a request to the URL"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except url.error.HTTPError as e:
        print(e.code)

