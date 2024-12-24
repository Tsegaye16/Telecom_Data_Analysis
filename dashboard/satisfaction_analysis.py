import dash.dcc as dcc
import dash.html as html
def user_satisfaction_analysis():
    return html.Div(
        children=[
            html.H1('User Satisfaction Analysis',style={"textAlign": "center", "color": "#003366", "fontWeight": "bold", "marginBottom": "20px"}),
            html.H3(
                        "Coming soon.........",
                        style={"lineHeight": "1.6", "fontSize": "30px", "color": "#666"}
                    ),
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