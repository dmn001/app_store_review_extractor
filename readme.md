# iTunes App Store review extractor in Python

## info

input = itunes_url

usage:

    python itunes_review_extractor.py itunes_url

e.g.

    python itunes_review_extractor.py https://apps.apple.com/us/app/super-hexagon/id549027629

get the review count

make requests in batches of 1000

output = 

    appid_app-name.json
    appid_app-name.csv

## notes

python 3+ dependencies: requests, unicodecsv

requests are made using the itunes user agent

output is most recent first

## todo

different country other than US

