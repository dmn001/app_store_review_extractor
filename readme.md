#iTunes app review extractor in Python

##info

input = itunes_url

usage:

    python itunes_review_extractor.py itunes_url

e.g.

    python itunes_review_extractor.py https://itunes.apple.com/us/app/sparkle-unleashed/id824153738?mt=8

get the review count

make requests in batches of 1000

output = appid_app-name.json

##notes

python 2.7+ dependencies: requests, unicodecsv

requests are made using the itunes user agent

output is most recent first

##todo

different country other than US

##links

http://docs.python-requests.org/en/latest/user/advanced/

http://stackoverflow.com/questions/12309269/write-json-data-to-file-in-python

http://jsonviewer.stack.hu/

http://stackoverflow.com/questions/10569438/how-to-print-unicode-character-in-python

http://stackoverflow.com/questions/17245415/read-and-write-csv-files-including-unicode-with-python-2-7

https://pypi.python.org/pypi/unicodecsv/0.9.4
