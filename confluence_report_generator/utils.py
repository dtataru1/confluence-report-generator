import matplotlib.pyplot as plt
import pandas as pd
import io
import base64
import xml.etree.ElementTree as ET


def is_valid_xml(xml_string: str) -> bool:
    """Check if a string is a valid XML document.

    Args:
        xml_string (str): String to check if it is a valid XML document.

    Returns:
        bool: True if the string is a valid XML document, False otherwise.
    """
    try:
        ET.fromstring(xml_string)
        return True
    except ET.ParseError:
        return False


def fig_to_confluence_xml(
    fig: plt.Figure, image_title: str = None, title_size: str = "Large"
) -> str:
    """
    Convert a Matplotlib figure to a Confluence XML image macro.

    Args:
        fig (plt.Figure): Matplotlib figure object.
        image_title (str): Title for the image.
        title_size (str): Size of the title (Large, Medium, Small, etc.).

    Returns:
        str: Confluence XML with the base64 encoded image.
    """

    img_data = io.BytesIO()
    fig.savefig(img_data, format="png", bbox_inches="tight")
    img_data.seek(0)
    img_base64 = base64.b64encode(img_data.read()).decode("utf-8")

    xml = (
        f'<ac:image ac:height="300">'
        f'<ri:attachment ri:filename="{image_title}.png" />'
        f'<ac:parameter ac:name="atlassian-macro-output-type">BLOCK</ac:parameter>'
        f"</ac:image>"
    )

    if image_title:
        return f"<h1>{image_title}</h1>{xml}"
    else:
        return xml


def dataframe_to_confluence_xml(
    df: pd.DataFrame, table_title: str = None, title_size: str = "Large"
) -> str:
    """
    Convert a Pandas DataFrame to a Confluence XML table.

    Args:
        df (pd.DataFrame): Pandas DataFrame to convert.
        table_title (str): Title for the table.
        title_size (str): Size of the title (Large, Medium, Small, etc.).

    Returns:
        str: Confluence XML table element with the DataFrame contents.
    """

    xml_table = '<ac:structured-macro ac:name="table"><ac:parameter ac:name="title">{}</ac:parameter><ac:parameter ac:name="class">confluenceTable</ac:parameter><ac:rich-text-body><table><tbody>'.format(
        table_title
    )
    for idx, row in df.iterrows():
        xml_table += "<tr>"
        for item in row:
            xml_table += f"<td>{item}</td>"
        xml_table += "</tr>"
    xml_table += "</tbody></table></ac:rich-text-body></ac:structured-macro>"

    if table_title:
        return f"<h1>{table_title}</h1>{xml_table}"
    else:
        return xml_table


def action_item_xml(assignee: str, due_date: str, content: str) -> str:
    """
    Generate Confluence XML for an action item.

    Args:
        assignee (str): User assigned to the action item.
        due_date (str): Due date in the format 'YYYY-MM-DD'.
        content (str): Description of the action item.

    Returns:
        str: Confluence XML for an action item.
    """

    return f"<ac:task-list><ac:task><ac:task-id /><ac:task-status>incomplete</ac:task-status><ac:task-body>{content}</ac:task-body><ac:task-assignee>{assignee}</ac:task-assignee><ac:task-due>{due_date}</ac:task-due></ac:task></ac:task-list>"


def media_xml(media_type: str, filename: str) -> str:
    """
    Generate Confluence XML for embedding an image, video, or file.

    Args:
        media_type (str): Type of media ('image', 'video', 'file').
        filename (str): The filename of the media to embed.

    Returns:
        str: Confluence XML for the specified media type.
    """
    if media_type == "image":
        tag = "ac:image"
    elif media_type == "video":
        tag = "ac:video"
    else:
        tag = "ri:attachment"
        return f'<ac:link><ri:attachment ri:filename="{filename}" /></ac:link>'

    return f'<{tag}><ri:attachment ri:filename="{filename}" /></{tag}>'


def mention_user_xml(username: str) -> str:
    """
    Generate Confluence XML for mentioning a user.

    Args:
        username (str): Username of the person to mention.

    Returns:
        str: Confluence XML for mentioning a user.
    """
    return f'<ac:link><ri:user ri:username="{username}" /></ac:link>'


def insert_expand_xml(title: str, content: str) -> str:
    """
    Generate Confluence XML for an expandable section.

    Args:
        title (str): Title of the expandable section.
        content (str): Content inside the expand section.

    Returns:
        str: Confluence XML for an expand section.
    """
    return f'<ac:structured-macro ac:name="expand"><ac:parameter ac:name="title">{title}</ac:parameter><ac:rich-text-body>{content}</ac:rich-text-body></ac:structured-macro>'


def insert_code_snippet_xml(language: str, code: str) -> str:
    """
    Generate Confluence XML for a code snippet.

    Args:
        language (str): Programming language of the code.
        code (str): The actual code snippet.

    Returns:
        str: Confluence XML for a code snippet.
    """
    return f'<ac:structured-macro ac:name="code"><ac:parameter ac:name="language">{language}</ac:parameter><ac:plain-text-body><![CDATA[{code}]]></ac:plain-text-body></ac:structured-macro>'


def insert_status_xml(status: str) -> str:
    """
    Generate Confluence XML for a status label.

    Args:
        status (str): The status label to display.

    Returns:
        str: Confluence XML for a status label.
    """
    return f'<ac:structured-macro ac:name="status"><ac:parameter ac:name="title">{status}</ac:parameter></ac:structured-macro>'


