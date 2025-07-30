from operator import itemgetter

import requests
import plotly.express as px

# Make an API call & check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a new api call for each submission:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}, status code: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article, skip the ones without comments
    submission_dict = {}
    try:
        submission_dict['comments'] = response_dict['descendants']
    except KeyError:
        print(f"Skipping discussion '{response_dict['title']}'")
    else:
        submission_dict['hn_link'] = f"https://news.ycombinator.com/item?id={submission_id}"
        submission_dict['title'] = response_dict['title']
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Extract titles, links and comments.
submission_links, comments_counts = [], []
for submission_dict in submission_dicts:
    # Turn submission titles into links to their discussion page.
    submission_title = submission_dict['title']
    submission_link = f"<a href='{submission_dict['hn_link']}'>{submission_title}</a>"
    submission_links.append(submission_link)
    comments_counts.append(submission_dict['comments'])

# Make visualization.
title = "Most active discussions on Hacker News"
labels = {"x": "Discussion", "y": "Comments"}
fig = px.bar(x=submission_links, y=comments_counts, title=title, 
             labels=labels)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, 
                  yaxis_title_font_size=20)
fig.update_traces(marker_color='IndianRed', marker_opacity=0.6)

fig.show()
