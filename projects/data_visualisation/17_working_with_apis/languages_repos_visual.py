import requests
import plotly.express as px

from prompt_functions import prompt_user_choice

# Prompt user for a language to generate chart for.
languages = ['Python', 'JavaScript', 'Ruby', 'C', 
             'Java', 'Perl', 'Haskell', 'Go']
prompt= "Which of these languages are you willing to explore"
prompt += " its most popular projects visually?"
choice_index = prompt_user_choice(prompt, languages)
print(f"\nGenerating chart for {languages[choice_index]}...")

# Make an API call and check the response
url = "https://api.github.com/search/repositories"
url += f"?q=language:{languages[choice_index].lower()}"
url += "&sort=stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"\tStatus code: {r.status_code}")

# Process overall results.
response_dict = r.json()
print(f"\tComplete results: {not response_dict['incomplete_results']}")

# Process repository info.
repo_dicts = response_dict['items']
repo_links, stars_counts, hover_texts = [], [], []
for repo_dict in repo_dicts:
    # Turn repo names into active links.
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars_counts.append(repo_dict['stargazers_count'])

    # Build hover texts.
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# Make visualization.
title = f"Most-Starred {languages[choice_index]} Projects on GitHub"
labels = {"x": "Repository", "y": "Stars"}
fig = px.bar(x=repo_links, y=stars_counts, title=title, labels=labels, 
             hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20, 
                  yaxis_title_font_size=20)

fig.update_traces(marker_color='IndianRed', marker_opacity=0.6)

fig.show()
