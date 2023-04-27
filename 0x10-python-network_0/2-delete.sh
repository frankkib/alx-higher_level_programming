#!/bin/bash
# Bash script that sends a DELETE request to the URL passed
url=$1
curl -X DELETE -s -w "\n%{http_code}" "$url" | sed '$d'
