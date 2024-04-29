import matplotlib.pyplot as plt
import pandas as pd
from confluence_report_generator.core import ConfluenceReportGenerator
import yaml

# API connection details
with open("config/user_config.yaml", "r") as file:
    try:
        credentials = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        print(f"Error loading the user_config.yaml file: {exc}")
        exit()

space = "SIM"
page_parent_ID = 159416321

confluence_url = "https://dufouraero.atlassian.net"
atlassian_username = credentials["Atlassian-API-Credentials"]["username"]
atlassian_token = credentials["Atlassian-API-Credentials"]["password"]

report_generator = ConfluenceReportGenerator(
    base_url=confluence_url, username=atlassian_username, api_token=atlassian_token
)

confluence_page_title = "Simple Report Example"



# dates = pd.date_range(start='2024-01-01', end='2024-01-31', freq='D')

# # Generate random sales data
# np.random.seed(0)
# sales = np.random.randint(100, 500, size=len(dates))

# # Create the DataFrame
# df_time_series = pd.DataFrame({
#     'Date': dates,
#     'Sales': sales
# })

# confluence_page_body = ""
# confluence_page_body += confluence_chart_from_dataframe(df_time_series, chart_type="line", title="Daily Sales for January 2024", width=600, height=400)
# # confluence_page_body = insert_ifrmae


# # confluence_page_body += dataframe_to_html(df=df, table_title="Example Data Table from a pandas dataframe")
# # confluence_page_body += fetch_merged_pull_requests(
# #     user="dtataru1",
# #     repo="Projet_Billard",
# #     access_token=github_token,
# #     branch="master",
# #     since_date="2020-05-11",
# # )

# # confluence_page_body += insert_paragraph_text("This is a test paragraph.")
# # confluence_page_body += insert_info_section("This is an example info")
# # confluence_page_body += insert_tip_section("This is an example tip")
# # confluence_page_body += insert_note_section("This is an example note")
# # confluence_page_body += insert_warning_section("This is an example warning")
# # confluence_page_body += insert_code_block(code="print('This is a code block')")
# # confluence_page_body += generate_action_points(["Action Point 1", "Action Point 2", "Action Point 3"])
# # # confluence_page_body += link_prs_with_action_points(["Action Point 1", "Action Point 2", "Action Point 3"])
# # confluence_page_body += generate_pr_action_table(["Action Item 1"], [(44, "https://wwww.github.com")], ["Daniel Tataru"], ["2021-05-11"])
# # confluence_page_body += link_prs_with_action_points(["Action Point Previous 1"]<<<asy<qw, [(44, "https://www.github.com")])

# # confluence.create_page(
# #     space=space,
# #     title=confluence_page_title,
# #     body=confluence_page_body,
# #     parent_id=parent_ID,
# # )


# confluence.update_page(
#     page_id=669876229,
#     title=confluence_page_title,
#     body=confluence_page_body,
# )
