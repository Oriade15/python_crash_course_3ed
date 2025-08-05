import requests
import plotly.graph_objects as go

from prompt_functions import prompt_user_choice

# Prompt user for a language to generate chart for.
languages = ['Python', 'JavaScript', 'Ruby', 'C', 
             'Java', 'Perl', 'Haskell', 'Go']
prompt= "Which of these languages are you willing to explore"
prompt += " its most popular projects visually?"
choice_index = prompt_user_choice(prompt, languages)
print(f"\nGenerating chart for {languages[choice_index]}...")

# Step 1: Fetch data from the GitHub API
url = "https://api.github.com/search/repositories"
url += f"?q=language:{languages[choice_index]}&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
response = requests.get(url, headers=headers)
response_dict = response.json()

# Step 2: Extract relevant data
repo_dicts = response_dict["items"][:10]  # Top 10 repositories
repo_names = [repo["name"] for repo in repo_dicts]
stars = [repo["stargazers_count"] for repo in repo_dicts]
forks = [repo["forks_count"] for repo in repo_dicts]
issues = [repo["open_issues_count"] for repo in repo_dicts]

# Step 3: Create a grouped bar chart using Plotly
fig = go.Figure()

# Add bars for stars
fig.add_trace(go.Bar(
    x=repo_names,
    y=stars,
    name="Stars",
    marker_color="skyblue"
))

# Add bars for forks
fig.add_trace(go.Bar(
    x=repo_names,
    y=forks,
    name="Forks",
    marker_color="orange"
))

# Add bars for open issues
fig.add_trace(go.Bar(
    x=repo_names,
    y=issues,
    name="Open Issues",
    marker_color="green"
))

# Step 4: Customize the layout
fig.update_layout(
    title=f"Comparison of Top 10 {languages[choice_index]} Repositories on GitHub",
    xaxis_title="Repositories",
    yaxis_title="Count",
    barmode="group",  # Grouped bar chart
    xaxis_tickangle=-45,
    template="plotly_white"
)

# Step 5: Show the chart
fig.show()