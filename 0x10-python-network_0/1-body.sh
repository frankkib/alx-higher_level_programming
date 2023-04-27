#!/bin/bash
#Bash script that takes in a URL, sends a GET request to the URL, and displays
curl -fLs -X GET "$1" 
