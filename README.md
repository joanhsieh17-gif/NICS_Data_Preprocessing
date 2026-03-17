# TFC 台灣事實查核中心 - 資料前處理工具 使用說明
`English Version Below`

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
├── data/                         # 存放原始json資料
├── output/                       # 處理後的csv/json存放位置
├── data_preprocessing.py         # 主要處理程式
├── requirements.txt              # 依賴套件清單
├── .gitignore
└── README.md
```

## 安裝

### 1.切換至您的目標路徑
```bash
cd 資料夾存放路徑
```

```bash
# 複製本資料夾
git clone https://github.com/joanhsieh17-gif/NICS_Data_Preprocessing.git
```

```bash
# 進入本專案資料夾
cd NICS_Data_Preprocessing
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
若虛擬環境取不同名稱，請自行加入.gitignore
例如：
```bash
venv/ --> change_name/
```

### 3. 安裝套件
```bash
pip install -r requirements.txt
```

## 執行
### 執行前處理程式，並依照提示輸入須處理的json檔，以及輸出檔案的位置
```bash
python data_preprocessing.py --input ./data/your_file.json --output ./output/
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

# TFC Taiwan FactCheck Center - Data Preprocessing Tool

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

This project is specifically designed to process raw JSON datasets from the **Taiwan FactCheck Center (TFC)**.

`data_preprocessing.py` performs the following operations:
- **HTML Tag Cleaning**: Removes tags such as `<p>`, `<div>`, and `<span>`.
- **Text Normalization**: Compresses redundant spaces and newlines to prevent formatting issues in CSV output.
- **Date Formatting**: Standardizes dates to `YYYY-MM-DD`.
- **Complex Structure Parsing**: Extracts plain text from the nested `orig_rumor` field.
- **Standardized Output**: Generates clean CSV and JSON files for further analysis.

## Project Structure

```text
NICS_Data_Preprocessing/
├── data/                 # Location for raw input JSON files
├── output/               # Location for processed CSV/JSON files
├── data_preprocessing.py # Main preprocessing script
├── requirements.txt      # List of Python dependencies
├── .gitignore            # Files to be ignored by Git
└── README.md             # Project documentation
```

## Installation

### 1.Navigate to Your Target Directory
```bash
# Navigate to your preferred folder
cd /path/to/your/directory

# Clone the repository
git clone [https://github.com/joanhsieh17-gif/NICS_Data_Preprocessing.git](https://github.com/joanhsieh17-gif/NICS_Data_Preprocessing.git)

# Enter the project directory
cd NICS_Data_Preprocessing
```

### 2.Set Up Virtual Environment
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
Note: If you name your virtual environment something other than venv/, please remember to update your .gitignore accordingly (e.g., replace venv/ with your_custom_name/).

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Run the preprocessing script by specifying the input JSON file and output directory.
```bash
python data_preprocessing.py --input ./data/your_file.json --output ./output/
```
Example
```bash
python data_preprocessing.py --input ./data/all_raw.json --output ./output/
```

## Output Results
After the script completes, the following two files will be generated in your output folder:

(1) tfc_processed.csv

(2) tfc_processed.json

## Field Mapping Table

| Output Field | Original Data Source (JSON) | Description |
| :--- | :--- | :--- |
| **Original Rumor** | `node > orig_rumor` | Cleaned plain text of the rumor |
| **Verification Date** | `node > updated_time` | Date format: `YYYY-MM-DD` |
| **Category** | `node > article_category` | Subject category (e.g., Health, Lifestyle) |
| **Organization** | Fixed Value | Labeled as `TFC` |
| **Report Title** | `node > title` | Official title of the fact-check report |
| **Report Link** | `node > node_url` | Direct URL to the official report |
| **Classification Tag** | `node > taxo_report_attr` | Verification result (e.g., False) |
