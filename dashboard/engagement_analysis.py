import pandas as pd
import plotly.express as px
import dash.html as html
import dash.dcc as dcc
import os

elbow_method = os.path.abspath("../assets/elbow_method.png")


def display_top_10_engagement_image():
    return html.Div(
        children=[
            html.H4("Top 10 User Engagement to Time"),
            html.Img(
                src="/assets/top-10-user-engaged.png",  # Ensure correct image path
                style={"width": "100%", "height": "auto", "borderRadius": "8px"}
            ),
        ],
        style={
            "backgroundColor": "#f9f9f9",
            "padding": "20px",
            "borderRadius": "8px",
            "border": "1px solid #ddd",
            "marginTop": "20px"
        }
    )


def create_clustered_user_scatter(data, x_col, y_col):
    """Create scatter plot for clustered user data."""
    fig = px.scatter(
        data,
        x=x_col,
        y=y_col,
        color="Cluster",  # Use 'cluster' column for grouping
        title="Clustered User Engagement",
        labels={x_col: "Time Duration (ms)", y_col: "Total UL and DL (bytes)"},
        color_continuous_scale="Viridis"
    )
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(family="Arial", size=14, color="#333"),
        title=dict(font=dict(size=18), x=0.5),
        xaxis=dict(title=x_col),
        yaxis=dict(title=y_col),
        margin=dict(l=40, r=20, t=50, b=80),
    )
    return fig


def display_normalized_metrics_image():
    return html.Div(
        children=[
            html.H4("Normalized Metrics per cluster"),
            html.Img(
                src="/assets/normalized-user.png",  # Correct image path
                style={"width": "100%", "height": "auto", "borderRadius": "8px"}
            ),
        ],
        style={
            "backgroundColor": "#f9f9f9",
            "padding": "20px",
            "borderRadius": "8px",
            "border": "1px solid #ddd",
            "marginTop": "20px"
        }
    )


def display_top_10_most_engaged_user():
    return html.Div(
        children=[
            html.H4("Top 10 most engaged users per application"),
            html.Img(
                src="/assets/top-10-most-engaged.jpg",  # Correct image path
                style={"width": "100%", "height": "auto", "borderRadius": "8px"}
            ),
        ],
        style={
            "backgroundColor": "#f9f9f9",
            "padding": "20px",
            "borderRadius": "8px",
            "border": "1px solid #ddd",
            "marginTop": "20px"
        }
    )


def create_top_3_applications(data):
    """Create bar plot for top 3 most used applications."""
    top_apps = data.nlargest(3, 'Usage')  # Assuming 'Usage' column for ranking
    fig_bar = px.bar(
        top_apps,
        x='Application',
        y='Usage',
        title="Top 3 Most Used Applications",
        labels={"Application": "AppApplication", "Usage": "Usage"},
        color='Usage',
        color_continuous_scale="Blues"
    )
    fig_bar.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(family="Arial", size=14, color="#333"),
        title=dict(font=dict(size=18), x=0.5),
        xaxis=dict(title="Application"),
        yaxis=dict(title="Usage"),
        margin=dict(l=40, r=20, t=50, b=80),
    )

    # Pie chart for clusters
    fig_pie = px.pie(
        data,
        names="Application",  # Assuming the data contains a 'Cluster' column
        values="Usage",   # Column containing the count of instances in each cluster
        title="Cluster Distribution",
    )
    fig_pie.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(family="Arial", size=14, color="#333"),
        title=dict(font=dict(size=18), x=0.5),
        margin=dict(l=40, r=20, t=50, b=80),
    )
    return fig_bar, fig_pie


def display_elbow_method_image():
    return html.Div(
        children=[
            html.H4("The Elbow Method"),
            html.Img(
                src="/assets/elbow-method.png",  # Correct image path
                style={"width": "100%", "height": "auto", "borderRadius": "8px"}
            ),
        ],
        style={
            "backgroundColor": "#f9f9f9",
            "padding": "20px",
            "borderRadius": "8px",
            "border": "1px solid #ddd",
            "marginTop": "20px"
        }
    )


def load_data(file_path):
    """Load data from a CSV file."""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise Exception(f"File not found: {file_path}")
    except pd.errors.EmptyDataError:
        raise Exception(f"File is empty: {file_path}")
    except pd.errors.ParserError:
        raise Exception(f"Error parsing file: {file_path}")


def user_engagement_analysis_layout():
    # Load relevant data (ensure paths are correct for CSVs)
    try:
        clustered_data = load_data("data/clustered-user.csv")  # Example file
        top_apps_data = load_data("data/most-used-top-3-apps.csv")  # Example file
    except Exception as e:
        return html.Div([html.H4(f"Error: {e}")])

    # Create scatter plot for clustered user
    clustered_user_scatter = create_clustered_user_scatter(clustered_data, 'Total UL and DL', "time_duration")

    # Create bar plot for top 3 most used applications
    fig_bar, fig_pie = create_top_3_applications(top_apps_data)

    # Elbow method image
    elbow_method_image = display_elbow_method_image()

    return html.Div(
        children=[
            html.Hr(style={"border": "1px solid #ddd", "marginTop": "40px", "marginBottom": "20px"}),
            html.H3(
                "User Engagement Analysis",
                style={"textAlign": "center", "color": "#003366", "fontWeight": "bold", "marginBottom": "20px"}
            ),
            # Top 10 User Engagement to Time
                        html.Hr(style={"border": "1px solid #ddd", "marginTop": "40px", "marginBottom": "20px"}),

            display_top_10_engagement_image(),
            # Clustered User
                        html.Hr(style={"border": "1px solid #ddd", "marginTop": "40px", "marginBottom": "20px"}),

            dcc.Graph(figure=clustered_user_scatter),
                        html.Hr(style={"border": "1px solid #ddd", "marginTop": "40px", "marginBottom": "20px"}),

            # Normalized Metrics
            display_normalized_metrics_image(),
                        html.Hr(style={"border": "1px solid #ddd", "marginTop": "40px", "marginBottom": "20px"}),

            # Top 10 most engaged user
            display_top_10_most_engaged_user(),
                        html.Hr(style={"border": "1px solid #ddd", "marginTop": "40px", "marginBottom": "20px"}),

            # Top 3 Most Used Applications
            dcc.Graph(figure=fig_bar),
                         html.Hr(style={"border": "1px solid #ddd", "marginTop": "40px", "marginBottom": "20px"}),

            dcc.Graph(figure=fig_pie),
                        html.Hr(style={"border": "1px solid #ddd", "marginTop": "40px", "marginBottom": "20px"}),

            # The Elbow Method
            elbow_method_image,           
        ],
        style={
            "padding": "30px",
            "maxWidth": "900px",
            "margin": "0 auto",
            "backgroundColor": "#fff",
            "borderRadius": "8px",
            "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.1)"
        }
    )
