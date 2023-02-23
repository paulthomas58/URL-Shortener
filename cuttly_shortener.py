import requests
import sys

# Enter your API key from cutt.ly
api_key= "5c01d10470b91d09336eeba56cf47e83c0f9e"

# The URL to shorten
url = sys.argv[1]

api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"

# Make the request
data = requests.get(api_url).json()["url"]
if data["status"] == 7:
    shortened_url = data["shortLink"]
    print("Shortened URL: ", shortened_url)
else:
    print("[!] Error Shortening URL: ", data)