import pandas as pd
import plotly.express as px
import dash.html as html
import dash.dcc as dcc

def load_data(file_path):
    """Load data from a CSV file."""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise Exception(f"File not found: {file_path}")

def create_correlation_heatmap(data):
    """Create a heatmap for correlation matrix of the data."""
    correlation_matrix = data.corr()
    fig = px.imshow(
        correlation_matrix,
        color_continuous_scale="RdBu_r",
        title="Correlation Matrix",
        labels={"x": "Features", "y": "Features"},
        color_continuous_midpoint=0
    )
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(family="Arial", size=14, color="#333"),
        title=dict(font=dict(size=18), x=0.5),  # Center the title
        xaxis=dict(showgrid=False, tickangle=45),
        yaxis=dict(showgrid=False),
        margin=dict(l=40, r=20, t=50, b=80),
    )
    return fig
def create_plots(data, title, x_col, y_col):
    """Create bar plot for handset data."""
    fig = px.bar(
        data,
        x=x_col,
        y=y_col,
        labels={x_col: "Manufacturer", y_col: "Count"},
        title=title,
        color=y_col,
        color_continuous_scale="Blues"
    )
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(family="Arial", size=14, color="#333"),
        title=dict(font=dict(size=18), x=0.5),  # Center the title
        xaxis=dict(title=x_col, showgrid=False, tickangle=45),
        yaxis=dict(title="Count", showgrid=True),
        margin=dict(l=40, r=20, t=50, b=80),
    )
    return fig

def layout():
    """Generate the layout for Overview Analysis."""
    # Load datasets
    original_data = load_data("data/top-10-handsets.csv")
    cleaned_data = load_data("data/top-10-handset-cleaned.csv")
    manufacturer_data = load_data("data/top-3-hndset-manuf.csv")
    top_5_apple_data = load_data("data/top-5-apple-handset.csv")
    top_5_huawei_data = load_data("data/top-5-huawei-handset.csv")
    top_5_samsung_data = load_data("data/top-5-Samsung-handset.csv")
    total_data_per_decile = load_data("data/total-data-per-decile.csv")
    correlation_data = load_data("data/data-correlation.csv")
    

    # Create plots
    fig_top_handsets_original = create_plots(
        original_data, "Top 10 Handsets Used by Customers", "Handset Type", "count"
    )
    fig_top_handsets_cleaned = create_plots(
        cleaned_data, "Top 10 Handsets Used by Customers", "Handset Type", "count"
    )
    fig_top_manufacturers = create_plots(
        manufacturer_data, "Top 3 Handset Manufacturers", "Handset Manufacturer", "count"
    )
    fig_top_5_apple = create_plots(
        top_5_apple_data, "Top 5 Apple Handsets", "Handset Type","count"
    )
    fig_top_5_samsung = create_plots(
        top_5_samsung_data, "Top 5 Samsung Handsets", "Handset Type","count" 
    )
    fig_top_5_huawei = create_plots(
        top_5_huawei_data, "Top 5 Huawei Handsets", "Handset Type","count"
    )

    fig_explore_feature = px.line(
    total_data_per_decile, 
    x="Decile", 
    y="Total UL and DL",  # First y variable
    title="Top 5 Deciled Customers by Duration in sec",
    markers=True,
    line_shape='linear',
     labels={"Total_UL_and_DL": "Total UL and DL"}

)

