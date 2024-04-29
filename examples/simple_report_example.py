import matplotlib.pyplot as plt
import pandas as pd
from confluence_report_generator.core import ConfluenceReportGenerator
from confluence_report_generator.utils import *
from datetime import datetime
import yaml
import numpy as np

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
# Sample data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"],
}
df = pd.DataFrame(data)


# Generate random data
np.random.seed(0)
x = np.random.rand(100)
y = np.random.rand(100)

# Create a scatter plot
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.scatter(x, y, color='red', label='Random Points')
# Add legend
ax.legend()
ax.set_xlabel("Data X")
ax.set_ylabel("Data Y")
ax.set_title("Random Data Plot")
ax.grid(True)
fig.tight_layout()
plt.show()

# Convert matplotlib figure to Confluence XML
image_xml = fig_to_confluence_xml(fig, image_title="Age Distribution")

# Convert pandas DataFrame to Confluence XML
table_xml = dataframe_to_confluence_xml(df, table_title="Employee Data")

# Create an action item
assignee = "John Doe"
due_date = datetime.now().strftime("%Y-%m-%d")
action_item_content = "Follow up with clients"
action_item_in_xml = action_item_xml(assignee, due_date, action_item_content)

# Create a decision
decision = "Approve budget proposal"
decision_date = datetime.now().strftime("%Y-%m-%d")
decision_xml = insert_decision_xml(decision)

# Create a hyperlink
url = "https://www.example.com"
link_text = "Visit Example Website"
hyperlink_xml = insert_link_xml(url, link_text)

# Create a new page and append content
page_title =  "Simple Report Example"

page_content = image_xml
# page_content = f"{decision}"
report_generator.create_page(
    space=space, title=page_title, parent_id=page_parent_ID, body=page_content
)
