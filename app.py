import dash
import dash.dcc as dcc
import dash.html as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from dashboard.overview_analysis import layout as overview_layout
from dashboard.engagement_analysis import user_engagement_analysis_layout as engagement_layout
from dashboard.experience_analysis import user_experience_analysis_layout as experience_layout
from dashboard.satisfaction_analysis import user_satisfaction_analysis as satisfaction_layout



# Create a sample DataFrame
data = pd.DataFrame({
    'User_ID': [1, 2, 3, 4, 5],
    'Engagement_Score': [500, 600, 450, 700, 300],
    'Experience_Score': [450, 600, 400, 750, 350],
    'Satisfaction_Score': [475, 600, 425, 725, 325],
    'Sessions': [3, 4, 2, 5, 1],
    'Time_Duration': [120, 180, 90, 240, 60]
})

# Create a Dash app
app = dash.Dash(__name__)

# Define the layout with different pages
app.layout = html.Div([
    dcc.Tabs(id="tabs", value='user-overview', children=[
        dcc.Tab(label='User Overview Analysis', value='user-overview'),
        dcc.Tab(label='User Engagement Analysis', value='user-engagement'),
        dcc.Tab(label='Experience Analysis', value='user-experience'),
        dcc.Tab(label='Satisfaction Analysis', value='user-satisfaction'),
    ]),
    html.Div(id='tabs-content')
])

# Callback to update content based on tab selected
@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'user-overview':
        return overview_layout()
    elif tab == 'user-engagement':
      
        return engagement_layout()
    elif tab == 'user-experience':
        
        return experience_layout()
    elif tab == 'user-satisfaction':
        return satisfaction_layout()

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

###/////////////////////////////////////////////////

# import dash
# import dash.html as html
# import dash.dcc as dcc
# from dash.dependencies import Input, Output

# # Import the layout from overview_analysis
# from dashboard.overview_analysis import layout as overview_layout

# # Create the Dash app
# app = dash.Dash(__name__)

# # App layout
# app.layout = html.Div([
#     dcc.Tabs(id="tabs", value='overview', children=[
#         dcc.Tab(label='Overview Analysis', value='overview'),
#     ]),
#     html.Div(id='tabs-content')
# ])

# # Callback to update the layout based on selected tab
# @app.callback(Output('tabs-content', 'children'),
#               Input('tabs', 'value'))
# def render_content(tab):
#     if tab == 'overview':
#         return overview_layout()
#     return html.Div("No content available")

# # Run the app
# if __name__ == "__main__":
#     app.run_server(debug=True)

