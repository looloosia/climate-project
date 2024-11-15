from flask import Flask, render_template
from update_data import load_and_process_co2_data, load_and_process_ch4_data

app = Flask(__name__)

# 데이터 파일 경로 지정
CO2_DATA_FILE_PATH = 'co2_data_file.csv'
CH4_DATA_FILE_PATH = 'ch4_data_file.csv'

@app.route('/')
def home():
    # 데이터 로드 및 처리
    df_co2 = load_and_process_co2_data(CO2_DATA_FILE_PATH)
    df_ch4 = load_and_process_ch4_data(CH4_DATA_FILE_PATH)

    # 날짜 및 평균 농도 데이터 전달
    co2_dates = df_co2['date'].dt.strftime('%Y-%m-%d').tolist()
    co2_averages = df_co2['average'].tolist()

    ch4_dates = df_ch4['date'].dt.strftime('%Y-%m-%d').tolist()
    ch4_averages = df_ch4['average'].tolist()

    return render_template(
        'index.html',
        co2_dates=co2_dates,
        co2_averages=co2_averages,
        ch4_dates=ch4_dates,
        ch4_averages=ch4_averages
    )

if __name__ == '__main__':
    app.run(debug=True)