def linked_status_xml(action_item_content: str, status: str) -> str:
    """
    Generate Confluence XML for an action item linked to a status label.

    Args:
        action_item_content (str): Description of the action item.
        status (str): The status label to display.

    Returns:
        str: Confluence XML for an action item linked to a status label.
    """
    return f'{action_item_xml("assignee_placeholder", "due_date_placeholder", action_item_content)}{insert_status_xml(status)}'


def insert_message_xml(message_type: str, message: str) -> str:
    """
    Generate Confluence XML for information blocks like note, success, warning, or error.

    Args:
        message_type (str): Type of the message ('info', 'note', 'success', 'warning', 'error').
        message (str): The content of the message.

    Returns:
        str: Confluence XML for the message block.
    """
    return f'<ac:message ac:type="{message_type}">{message}</ac:message>'


def insert_decision_xml(decision: str, decision_date: str) -> str:
    """
    Generate Confluence XML for a decision.

    Args:
        decision (str): The decision made.
        decision_date (str): The date the decision was made.

    Returns:
        str: Confluence XML for the decision.
    """
    return f'<ac:structured-macro ac:name="decision"><ac:parameter ac:name="decision">{decision}</ac:parameter><ac:parameter ac:name="date">{decision_date}</ac:parameter></ac:structured-macro>'


def insert_date_xml(date: str) -> str:
    """
    Generate Confluence XML for displaying a date.

    Args:
        date (str): The date to display.

    Returns:
        str: Confluence XML for displaying the date.
    """
    return f'<time datetime="{date}">{date}</time>'


def insert_list_xml(items: list, list_type: str = "bullet") -> str:
    """
    Generate Confluence XML for a list (bullet or numbered).

    Args:
        items (list): List of items to include in the list.
        list_type (str): Type of the list ('bullet' or 'numbered').

    Returns:
        str: Confluence XML for the list.
    """
    tag = "ul" if list_type == "bullet" else "ol"
    list_items = "".join(f"<li>{item}</li>" for item in items)
    return f"<{tag}>{list_items}</{tag}>"


def insert_layout_xml(content_sections: list) -> str:
    """
    Generate Confluence XML for a layout with multiple sections.

    Args:
        content_sections (list): A list of content sections to be placed in the layout.

    Returns:
        str: Confluence XML for the layout.
    """
    sections_xml = "".join(
        f'<ac:layout-section ac:type="single"><ac:layout-cell>{section}</ac:layout-cell></ac:layout-section>'
        for section in content_sections
    )
    return f"<ac:layout>{sections_xml}</ac:layout>"


def insert_link_xml(url: str, link_text: str) -> str:
    """
    Generate Confluence XML for a hyperlink.

    Args:
        url (str): URL to link to.
        link_text (str): Text of the hyperlink.

    Returns:
        str: Confluence XML for the hyperlink.
    """
    return f'<ac:link><ri:url ri:value="{url}" /><ac:plain-text-link-body><![CDATA[{link_text}]]></ac:plain-text-link-body></ac:link>'


def insert_paragraph_xml(content: str) -> str:
    """
    Generate Confluence XML for a paragraph.

    Args:
        content (str): Text content of the paragraph.

    Returns:
        str: Confluence XML for the paragraph.
    """
    return f"<p>{content}</p>"


def insert_heading_xml(content: str, level: int) -> str:
    """
    Generate Confluence XML for a heading.

    Args:
        content (str): Text content of the heading.
        level (int): Heading level (1 to 6).

    Returns:
        str: Confluence XML for the heading.
    """
    return f"<h{level}>{content}</h{level}>"


def insert_toc_xml() -> str:
    """
    Generate Confluence XML for a table of contents.

    Returns:
        str: Confluence XML for the table of contents.
    """
    return '<ac:structured-macro ac:name="toc" />'


def insert_child_pages_list_xml() -> str:
    """
    Generate Confluence XML for listing child pages of the current page.

    Returns:
        str: Confluence XML for listing child pages.
    """
    return '<ac:structured-macro ac:name="children" />'


def insert_task_report_xml() -> str:
    """
    Generate Confluence XML for a task report.

    Returns:
        str: Confluence XML for a task report.
    """
    return '<ac:structured-macro ac:name="task-report" />'


def insert_page_properties_report_xml() -> str:
    """
    Generate Confluence XML for a page properties report.

    Returns:
        str: Confluence XML for a page properties report.
    """
    return '<ac:structured-macro ac:name="page-properties-report" />'


def insert_change_history_xml() -> str:
    """
    Generate Confluence XML for displaying the change history of a page.

    Returns:
        str: Confluence XML for the change history.
    """
    return '<ac:structured-macro ac:name="change-history" />'


def insert_contributions_summary_xml() -> str:
    """
    Generate Confluence XML for summarizing contributions to a page.

    Returns:
        str: Confluence XML for contributions summary.
    """
    return '<ac:structured-macro ac:name="contributor-summary" />'


def insert_iframe_xml(url: str, width: str = "100%", height: str = "300px") -> str:
    """
    Generate Confluence XML for embedding an Iframe, useful for embedding external content like dynamic plots.

    Args:
        url (str): URL of the content to be embedded.
        width (str): Width of the iframe (default is "100%").
        height (str): Height of the iframe (default is "300px").

    Returns:
        str: Confluence XML for an iframe.
    """
    return f'<ac:structured-macro ac:name="iframe"><ac:parameter ac:name="src">{url}</ac:parameter><ac:parameter ac:name="width">{width}</ac:parameter><ac:parameter ac:name="height">{height}</ac:parameter></ac:structured-macro>'
