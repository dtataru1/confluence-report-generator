import matplotlib.pyplot as plt
import pandas as pd
import io
import base64
import requests
from datetime import datetime


def fig_to_html(fig: plt.Figure, image_title: str = None, title_size: int = 1) -> str:
    """
    Convert a Matplotlib figure to an HTML image element.

    Args:
        fig (plt.Figure): Matplotlib figure object.
        image_title (str): Title for the image.
        title_size (int): Size of the title, from 1 (largest) to 6 (smallest).

    Returns:
        str: HTML image element with the base64 encoded image.
    """

    img_data = io.BytesIO()
    fig.savefig(img_data, format="png", bbox_inches="tight")
    img_data.seek(0)
    img_base64 = base64.b64encode(img_data.read()).decode("utf-8")
    img_html = f'<img src="data:image/png;base64,{img_base64}" alt="{image_title}"/>'

    if image_title:
        html_plot = f"<h{title_size}>{image_title}</h{title_size}>{img_html}"
    else:
        html_plot = img_html

    return html_plot


def dataframe_to_html(
    df: pd.DataFrame, table_title: str = None, title_size: int = 1
) -> str:
    """
    Convert a Pandas DataFrame to an HTML table.

    Args:
        df (pd.DataFrame): Pandas DataFrame to convert.
        table_title (str): Title for the table.
        title_size (int): Size of the title, from 1 (largest) to 6 (smallest).

    Returns:
        str: HTML table element with the DataFrame contents.
    """
    html_table = df.to_html(
        index=False, border=0, classes="confluenceTable", escape=False
    )
    html_table = html_table.replace('class="dataframe"', "").replace('border="1"', "")

    if table_title:
        return f"<h{title_size}>{table_title}</h{title_size}>{html_table}"
    else:
        return html_table


# Action item funcitonality

# image, video or file functionality


# mention functionality

#emoji funcitonality

#expand functionality

#table functionality

#code snippet functionality

#status functionality


#info panel functionality

#date functionality


#decision functionality

#note functionality

#success func

#warning func

#error func

#custom panel func


#bullet list

#layouts

#link

#numbered list

#divider

#quote

#heading 1->6

#help


##### JIRA STUFF #####
#jira issues

#asstes

#confluence lists





#office powerpoint


# related labels


# contributors summary

# filter results

# jira premium plan

# jira charts

# sprint burndown gadget

# average time in status

# page properties report


# labels list

# blog posts

# child pages (children display)


# table of contents

# recently updated dashboard

#task report

# jira premium page


# page properties report (what are page properties?)


# chart (display a chart)

# labels list

# anchor

# change history

# use profile

#