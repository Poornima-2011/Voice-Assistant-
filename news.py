# news.py
import requests

def get_news():
    # Example API request to get news data (using NewsAPI)
    api_key = '09848dad63ee4bb19c3d10f473607c7f'
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'ok':
        articles = data['articles'][:5]  # Get top 5 articles
        news_list = [f"Title: {article['title']}\nDescription: {article['description']}" for article in articles]
        return "\n\n".join(news_list)
    else:
        return "Could not retrieve news."
