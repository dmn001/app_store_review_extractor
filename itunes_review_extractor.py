import requests, json

class itunes_review_extractor():
    def __init__(self,appid):
        self.appid = appid
        self.user_agent_string = 'iTunes/11.1.5 (Windows; Microsoft Windows 7 x64 Ultimate Edition Service Pack 1 (Build 7601)) AppleWebKit/537.60.15'
        self.start_index = 0
        self.range = 100
        self.end_index = self.start_index + self.range - 1
        
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
        self.review_count = int(self.json_string['totalNumberOfReviews'])
        # print "totalNumberOfReviews =", self.json_string['totalNumberOfReviews']
        return self.review_count

    def get_reviews(self,start_index=None):
        if start_index is None:
            start_index = self.start_index
        else:
            self.update_end_index()
        self.url = 'https://itunes.apple.com/WebObjects/MZStore.woa/wa/userReviewsRow?id=%s&displayable-kind=11&startIndex=%s&endIndex=%s&sort=4&appVersion=all' % (self.appid,start_index,self.end_index)
        self.response = self.session.get(self.url)
        self.json_string = self.response.json()
        return self.json_string

    def get_all_reviews(self):
        self.review_count = 1234
        while(self.start_index < self.review_count):
            print self.start_index
            self.update_end_index()
            self.start_index = self.start_index + self.range


    def update_end_index(self):
        self.end_index = self.start_index + self.range - 1

    # def print_reviews(self):
    #     for item in self.json_string['userReviewList']:
    #         print item['body']

    def output_to_file(self):
        with open(self.appid+'.json', 'w') as outfile:
          json.dump(self.response.json(), outfile)


        # body, rating, name, title, voteSum, voteCount, date, userReviewId
