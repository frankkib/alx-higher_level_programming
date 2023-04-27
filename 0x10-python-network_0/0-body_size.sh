#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size
curl -Is "$1" | wc -c | cut -d " " -f 2

