import json
import pandas as pd
from bs4 import BeautifulSoup
import re
import os
import argparse


# 工具函式 (Data Cleaning Tools)==================================================
def normalize_text(text):
    """清理 HTML 並將多餘的空白、換行正規化"""
    if not text:
        return ""
    # 1. 去除 HTML 標籤
    clean_str = BeautifulSoup(str(text), "html.parser").get_text(separator=" ", strip=True)
    # 2. 正規化：將多個連續的空白、換行或 tab 替換成單一個空白
    clean_str = re.sub(r'\s+', ' ', clean_str)
    # 3. 去除首尾空白
    return clean_str.strip()

def normalize_list(data):
    """將 List 型態的標籤或分類轉換為逗號分隔的字串"""
    if not data:
        return ""
    if isinstance(data, list):
        # 過濾掉空值並轉為字串
        return ", ".join([str(i) for i in data if i])
    return str(data)

def extract_rumor(raw_rumor):
    """處理 orig_rumor 複雜的資料結構並提取文字"""
    if not raw_rumor:
        return ""
    
    if isinstance(raw_rumor, str):
        return raw_rumor
        
    if isinstance(raw_rumor, list):
        rumor_parts = []
        for item in raw_rumor:
            if isinstance(item, dict):
                text = item.get('field_orig_body', '')
                if text:
                    rumor_parts.append(text)
            elif isinstance(item, str):
                rumor_parts.append(item)
        return " ".join(rumor_parts)
    return ""

# 核心處理邏輯 (Core Logic)========================================================
def process_tfc_data(input_file, output_dir):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"錯誤：找不到檔案 {input_file}")
        return

    processed_list = []
    for entry in data:
        node = entry.get('node', {})
        
        # 提取並解析原始謠言
        raw_rumor_data = node.get('orig_rumor', [])
        extracted_rumor_text = extract_rumor(raw_rumor_data)
        
        # 處理日期正規化 (只取 YYYY-MM-DD)
        raw_date = node.get('updated_time', "")
        norm_date = raw_date.split(" ")[0] if raw_date else ""

        # 組合需要的欄位 (根據你的正確對應)
        item = {
            "原始謠言": normalize_text(extracted_rumor_text),
            "查核日期": norm_date,
            "分類": normalize_list(node.get('article_category', "")),      # 對應 article_category
            "查核單位": "TFC",
            "查核報告標題": normalize_text(node.get('title', "")),
            "查核報告連結": node.get('node_url', ""),
            "分類標籤": normalize_list(node.get('taxo_report_attr', "")) # 對應 taxo_report_attr
        }
        processed_list.append(item)

    # 輸出
    df = pd.DataFrame(processed_list)
    csv_path = os.path.join(output_dir, "tfc_processed.csv")
    json_path = os.path.join(output_dir, "tfc_processed.json")
    
    df.to_csv(csv_path, index=False, encoding='utf-8-sig')
    df.to_json(json_path, orient='records', force_ascii=False, indent=4)
    print(f"成功處理 {len(processed_list)} 筆資料！")
    print(f"檔案已儲存至: {csv_path} 與 {json_path}")

def main():
    # 1. 建立 ArgumentParser 物件
    parser = argparse.ArgumentParser(description="TFC 資料前處理工具")

    # 2. 加入參數設定
    parser.add_argument('--input', type=str, required=True, help='原始 JSON 檔案路徑')
    parser.add_argument('--output', type=str, default='./output', help='輸出檔案所在的目錄路徑')

    # 3. 解析參數
    args = parser.parse_args()

    # 確保輸出目錄存在
    if not os.path.exists(args.output):
        os.makedirs(args.output)

    # 傳遞參數給處理函式
    process_tfc_data(args.input, args.output)

# 主程式入口 (Main Entry Point)====================================================
if __name__ == "__main__":
    main()