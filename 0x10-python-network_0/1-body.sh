#!/bin/bash
#Bash script that takes in a URL, sends a GET request to the URL, and displays
url=$1
curl -s -w "\n%{http_code}" "$url" | awk 'NF{if (f) print $0; else if ($0=="200") f=1}'
