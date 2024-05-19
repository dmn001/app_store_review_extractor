import requests, json
from pprint import pprint

appid = '624555293'

user_agent_string = 'iTunes/11.1.5 (Windows; Microsoft Windows 7 x64 Ultimate Edition Service Pack 1 (Build 7601)) AppleWebKit/537.60.15'

start_index = 0
end_index = start_index + 1000

url = 'https://itunes.apple.com/WebObjects/MZStore.woa/wa/userReviewsRow?id=%s&displayable-kind=11&startIndex=%s&endIndex=%s&sort=4&appVersion=all' % (appid,start_index,end_index)

s = requests.Session()

s.headers.update({'User-Agent':user_agent_string})

print(s.headers)

r = s.get(url)

j = r.json()

pprint(j['userReviewList'][0])


with open(appid+'.json', 'w') as outfile:
    json.dump(r.json(), outfile)


# body, rating, name, title, voteSum, voteCount, date, userReviewId
