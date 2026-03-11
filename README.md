# TFC 台灣事實查核中心 - 資料前處理工具 使用說明

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

本專案專為處理台灣事實查核中心 (TFC) 的原始 JSON 資料集而設計。
data_preprocessing.py 執行以下動作：
- **清理 HTML 標籤**: 如 `<p>`, `<div>`, `<span>`。
- **正規化文字**: 壓縮多餘空格、換行，避免 CSV 格式跑版。
- **格式化日期**: 僅保留 YYYY-MM-DD。
- **解析複雜的原始謠言結構**: 從 orig_rumor 欄位提取純文字。
- **輸出標準化的 CSV 與 JSON 檔案**

## 專案架構

```text
NICS_Data_Preprocessing/
├── data/                         # input data (.json)
├── data_preprocessing.py         # 資料前處理 script
├── requirements.txt              # Python 安裝套件
├── .gitignore.txt
└── README.md
```

## 安裝

### 1.切換至您的目標路徑
```bash
cd 資料夾存放路徑
git clone https://github.com/joanhsieh17-gif/NICS_Data_Preprocessing.git
```

### 2. 建立虛擬環境
`macOS/Linux`
```bash
python3 -m venv venv
source venv/bin/activate
```

`Windows`
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. 安裝套件
```bash
pip install -r requirements.txt
```

## 執行
### 1. 執行前處理程式
```bash
python data_preprocessing.py
````
### 2. 依照提示輸入處理的json檔，以及輸出檔案的位置
```bash
python data_preprocessing.py --input ./data/your_file.json --output your_output_file
```

例如：python data_preprocessing.py --input ./data/all_raw.json --output ./output/

## 輸出結果
程式執行完成後，會產出以下兩個檔案：

(1) tfc_processed.csv

(2) tfc_processed.json

## 欄位對應表
| 輸出欄位 | 原始資料來源 (JSON) | 說明 |
| :--- | :--- | :--- |
| **原始謠言** | `node > orig_rumor` | 清理後的謠言純文字 |
| **查核日期** | `node > updated_time` | 僅保留日期 `YYYY-MM-DD` |
| **分類** | `node > article_category` | 主題分類 (如: 健康、生活) |
| **查核單位** | 固定值 | 標註為 `TFC` |
| **查核報告標題** | `node > title` | 報告正式大標題 |
| **查核報告連結** | `node > node_url` | 官方原始網址 |
| **分類標籤** | `node > taxo_report_attr` | 查核結果 (如: 錯誤) |
