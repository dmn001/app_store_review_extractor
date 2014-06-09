from itunes_review_extractor import itunes_review_extractor

itunes_url = 'https://itunes.apple.com/gb/app/trials-frontier/id659283309?mt=8'
try:
	e = itunes_review_extractor(itunes_url=itunes_url)
	e.get_all_reviews()
except Exception, e:
	# raise e
	pass