import requests


class ConfluenceClient:
    def __init__(self, base_url: str, username: str, api_token: str) -> None:
        """
        Initialize the ConfluenceClient with API credentials.

        Args:
            base_url (str): The base URL for the Confluence API.
            username (str): The username used for API authentication.
            api_token (str): The API token for authentication.
        """
        self.base_url = base_url
        self.auth = (username, api_token)

    def create_page(self, space: str, title: str, body: str) -> dict:
        """
        Create a Confluence page in a specified space with given title and body.

        Args:
            space (str): Key of the space where the page will be created.
            title (str): Title of the new page.
            body (str): Body of the new page in storage format (typically HTML/XML).

        Returns:
            dict: JSON response from Confluence API indicating success or failure.
        """
        url = f"{self.base_url}/rest/api/content"
        headers = {"Content-Type": "application/json"}
        data = {
            "type": "page",
            "title": title,
            "space": {"key": space},
            "body": {"storage": {"value": body, "representation": "storage"}},
        }
        response = requests.post(url, json=data, headers=headers, auth=self.auth)
        return response.json()

    def update_page(self, page_id: str, title: str, body: str, version: int) -> dict:
        """
        Update an existing Confluence page identified by page_id with new title, body, and version.

        Args:
            page_id (str): The ID of the page to be updated.
            title (str): The new title for the page.
            body (str): The new body of the page in storage format.
            version (int): The current version of the page to increment.

        Returns:
            dict: JSON response from Confluence API indicating success or failure.
        """
        url = f"{self.base_url}/rest/api/content/{page_id}"
        headers = {"Content-Type": "application/json"}
        data = {
            "id": page_id,
            "type": "page",
            "title": title,
            "body": {"storage": {"value": body, "representation": "storage"}},
            "version": {"number": version + 1},
        }
        response = requests.put(url, json=data, headers=headers, auth=self.auth)
        return response.json()

    def get_page(self, page_id: str) -> dict:
        """
        Retrieve a Confluence page by its ID.

        Args:
            page_id (str): The ID of the page to retrieve.

        Returns:
            dict: JSON response containing the page details from Confluence API.
        """
        url = f"{self.base_url}/rest/api/content/{page_id}?expand=body.storage,version"
        response = requests.get(url, auth=self.auth)
        return response.json()

    def delete_page(self, page_id: str) -> int:
        """
        Delete a Confluence page by its ID.

        Args:
            page_id (str): The ID of the page to delete.

        Returns:
            int: HTTP status code indicating success or failure of the delete operation.
        """
        url = f"{self.base_url}/rest/api/content/{page_id}"
        response = requests.delete(url, auth=self.auth)
        return response.status_code