# Add a second line for 'Duration' by using `add_scatter`
    fig_explore_feature.add_scatter(
    x=total_data_per_decile["Decile"], 
    y=total_data_per_decile["Duration"], 
    mode="lines+markers", 
    name="Duration"
)

    fig_explore_feature.update_layout(
    xaxis_title="Decile",
    yaxis_title="Value",
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(family="Arial", size=14, color="#333"),
    title=dict(font=dict(size=18), x=0.5),  # Center the title
     xaxis=dict(
        showgrid=True,
        tickangle=45,
        zeroline=True,  # Ensures the x-axis line is visible
        showline=True,  # Ensures the x-axis line is visible
        linecolor='black',  # Axis line color
        linewidth=2  # Axis line thickness
    ),
    yaxis=dict(
        showgrid=True,
        zeroline=True,  # Ensures the y-axis line is visible
        showline=True,  # Ensures the y-axis line is visible
        linecolor='black',  # Axis line color
        linewidth=2  # Axis line thickness
    ),
    legend = dict(
        title="Legend",
        tracegroupgap=5,
        font=dict(size=12)
    ),
    margin=dict(l=40, r=20, t=50, b=80)
)


    # Interpretation for cleaned data
    interpretation_cleaned = html.Div(
        children=[
            html.H4(
                "Interpretation",
                style={"color": "#003366", "fontWeight": "bold", "marginBottom": "10px"}
            ),
            html.P(
                "After removing 'undefined' entries, we observe a more accurate representation of handset usage. "
                "The top 10 handsets reflect cleaner data with improved insights into customer preferences.",
                style={"lineHeight": "1.6", "fontSize": "16px", "color": "#666"}
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

    # Interpretation for top manufacturers
    interpretation_manufacturers = html.Div(
        children=[
            html.H4(
                "Interpretation of Top 3 Manufacturers:",
                style={"color": "#003366", "fontWeight": "bold", "marginBottom": "10px"}
            ),
            html.P(
                "The top 3 handset manufacturers are Apple, Samsung, and Huawei. Apple leads the market with "
                "59,339 devices, followed by Samsung with 40,429 devices, and Huawei with 34,296 devices. "
                "This indicates a competitive landscape dominated by these manufacturers.",
                style={"lineHeight": "1.6", "fontSize": "16px", "color": "#666"}
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
    interpretation_top_3_manufacturers = html.Div(
    children=[
        html.H4(
            "Main insights!🍀",
            style={"color": "#003366", "fontWeight": "bold"}
        ),
        html.P(
            "The most used handset model by customers is Huawei B528S-23A which is manufactured by Huawei",
            style={"lineHeight": "1.6", "fontSize": "16px", "color": "#666"}
        ),
        html.Br(),
        html.P(
            "🫥 The top 3 handset manufacturers are:",
            style={"lineHeight": "1.6", "fontSize": "16px", "color": "#666"}
        ),
        html.Br(),
        html.P(
            "First, Apple with a total of 59,339 units;",
            style={"lineHeight": "1.6", "fontSize": "16px", "color": "#666"}
        ),
        html.Br(),
        html.P(
            "Second, Samsung with a total of 40,429 units;",
            style={"lineHeight": "1.6", "fontSize": "16px", "color": "#666"}
        ),
        html.Br(),
        html.P(
            "And third, Huawei with a total of 34,296 units.",
            style={"lineHeight": "1.6", "fontSize": "16px", "color": "#666"}
        ),
        html.Br(),
        html.P(
            "🫥 Apple's handsets are not preferred by as many customers, and Samsung's are in a similar position to Apple's.",
            style={"lineHeight": "1.6", "fontSize": "16px", "color": "#666"}
        ),
        html.Br(),
        html.P(
            "🫥 Huawei handsets are more widely used, and their manufacturers can be recommended to increase manufacturing capacity to expand their customer reach.",
            style={"lineHeight": "1.6", "fontSize": "16px", "color": "#666"}
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
    correlation_interpretation =  html.Div(
        children=[
            html.H4(
                "Main Insights",
                style={"color": "#003366", "fontWeight": "bold", "marginBottom": "10px"}
            ),
            html.P(
                "Dominance of Gaming: The perfect correlation between Gaming_Total_Data and Total UL and DL suggests that gaming data usage dominates or overlaps with the total data metric. This could indicate gaming as the primary driver of overall network usage or a potential data logging issue.",
                style={"lineHeight": "1.6", "fontSize": "16px", "color": "#666"}
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

  

    top_3_manufacturer_title = html.Div(
    children=[
        html.H2("Top 3 Handset Manufacturers"),
    ],
    

    )
    # Create Correlation Heatmap
    correlations_data = correlation_data.select_dtypes(include=["float64", "int64"])  # Select numeric columns
    fig_correlation = create_correlation_heatmap(correlations_data)
    return html.Div(
        
        children=[
            html.Hr(style={"border": "1px solid #ddd", "marginTop": "40px", "marginBottom": "20px"}),
            html.H3(
                "Overview Analysis",
                style={"textAlign": "center", "color": "#003366", "fontWeight": "bold", "marginBottom": "20px"}
            ),
            # Original Data
            html.Hr(style={"border": "1px solid #ddd", "marginTop": "40px", "marginBottom": "20px"}),
            dcc.Graph(figure=fig_top_handsets_original),
            html.Div(
                children=[
                    html.H4("Interpretation:"),
                    html.P(
                        "The graph above includes rows with 'undefined' values, contributing to 6.00% of the dataset. "
                        "While these entries have minimal impact, cleaning the data improves its accuracy.",
                        style={"lineHeight": "1.6", "fontSize": "16px", "color": "#666"}
                    ),
                ],
                style={
                    "backgroundColor": "#f9f9f9",
                    "padding": "20px",
                    "borderRadius": "8px",
                    "border": "1px solid #ddd",
                    "marginTop": "20px"
                }
            ),
            # Cleaned Data
            
            dcc.Graph(figure=fig_top_handsets_cleaned),
            interpretation_cleaned,
            # Top Manufacturers
            html.Hr(style={"border": "1px solid #ddd", "marginTop": "40px", "marginBottom": "20px"}),
            dcc.Graph(figure=fig_top_manufacturers),
            interpretation_manufacturers,
            html.Hr(style={"border": "1px solid #ddd", "marginTop": "40px", "marginBottom": "20px"}),
            top_3_manufacturer_title,
            dcc.Graph(figure=fig_top_5_apple),
            dcc.Graph(figure=fig_top_5_samsung),
            dcc.Graph(figure=fig_top_5_huawei),
            interpretation_top_3_manufacturers,
            html.Hr(style={"border": "1px solid #ddd", "marginTop": "40px", "marginBottom": "20px"}),
            dcc.Graph(figure=fig_explore_feature),
            html.Hr(style={"border": "1px solid #ddd", "marginTop": "40px", "marginBottom": "20px"}),
            dcc.Graph(figure=fig_correlation,style={"height": "600px", "width": "100%"}),
            correlation_interpretation

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
