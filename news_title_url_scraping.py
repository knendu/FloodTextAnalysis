# using requests_html library to scrape news articles from Google News, and extract information like the title and url of each article

from requests_html import HTMLSession

session = HTMLSession()
url = 'https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en'
r = session.get(url)

r.html.render(sleep=1, scrolldown=10)
articles = r.html.find('article')
print(articles)

newslist = []
for item in articles:
    try:
        newsitem = item.find('article', first=True)
        newsarticle = {
            'title': newsitem.text,
            'link': newsitem.absolute_links
        }
        newslist.append(newsarticle)
    except:
        pass
    
print(len(newslist))
print(newslist)