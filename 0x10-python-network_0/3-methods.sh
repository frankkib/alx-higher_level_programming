#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept
curl -X OPTIONS -sI "$url" | grep "Allow" | cut -d " " -f 2-
