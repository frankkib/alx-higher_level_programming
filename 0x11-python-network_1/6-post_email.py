#!/usr/bin/python3
"""script that takes in a URL and an email address, sends a POST"""
import requests
import sys


if __name__ == "__main___":
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)
