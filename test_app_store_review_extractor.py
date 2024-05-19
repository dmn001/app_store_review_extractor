from app_store_review_extractor import app_store_review_extractor

# app_store_url = 'https://apps.apple.com/us/app/8-ball-pool/id543186831'
app_store_url = 'https://apps.apple.com/us/app/super-hexagon/id549027629'
e = app_store_review_extractor(app_store_url=app_store_url)
e.get_all_reviews()
