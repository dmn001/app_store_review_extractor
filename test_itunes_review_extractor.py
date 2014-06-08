from itunes_review_extractor import itunes_review_extractor

e = itunes_review_extractor('624555293')

e.get_url()
# e.print_reveiews()
e.output_to_file()