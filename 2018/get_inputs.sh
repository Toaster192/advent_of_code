#!/bin/bash

for i in {1..25}
do
   # Removed the potentionaly sensitive cookie data from here
   # If you want to use this yourself you will need to use your own cURL
   # (you need to be logged in to download the inputs since they are per-user
   # meaning you need to include the session here)
   curl "https://adventofcode.com/2018/day/$i/input" -H 'authority: adventofcode.com' -H 'cache-control: max-age=0' -H 'upgrade-insecure-requests: 1' -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' -H "referer: https://adventofcode.com/2018/day/$i" -H 'accept-encoding: gzip, deflate, br'  --compressed > "input$i"
done
