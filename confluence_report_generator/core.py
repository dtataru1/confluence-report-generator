from .api_client import ConfluenceClient
from .utils import fig_to_confluence_xml, dataframe_to_confluence_xml


class ConfluenceReportGenerator:
    def __init__(self, base_url: str, username: str, api_token: str):
        """
        Initialize the ConfluenceReportGenerator with API credentials.

        Args:
            base_url (str): Base URL of the Confluence site.
            username (str): Username for Confluence API access.
            api_token (str): API token for Confluence API access.
        """
        self.client = ConfluenceClient(base_url, username, api_token)

   
    def create_page(self, space: str, title: str, body: str) -> dict:
        """
        Create a Confluence page with specified XML content.

        Args:
            space (str): Key of the space where the page will be created.
            title (str): Title of the new page.
            body (str): XML content for the new page.

        Returns:
            dict: Response from Confluence API.
        """
        return self.client.create_page(space, title, body)

    def update_page(self, page_id: str, new_content: str) -> dict:
        """
        Update a Confluence page with new XML content.

        Args:
            page_id (str): ID of the page to be updated.
            new_content (str): New XML content to update the page with.

        Returns:
            dict: Response from Confluence API.
        """
        page_info = self.client.get_page(page_id)
        new_body = page_info["body"]["storage"]["value"] + new_content
        return self.client.update_page(
            page_id, page_info["title"], new_body, page_info["version"]["number"]
        )

    def delete_page(self, page_id: str) -> int:
        """
        Delete a Confluence page.

        Args:
            page_id (str): ID of the page to delete.

        Returns:
            int: Status code of the operation.
        """
        return self.client.delete_page(page_id)
