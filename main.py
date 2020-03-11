from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='dd21ae73b23140fd868973b2647c75a5')

def news(amount_of_stories, q):
    top_headlines = newsapi.get_top_headlines(q=q)
    for i in range(0, int(amount_of_stories)):
        try:
            print(top_headlines.get('articles')[i].get('title'))#, top_headlines.get('articles')[i].get('url'))
        except IndexError:
            print('Not enough articles')
            break
while True:
    q = input('What would you like to read about?')
    amount_of_stories = input('How many stories would you like to read?')
    news(amount_of_stories, q)