from itunes_review_extractor import itunes_review_extractor

# itunes_url = 'https://apps.apple.com/us/app/8-ball-pool/id543186831'
itunes_url = 'https://apps.apple.com/us/app/super-hexagon/id549027629'
e = itunes_review_extractor(itunes_url=itunes_url)
e.get_all_reviews()
