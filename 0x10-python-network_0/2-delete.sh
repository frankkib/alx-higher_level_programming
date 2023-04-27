#!/bin/bash
# Bash script that sends a DELETE request to the URL passed
curl -X DELETE -s -w "\n%{http_code}" "$1" 
