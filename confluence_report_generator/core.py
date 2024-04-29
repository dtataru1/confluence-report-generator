from .api_client import ConfluenceClient
from .utils import fig_to_confluence_xml, dataframe_to_confluence_xml  # and others as needed

class ConfluenceReportGenerator:
    def __init__(self, base_url, username, api_token):
        self.client = ConfluenceClient(base_url, username, api_token)

    def create_report_page(self, space, title, figures, dataframes, text_content):
        body_xml = ''
        for fig in figures:
            body_xml += fig_to_confluence_xml(fig, image_title="Figure")
        for df in dataframes:
            body_xml += dataframe_to_confluence_xml(df, table_title="Data Table")
        body_xml += text_content
        return self.client.create_page(space, title, body_xml)

    def update_report_page(self, page_id, new_content):
        page_info = self.client.get_page(page_id)
        new_body = page_info['body']['storage']['value'] + new_content
        return self.client.update_page(page_id, page_info['title'], new_body, page_info['version']['number'])

    def delete_report_page(self, page_id):
        return self.client.delete_page(page_id)
