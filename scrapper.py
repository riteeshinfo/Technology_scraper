import requests
from bs4 import BeautifulSoup
import re


def extract_details(url):
    try:
        
        response = requests.get(url)
        response.raise_for_status()

        
        soup = BeautifulSoup(response.text, 'html.parser')

        
        social_links = []
        social_patterns = ['facebook', 'linkedin', 'twitter', 'instagram']

        for link in soup.find_all('a', href=True):
            for pattern in social_patterns:
                if pattern in link['href']:
                    social_links.append(link['href'])

        
        email_addresses = re.findall(r'\S+@\S+', soup.get_text())

        
        contact_details = re.findall(r'(\+\d{1,4}\s\d{1,10})', soup.get_text())

        
        print("Social links:")
        for link in social_links:
            print(link)

        print("\nEmail:")
        for email in email_addresses:
            print('support@',user_input)

        print("\nContact:")
        for contact in contact_details:
            print(contact)

    except requests.exceptions.RequestException as e:
        print("Error: Could not fetch the web page.")
    except Exception as e:
        print("An error occurred:", str(e))


user_input = input("Enter a website URL: ")


extract_details(user_input)
