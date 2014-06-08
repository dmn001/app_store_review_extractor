import requests, json

class itunes_review_extractor():
    def __init__(self,appid):
        self.appid = appid
        self.user_agent_string = 'iTunes/11.1.5 (Windows; Microsoft Windows 7 x64 Ultimate Edition Service Pack 1 (Build 7601)) AppleWebKit/537.60.15'
        self.start_index = 0
        self.end_index = self.start_index + 100
        
        self.session = requests.Session()
        self.session.headers.update({'User-Agent':self.user_agent_string})

        self.review_count = 0

    def get_review_info(self):
        self.url = 'https://itunes.apple.com/us/customer-reviews/id%s?dataOnly=true&displayable-kind=11&appVersion=all' % (self.appid)
        self.response = self.session.get(self.url)
        self.json_string = self.response.json()
        return self.json_string

    def get_review_count(self):
        self.get_review_info()
        print "totalNumberOfReviews =", self.json_string['totalNumberOfReviews']

    def get_reviews(self):
        self.url = 'https://itunes.apple.com/WebObjects/MZStore.woa/wa/userReviewsRow?id=%s&displayable-kind=11&startIndex=%s&endIndex=%s&sort=4&appVersion=all' % (self.appid,self.start_index,self.end_index)
        self.response = self.session.get(self.url)
        self.json_string = self.response.json()
        return self.json_string

    # def print_reviews(self):
    #     for item in self.json_string['userReviewList']:
    #         print item['body']

    def output_to_file(self):
        with open(self.appid+'.json', 'w') as outfile:
          json.dump(self.response.json(), outfile)


        # body, rating, name, title, voteSum, voteCount, date, userReviewId
