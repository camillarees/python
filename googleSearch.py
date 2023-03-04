from bs4 import BeautifulSoup
from googlesearch import search
import requests

search_term = input("Enter your search terms (separated by commas): ").split(",")

for term in search_term:
    results = search(term=term.strip(), num_results=10, lang="en")
    results = list(results)
    
print(f"Search results for '{term}':")
for i, result in enumerate(results):
    print(f"{i+1}. {result}")
    try:
        response = requests.get(result)
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.title.string
        description = soup.find("meta", {"name": "description"})['content']
        print(f"   Title: {title}")
        print(f"   Description: {description}")
        print()

    except:
        print("   Title: N/A")
        print("   Description: N/A")
        print()
