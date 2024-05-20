import requests


def call_client(filling):
    # Make a GET request to a URL
    response = requests.get('https://httpbin.org/get?filling={filling}')
    if response.status_code == 200:
        # Print the response content (typically JSON or HTML)
        print(response.json())
    else:
        # Print an error message if the request was unsuccessful
        print(f"Error: {response.status_code}")
