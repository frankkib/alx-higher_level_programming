#!/bin/bash
#Bash script that takes in a URL, sends a GET request to the URL, and displays
url=$1
curl -fLs -X GET "$url" 
