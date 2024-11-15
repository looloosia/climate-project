import pandas as pd

def load_and_process_co2_data(file_path):
    # CO2 데이터 불러오기
    df_co2 = pd.read_csv(file_path)
    df_co2.columns = df_co2.columns.str.strip().str.lower()  # 열 이름 표준화
    
    # 비정상적인 값 필터링 (-999.99를 NaN으로 바꾸고 제거)
    df_co2['average'] = pd.to_numeric(df_co2['average'], errors='coerce')
    df_co2 = df_co2[df_co2['average'] != -999.99]
    df_co2 = df_co2.dropna(subset=['average', 'year', 'month', 'day'])
    
    # 날짜 생성
    df_co2['date'] = pd.to_datetime(df_co2[['year', 'month', 'day']], errors='coerce')
    df_co2 = df_co2.dropna(subset=['date'])

    # 데이터 정렬
    df_co2 = df_co2.sort_values(by='date')
    
    return df_co2

def load_and_process_ch4_data(file_path):
    # CH4 데이터 불러오기
    df_ch4 = pd.read_csv(file_path)
    df_ch4.columns = df_ch4.columns.str.strip().str.lower()

    # 비정상적인 값 필터링 (-999.99를 NaN으로 바꾸고 제거)
    df_ch4['average'] = pd.to_numeric(df_ch4['average'], errors='coerce')
    df_ch4 = df_ch4[df_ch4['average'] != -999.99]
    df_ch4 = df_ch4.dropna(subset=['average', 'year', 'month'])

    # 날짜 생성
    df_ch4['date'] = pd.to_datetime(df_ch4[['year', 'month']].assign(day=1), errors='coerce')
    df_ch4 = df_ch4.dropna(subset=['date'])

    # 데이터 정렬
    df_ch4 = df_ch4.sort_values(by='date')
    
    return df_ch4
