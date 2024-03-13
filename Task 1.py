import requests
from bs4 import BeautifulSoup

def scrape_news_headlines(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all elements with the specified class (or any other method to locate the desired data)
        headlines = soup.find_all('h2', class_='headline')
        
        # Extract the text from each headline and print it
        for headline in headlines:
            print(headline.text)
    else:
        print("Error: Failed to retrieve webpage")

# Example usage
url = "https://www.example.com/news"
scrape_news_headlines(url)