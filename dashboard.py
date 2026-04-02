# dashboard.py
import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

#Import from excel
df = pd.read_excel("Cybersecurity_Dashboard.xlsx", sheet_name="RawData")

# KPIs calculation
total_sessions = df['SessionID'].count()
avg_duration = df['SessionDuration'].mean()
high_severity = df[df['Severity'] == 'High'].shape[0]
under_attack = df[df['Status'] == 'Under Attack'].shape[0]


severity_counts = df['Severity'].value_counts().reset_index()
severity_counts.columns = ['Severity', 'Count']

severity_chart = px.bar(
    severity_counts,
    x='Severity',
    y='Count',
    title='Severity Levels of Sessions'
)

# Protocol chart
protocol_counts = df['ProtocolType'].value_counts().reset_index()
protocol_counts.columns = ['Protocol', 'Count']

protocol_chart = px.bar(
    protocol_counts,
    x='Protocol',
    y='Count',
    title='Protocol Usage in Network'
    
    
)

status_chart = px.pie(df, names='Status', title='Security Status Distribution')

# Browser chart
browser_counts = df['BrowserType'].value_counts().reset_index()
browser_counts.columns = ['Browser', 'Count']

browser_chart = px.bar(
    browser_counts,
    x='Browser',
    y='Count',
    title='Browser Type Risk Overview'

)

#Dashboard Layout
app = Dash(__name__)

app.layout = html.Div(style={'backgroundColor':'#1e1e1e', 'color':'white', 'padding':'20px'}, children=[

    # Dashboard Title
    html.H1("Cybersecurity Network Dashboard", style={'textAlign':'center'}),

    # KPI Boxes
    html.Div([
        html.Div([
            html.H3("Total Sessions"),
            html.P(f"{total_sessions}", style={'fontSize':'24px', 'color':'#00FF00'})
        ], style={'display':'inline-block','width':'23%','margin':'1%','padding':'10px','backgroundColor':'#333'}),

        html.Div([
            html.H3("Avg Session Duration"),
            html.P(f"{avg_duration:.2f}", style={'fontSize':'24px','color':'#00FF00'})
        ], style={'display':'inline-block','width':'23%','margin':'1%','padding':'10px','backgroundColor':'#333'}),

        html.Div([
            html.H3("High Severity Sessions"),
            html.P(f"{high_severity}", style={'fontSize':'24px','color':'#FF0000'})
        ], style={'display':'inline-block','width':'23%','margin':'1%','padding':'10px','backgroundColor':'#333'}),

        html.Div([
            html.H3("Under Attack Sessions"),
            html.P(f"{under_attack}", style={'fontSize':'24px','color':'#FF0000'})
        ], style={'display':'inline-block','width':'23%','margin':'1%','padding':'10px','backgroundColor':'#333'}),
    ], style={'textAlign':'center'}),

    # Charts
    html.Div([
        dcc.Graph(figure=severity_chart),
        dcc.Graph(figure=protocol_chart),
        dcc.Graph(figure=status_chart),
        dcc.Graph(figure=browser_chart)
    ])
])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8050)))
