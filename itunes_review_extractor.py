import requests, json, re, sys, unicodecsv, codecs

class itunes_review_extractor():
    def __init__(self,appid=None,itunes_url=None):
        if itunes_url is not None:
            ret = self.get_id_from_url(itunes_url)
            if ret == -1:
                return
        if appid is not None:
            self.appid = appid
            self.app_name = ''

        self.out_base_filename = self.appid + self.app_name
        
        self.user_agent_string = 'iTunes/11.1.5 (Windows; Microsoft Windows 7 x64 Ultimate Edition Service Pack 1 (Build 7601)) AppleWebKit/537.60.15'

        self.start_index = 0
        self.range = 1000
        self.end_index = self.start_index + self.range - 1
        
        self.session = requests.Session()
        self.session.headers.update({'User-Agent':self.user_agent_string})

        self.review_count = 0
        self.results = []

        self.csv_fh = None

    def get_review_info(self):
        self.url = 'https://itunes.apple.com/us/customer-reviews/id%s?dataOnly=true&displayable-kind=11&appVersion=all' % (self.appid)
        self.response = self.session.get(self.url)
        self.json_string = self.response.json()
        return self.json_string

    def get_review_count(self):
        self.get_review_info()
        self.review_count = int(self.json_string['totalNumberOfReviews'])
        return self.review_count

    def get_reviews(self,start_index=None):
        if start_index is None:
            start_index = self.start_index
        else:
            self.update_end_index()
        self.url = 'https://itunes.apple.com/WebObjects/MZStore.woa/wa/userReviewsRow?id=%s&displayable-kind=11&startIndex=%s&endIndex=%s&sort=4&appVersion=all' % (self.appid,start_index,self.end_index)
        print self.url
        self.response = self.session.get(self.url)
        self.json_string = self.response.json()
        return self.json_string

    def get_all_reviews(self):
        self.get_review_count()
        print "getting %i reviews" % self.review_count
        self.output_csv_init()
        while(self.start_index < self.review_count):
            self.update_end_index()
            print self.start_index, self.end_index
            json_string = self.get_reviews()
            self.start_index = self.start_index + self.range
            self.append_json_list_to_results(json_string)
            self.output_append_to_csv(json_string)
        self.output_results_to_json()

    def append_json_list_to_results(self,json_string):
        self.results = self.results + json_string['userReviewList']

    def output_csv_init(self):
        self.csv_fh = codecs.open(self.out_base_filename+'.csv', 'wb')
        self.csv_fh.write(u'\uFEFF'.encode('utf8'))
        header = ['userReviewId', 'date', 'voteSum', 'voteCount', 'rating', 'name', 'title', 'body']
        self.csv_unicode_writer = unicodecsv.writer(self.csv_fh, encoding='utf-8')
        self.csv_unicode_writer.writerow(header)

    def output_append_to_csv(self,json_string):
        # userReviewId, date, voteSum, voteCount, rating, name, title, body
        for r in json_string['userReviewList']:
            out_list = [r['userReviewId'],r['date'],r['voteSum'],r['voteCount'],r['rating'],r['name'],r['title'],r['body']]
            self.csv_unicode_writer.writerow(out_list)

    def update_end_index(self):
        self.end_index = self.start_index + self.range - 1
        if self.end_index > self.review_count:
            self.end_index = self.review_count - 1

    def output_results_to_json(self):
        with open(self.out_base_filename+'.json', 'w') as outfile:
            json.dump(self.results, outfile)
        print "output to %s" % self.out_base_filename+'.json'

    def get_id_from_url(self,itunes_url):
        m = re.search(r"/([^/]+)/id(\d+)",itunes_url)
        if m:
            # print m.groups()
            self.app_name = '_' + m.groups()[0]
            self.appid = m.groups()[1]
        else:
            print "error, no match found"
            return -1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        itunes_url = sys.argv[1]
    else:
        print "usage: 'python itunes_review_extractor.py itunes_url'"
        itunes_url = 'https://itunes.apple.com/us/app/sparkle-unleashed/id824153738?mt=8'
        print "e.g. : %s" % itunes_url
    e = itunes_review_extractor(itunes_url=itunes_url)
    e.get_all_reviews()