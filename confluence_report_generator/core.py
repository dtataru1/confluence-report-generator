from atlassian import Confluence
from .utils import is_valid_xml


class ConfluenceReportGenerator:
    def __init__(self, base_url: str, username: str, api_token: str):
        """
        Initialize the ConfluenceReportGenerator with API credentials.

        Args:
            base_url (str): Base URL of the Confluence site.
            username (str): Username for Confluence API access.
            api_token (str): API token for Confluence API access.
        """
        self.client = Confluence(url=base_url, username=username, password=api_token)

    def create_page(
        self, space: str, title: str, body: str, parent_id: int = None
    ) -> dict:
        """
        Create a Confluence page with specified XML content.

        Args:
            space (str): Key of the space where the page will be created.
            title (str): Title of the new page.
            body (str): XML content for the new page.
            parent_id (int): ID of the parent page.

        Returns:
            dict: Response from Confluence API.
        """
        is_valid_xml(body)
        # Check if the page already exists
        page_exists = self.page_exists(space, title)
        if page_exists:
            # Ask the user if they want to completely update the existing page
            user_input = input(
                f"The page '{title}' already exists. Do you want to completely update it? (yes/no): "
            ).lower()
            if user_input == "yes":
                # Update the existing page
                return self.client.update_page(
                    page_id=page_exists["id"], title=title, body=body
                )
            else:
                # Return without updating the page
                return {"message": "Page not updated."}
        else:
            # Create a new page
            return self.client.create_page(
                space=space, title=title, body=body, parent_id=parent_id
            )

    def page_exists(self, space: str, title: str) -> dict:
        """
        Check if a page with the given title already exists in the specified space.

        Args:
            space (str): Key of the space to search for the page.
            title (str): Title of the page to check for existence.

        Returns:
            dict: Details of the existing page if found, None otherwise.
        """
        try:
            page_id = self.client.get_page_id(space, title)
            page_details = self.client.get_page_by_id(page_id)
            return page_details
        except Exception as e:
            return None

    def update_page(self, page_id: str, new_content: str) -> dict:
        """
        Update a Confluence page with new XML content.

        Args:
            page_id (str): ID of the page to be updated.
            new_content (str): New XML content to update the page with.

        Returns:
            dict: Response from Confluence API.
        """

        page_info = self.client.get_page_by_id(page_id)
        new_body = page_info["body"]["storage"]["value"] + new_content
        is_valid_xml(new_body)
        return self.client.update_page(
            page_id=page_id,
            title=page_info["title"],
            body=new_body,
        )

    def delete_page(self, page_id: str) -> int:
        """
        Delete a Confluence page.

        Args:
            page_id (str): ID of the page to delete.

        Returns:
            int: Status code of the operation.
        """
        return self.client.remove_page(page_id)

    def append_content_to_page(self, page_id: str, content_to_append: str) -> dict:
        """
        Append specific content to the end of a Confluence page.

        Args:
            page_id (str): ID of the page to be updated.
            content_to_append (str): Content to append to the page.

        Returns:
            dict: Response from Confluence API.
        """
        page_info = self.client.get_page_by_id(page_id)
        new_body = page_info["body"]["storage"]["value"] + content_to_append
        is_valid_xml(new_body)
        return self.client.update_page(
            page_id=page_id,
            title=page_info["title"],
            body=new_body,
        )
