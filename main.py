from dayu.news.weibo_top import handle_weibo
from dayu.news.google_news import handle_google_news, handle_google_news_sites
from dayu.news.hacker_news import handle_hacker_news
from dayu.news.news_api import handle_news_api
from dayu.news.rss import handle_rss
from dayu.news.good import pacing

import os
import shutil

import time, datetime

from baikal.rdbs.leisure_news import SqlLeisureNews
from viewer import html

sql_news = SqlLeisureNews("leisure_news")
sql_news.open()

loop = True
while loop:
    loop = False
    current_time = datetime.datetime.now()  #.time()
    # work during 5-7am
    #if current_time.time() < datetime.time(8, 0, 0) or current_time.time() >= datetime.time(10, 0, 0):
    #    time.sleep(7200)  # Sleep for 2 hours (7200 seconds)
    #    continue

    print("crawling @ ", current_time)
    records = []
    handle_weibo(records)
    pacing()
    handle_google_news(records)
    pacing()
    handle_hacker_news(records)
    pacing()
    handle_news_api(records)
    pacing()
    handle_google_news_sites(records)
    pacing()
    handle_rss(records)
    pacing()

    for r in records:
        sql_news.add_record(r)

    time.sleep(10)

    print("updating @ ", current_time)
    # Generate date-based filename
    os.makedirs("htmls", exist_ok=True)
    date_filename = current_time.strftime("%Y-%m-%d.html")
    htmls_path = os.path.join("htmls", date_filename)

    with open(htmls_path, "w") as page:
        df = sql_news.get_data_frame()
        df = df.loc[:, ['affiliation', 'venue', 'title', 'overview', 'url']]
        #page.write(df.to_markdown())
        page.write(html(df))
    
    # Copy file: index.html <- news/2026-01-17.html
    if os.path.exists("index.html"):
        os.remove("index.html")
    shutil.copy2(htmls_path, "index.html")
    print("done")
sql_news.close()
