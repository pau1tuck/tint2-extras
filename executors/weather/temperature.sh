#!/bin/bash

# Store the API endpoint in a variable
endpoint="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Mae%20Chan?unitGroup=metric&include=current&key=ASRQL55QSXYKL63Y2DCEMFUC3&contentType=json"

# Make the API request using curl
response=$(curl -s "$endpoint")

# Parse the JSON response using jq
parsed_response=$(echo "$response" | jq)

# Print the parsed JSON response
echo "$parsed_response"