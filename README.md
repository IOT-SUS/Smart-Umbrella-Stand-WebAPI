# BackendAPI-Flask-Structure
結構化的範例程式

<img width="480" alt="16l3TukgY6FI71lTOSSvAS" src="https://user-images.githubusercontent.com/60885166/147197836-5cec2839-89b6-4ae7-966a-3d095c723dda.png">

## File Structure
```bash
config      # 所有設定資料 ex: secret token
controllers # 所有API的邏輯
models      # 資料庫相關
middlewares # 帳戶驗證相關
libs        # 所有Tools
static      # 所有public的東西 ex: css, js, images...
templates   # 所有html
router.py   # 所有路徑的定義
app.py      # 資料庫相關
run.py      # 程式的進入點
README.md
```
## Installation
```bash
# Step 1 使用 git 下載專案
git clone https://github.com/IOT-SUS/BackendAPI-Flask-Structure.git
cd BackendAPI-Flask-Structure

# Step 2 使用 Miniconda 建立虛擬 python 環境
conda create --name sus python=3.7
conda activate sus

# Step 3 安裝套件
pip3 install -r requirements.txt

# Step 4 修改config檔案
cp cfg.dev.py cfg.py
```

## Run
```bash
python3 run.py
```

### Testing
- 可以使用 [Postman](https://www.postman.com/) 進行測試
