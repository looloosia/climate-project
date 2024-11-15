import dash
from dash import dcc, html
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children='기후 변화 대시보드', style={'textAlign': 'center'}),
        
        html.Div(children='CO2 및 CH4 농도에 대한 최신 정보를 제공합니다.', style={'textAlign': 'center'}),

        html.Div(
            children=[
                html.H2('주간 평균 CO2 농도', style={'textAlign': 'center'}),
                html.Img(src='/static/co2_concentration_plot.png', style={'width': '80%', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
                html.P("이 그래프는 주간 평균 CO2 농도의 변화를 보여줍니다. CO2 농도가 400 ppm을 넘어서면 주의 수준에 도달하며, 420 ppm을 초과하면 심각한 기후 위험 수준으로 간주됩니다. 이러한 농도 증가는 지구 온난화 및 다양한 기후 변화의 주요 요인입니다.", style={'textAlign': 'center'}),
                
                html.H2('월간 평균 CH4 농도', style={'textAlign': 'center'}),
                html.Img(src='/static/ch4_concentration_plot.png', style={'width': '80%', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
                html.P("이 그래프는 월간 평균 CH4 농도의 변화를 보여줍니다. 메탄(CH4)은 CO2보다 강력한 온실가스로, 대기 중 농도 증가는 기후 변화에 중요한 역할을 합니다.", style={'textAlign': 'center'}),
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
