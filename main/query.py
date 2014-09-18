#!/usr/bin/python
import json
import requests
from datetime import datetime
from config import NPR_API_KEY


def query_api(tag, numResults=10):
    """Hits the NPR API, returns JSON story list"""

    query = ('http://api.npr.org/query?orgid=692' +
        '&fields=title,storyDate,parent' +
        '&sort=dateDesc' +
        '&action=Or' +
        '&output=JSON' +
        '&numResults=%d' +
        '&id=%s' +
        '&apiKey=%s') % (numResults, str(tag), NPR_API_KEY)

    r = requests.get(query)
    j = json.loads(r.text)
    stories = j['list']['story']

    return stories


def get_posts(tag_id):
    stories = query_api(tag_id, 50)
    bad_tags = ['VPR News', 'The Frequency', 'News Features']
    posts = []
    for story in stories:
        post = {}
        post['title'] = story['title']['$text'].strip()
        post['link'] = story['link'][0]['$text']

        dow, day, month, year, time, tz = story['storyDate']['$text'].split(' ')
        month = datetime.strptime(month, "%b").strftime("%m")
        post['datetime'] = "%s-%s-%sT%s:%s" % (year, month, day, time, tz)

        tags = [tag['title']['$text'] for tag in story['parent']
            if tag['type'] == 'tag']
        keywords = [tag for tag in tags if tag not in bad_tags]
        post['keywords'] = ', '.join(keywords)

        date_of_post = datetime.strptime(year + month + day, "%Y%m%d")
        if (datetime.now() - date_of_post).days <= 2:
            posts.append(post)
    return posts
