import requests
import plotly.express as px

# Make an API call & check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_links, comments_counts = [], []
for submission_id in submission_ids[:30]:
    # Make a new api call for each submission:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}, status code: {r.status_code}")
    response_dict = r.json()

    # Turn submission titles into links to their discussion page.
    try: 
        submission_title = response_dict['title']
        submission_link = f"<a href='https://news.ycombinator.com/item?id={submission_id}'>{submission_title}</a>"
        submission_links.append(submission_link)
        comments_counts.append(response_dict['descendants'])
    except KeyError: 
        continue # Skip submissions without comments.

# Make visualization.
title = "Most active discussions on Hacker News"
labels = {"x": "Discussion", "y": "Comments"}
fig = px.bar(x=submission_links, y=comments_counts, title=title, 
             labels=labels)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, 
                  yaxis_title_font_size=20)
fig.update_traces(marker_color='IndianRed', marker_opacity=0.6)

fig.show()
