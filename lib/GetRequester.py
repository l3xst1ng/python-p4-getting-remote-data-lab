import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.content
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def load_json(self):
        data = self.get_response_body()
        if data:
            try:
                return json.loads(data)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                return None
        return None