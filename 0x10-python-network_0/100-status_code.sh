#!/bin/bash
#Bash script that sends a request to a URL passed as an argument
curl -o /dev/null -s --write-out '%{http_code}\n' "$1"
