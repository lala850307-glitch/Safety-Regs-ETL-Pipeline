import os
from datetime import datetime
import pandas as pd

def generate_report(list_test_report):
    # 1. 將資料轉回 DataFrame 方便統計
    df = pd.DataFrame(list_test_report)
    
    # 2. 設定路徑
    base_dir = os.path.dirname(os.path.abspath(__file__))
    folder = os.path.join(base_dir, "report")
    time_str = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    file_name = f"{folder}/report-{time_str}.csv"
    full_path = file_name
    # 3. 儲存 CSV 檔案 (保持原有的功能)
    df.to_csv(full_path, index=False, encoding="utf-8-sig")
    # --- 4. 生成你想要的精美文字報表內容 ---
    total_count = len(df)
    # 統計違規類型
    type_counts = df['violation_type'].value_counts()
    # 統計時段 (使用你洗好的 hour_range)
    temp_display_hour = df['hour'].apply(lambda x: f"{int(x):02d}時-{int(x)+1:02d}")
    hour_counts = temp_display_hour.value_counts().sort_index()
    # 統計工地
    location_counts = df['location'].value_counts()
    # 組合字串
    report_text = []
    report_text.append("="*50)
    report_text.append("工安違規統計報表")
    report_text.append(f"報表產生時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_text.append("="*50)
    report_text.append(f"違規事件總數: {total_count} 件\n")
    report_text.append("違規類型統計:")
    report_text.append("-" * 30)
    for v_type, count in type_counts.items():
        percentage = (count / total_count) * 100
        report_text.append(f"  {v_type}: {count} 件 ({percentage:.1f}%)")
    
    report_text.append("時段分析:")
    report_text.append("-" * 30)
    for hour, count in hour_counts.items():
        report_text.append(f"  {hour}: {count} 件")
        
    report_text.append("工地統計:")
    report_text.append("-" * 30)
    for loc, count in location_counts.items():
        report_text.append(f"  {loc}: {count} 件")
        
    report_text.append("=" * 50)

    # 將所有文字串接起來
    final_report = "\n".join(report_text)
    
    # 將文字報表也存成一個 txt 檔
    with open(os.path.join(folder, f"report_{time_str}.txt"), "w", encoding="utf-8") as f:
        f.write(final_report)

    # 傳回給 main.py 印出來
    return final_report