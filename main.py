import requests


def make_request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

target_input = "google.com"

with open("subdomainLister.txt", "r") as subdomain_list:
    for word in subdomain_list:
        word = word.strip()
        url = "https://" + word + "." + target_input
        response = make_request(url)
        if response:
            print("Found subdomain --->" + url)