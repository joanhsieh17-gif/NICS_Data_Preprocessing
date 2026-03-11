===========================================================
       # TFC 台灣事實查核中心 - 資料前處理工具 使用說明
===========================================================

## 1. 程式簡介
-----------
本工具 (data_preprocessing.py) 專為處理台灣事實查核中心 (TFC) 的原始 JSON 
資料集而設計。它會自動執行以下動作：
- **清理 HTML 標籤**: 如 <p>, <div>, <span>。
- **正規化文字**: 壓縮多餘空格、換行，避免 CSV 格式跑版。
- **格式化日期**: 僅保留 YYYY-MM-DD。
- **解析複雜的原始謠言結構**: 從 orig_rumor 欄位提取純文字。
- **輸出標準化的 CSV 與 JSON 檔案**

2. 環境需求
-----------
執行前請確保您的電腦已安裝 Python，並安裝以下必要套件：

```bash
   pip install pandas beautifulsoup4
```

3. 資料夾準備
-------------
請確保以下檔案放在「同一個資料夾」內：
- data_preprocessing.py **資料前處理的程式碼**
- all_raw.json **請改成您要處理的檔案**

4. 執行步驟
-----------
1. 開啟 CMD (命令提示字元) 或 Terminal。
2. 切換至您要放置該資料夾的位置：
```bash
   cd /d "C:\您的路徑\NICS"
```
3. 從github上複製到本地
```bash
   git clone https://github.com/joanhsieh17-gif/NICS-Data-Preprocessing.git
```
4. 執行程式：
```bash
   python data_preprocessing.py
````
5. 依照提示：
   - 輸入檔名：例如輸入「all_raw.json」後按 Enter。
   - 直接按 Enter：程式會預設抓取「all_raw.json」。

5. 輸出結果說明
---------------
程式執行完成後，會產出以下兩個檔案：

(1) tfc_processed.csv：
    - 編碼：utf-8-sig (Excel 直接開啟不亂碼)。
    - 用途：方便人工檢視、統計、標註資料。

(2) tfc_processed.json：
    - 格式：Records (List of Dictionaries)。
    - 特點：已排除 Unicode 編碼，可直接閱讀中文字，適合模型訓練。

6. 欄位對應表
-------------
[ 輸出欄位 ]      [ 原始欄位來源 ]         [ 說明 ]
- 原始謠言        node > orig_rumor        清理後的謠言純文字
- 查核日期        node > updated_time      僅保留日期 YYYY-MM-DD
- 分類            node > article_category  主題分類 (如: 健康、生活)
- 查核單位        (固定值)                 TFC
- 查核報告標題    node > title             報告正式大標題
- 查核報告連結    node > node_url          官方原始網址
- 分類標籤        node > taxo_report_attr  查核結果 (如: 錯誤)