# Step 1: import plotly library and chart objects
# Step 2: feed data
# Step 3: decorate layout

import plotly
from plotly.graph_objs import Bar, Pie, Scatter, Layout

# Bar Chart
bar_chart = plotly.offline.plot({
    "data": [Bar(x=["Leatherby", "Law", "Science", "Music", "Brandman"], y=[543, 365, 92, 61, 77])],
    "layout": Layout(title="Checkouts by Libraries")
}, output_type='div')


# Pie Chart
pie_chart = plotly.offline.plot({
    "data": [Pie(labels=["Leatherby", "Law", "Science", "Music", "Brandman"], values=[543, 365, 92, 61, 77])],
    "layout": Layout(title="Checkouts by Libraries")
}, output_type='div')

# print(bar_chart)


#################################################
#########  Embed div charts inside a html  ###### 
#################################################
from createHTML import create_html

context = {
    'bar_chart': bar_chart,
    'pie_chart': pie_chart,
}

# pass Plotly charts 'div' outputs to the template engine
create_html('embed_template.html', 'embed.html', context)