import requests

class ConfluenceClient:
    def __init__(self, base_url, username, api_token):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.auth = (username, api_token)

    def get_page(self, page_id):
        """ Fetch a Confluence page by ID """
        url = f"{self.base_url}/wiki/rest/api/content/{page_id}"
        response = self.session.get(url)
        return response.json()

    def create_page(self, space, title, body):
        """ Create a Confluence page """
        url = f"{self.base_url}/wiki/rest/api/content"
        data = {
            "type": "page",
            "title": title,
            "space": {"key": space},
            "body": {
                "storage": {
                    "value": body,
                    "representation": "storage"
                }
            }
        }
        response = self.session.post(url, json=data)
        return response.json()

    def update_page(self, page_id, title, body, version):
        """ Update a Confluence page """
        url = f"{self.base_url}/wiki/rest/api/content/{page_id}"
        data = {
            "id": page_id,
            "type": "page",
            "title": title,
            "version": {"number": version + 1},
            "body": {
                "storage": {
                    "value": body,
                    "representation": "storage"
                }
            }
        }
        response = self.session.put(url, json=data)
        return response.json()

    def delete_page(self, page_id):
        """ Delete a Confluence page """
        url = f"{self.base_url}/wiki/rest/api/content/{page_id}"
        response = self.session.delete(url)
        return response.status_code
