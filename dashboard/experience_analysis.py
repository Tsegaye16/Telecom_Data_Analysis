import pandas as pd
import os
import plotly.express as px
import dash.html as html
import dash.dcc as dcc

def display_tcp_value_image():
    return html.Div(
        children=[
            html.H4("TCP values in the dataset"),
            html.Img(
                src="/assets/tcp-value.png",  # Ensure correct image path
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
def display_rtt_value_image():
    return html.Div(
        children=[
            html.H4("RTT values in the dataset"),
            html.Img(
                src="/assets/att-value.png",  # Ensure correct image path
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
def display_throughput_value_image():
    return html.Div(
        children=[
            html.H4("Throughput values in the dataset"),
            html.Img(
                src="/assets/throughput-value.png",  # Ensure correct image path
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

def load_clustered_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading clustered data: {e}")
        return None
def create_data_table(data):
    """Generate an HTML table for the clustered data."""
    return html.Table(
        # Table headers
        [html.Tr([html.Th(col) for col in data.columns])] +
        # Table rows
        [html.Tr([html.Td(data.iloc[i][col]) for col in data.columns]) for i in range(len(data))],
        style={
            "border": "1px solid #ddd",
            "borderCollapse": "collapse",
            "width": "100%",
            "margin": "20px 0",
        }
    )
def create_experience_scatter(data, x_col, y_col, z_col, cluster_col="Cluster"):
    """Create 3D scatter plot for user experience clustering."""
    fig = px.scatter_3d(
        data,
        x=x_col,
        y=y_col,
        z=z_col,  # Use Total_Avg_TCP for the z-axis
        color=cluster_col,
        title="User Experience Clustering (3D)",
        labels={x_col: x_col, y_col: y_col, z_col: z_col},
        hover_data=["MSISDN/Number", "Handset Type"],
        color_discrete_sequence=px.colors.qualitative.Plotly
    )
    fig.update_layout(
        scene=dict(
            xaxis=dict(title=x_col),
            yaxis=dict(title=y_col),
            zaxis=dict(title=z_col),
        ),
        margin=dict(l=40, r=20, t=50, b=80),
        font=dict(family="Arial", size=14, color="#333"),
        title=dict(font=dict(size=18), x=0.5),
        width=1000,  # Set width
        height=600,  # Set height
    )
    return fig

def display_cluster_analysis(data):
    # Create scatter plot
    scatter_fig = create_experience_scatter(data, "Total_Avg_RTT", "Total_Avg_Bearer_TP", "Total_Avg_TCP")

    # Dash Layout
    return html.Div(
        children=[
            html.Hr(style={"border": "1px solid #ddd", "marginTop": "40px", "marginBottom": "20px"}),

            # Data Table
            # html.Div([
            #     html.H4("Clustered Data"),
            #     create_data_table(data),
            # ]),

            # Clustered Scatter Plot
          html.Div([
    html.H4("Clustered User Experience"),
    dcc.Graph(figure=scatter_fig,style={"width": "100%", "height": "700px"}),
]),

        ],
        style={
            "padding": "30px",
            "maxWidth": "1200px",
            "margin": "0 auto",
            "backgroundColor": "#fff",
            "borderRadius": "8px",
            "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.1)"
        }
    )

def user_experience_analysis_layout():
    """Layout for User Experience Analysis Dashboard."""
    # Load the clustered data (replace 'path/to/your/clustered_data.csv' with your actual file path)
    data = load_clustered_data("data/experience-clustered.csv")
    
    if data is None:
        return html.Div(
            children=[
                html.H4("Error: Unable to load data."),
                html.P("Please check the file path or the format of your dataset."),
            ],
            style={
                "padding": "30px",
                "maxWidth": "600px",
                "margin": "50px auto",
                "textAlign": "center",
                "backgroundColor": "#fff",
                "borderRadius": "8px",
                "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.1)",
            }
        )

    # Define the layout
    return html.Div(
        children=[
            # Page Header
            html.H1(
                "User Experience Analysis Dashboard",
                style={"textAlign": "center", "marginBottom": "30px"}
            ),

            # TCP Value Image
            display_tcp_value_image(),

            # RTT Value Image
            display_rtt_value_image(),

            # Throughput Value Image
            display_throughput_value_image(),

            # Cluster Analysis
            display_cluster_analysis(data),
        ],
        # style={
        #     "padding": "30px",
        #     "backgroundColor": "#f4f4f9",
        # }
        style={
            "padding": "30px",
            "maxWidth": "900px",
            "margin": "0 auto",
            "backgroundColor": "#fff",
            "borderRadius": "8px",
            "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.1)"
        }
    )
