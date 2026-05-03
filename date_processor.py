import pandas as pd
import schemas as schemas

def process_data(raw_events):
    # 1. 將傳入的資料轉為 DataFrame
    df = pd.DataFrame(raw_events)
    
    # 2. 你的欄位重新命名邏輯
    df = df.rename(columns={
        'image': 'image_id',
        'type': 'violation_type',
        'time': 'timestamp',
    })
    
    # 3. 你的時間處理邏輯
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["date"] = df["timestamp"].dt.date
    df['hour'] = df['timestamp'].dt.hour
    df['weekday'] = df['timestamp'].dt.day_name()
    # 5. 設定中文顯示 (這寫在裡面會確保每次執行都生效)
    pd.set_option('display.unicode.ambiguous_as_wide', True)
    pd.set_option('display.unicode.east_asian_width', True)
    # 6. 【最重要】把整理好的結果丟回去給 main.py
    
    return df
