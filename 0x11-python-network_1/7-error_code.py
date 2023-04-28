#!/usr/bin/python3
"""A Python script that fetches url"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if reponse.status_code >= 400:
        print(f"Error code: {reponse.status_code}")
    else:
        print(response.content.decode('utf-8'))
