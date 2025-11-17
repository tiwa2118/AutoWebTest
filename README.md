# AutoWebTest
## 🧩 概要
AutoWebTestは、Excelのシナリオファイルを元にWebアプリのテスト自動化ツールです。  
Seleniumをベースに、検証・スクリーンショット・レポート出力まで一括で実行できます。

---

## 🚀 特徴
- Excelでテストシナリオを記述
- GUI操作で簡単に実行
- 実行結果をExcel形式でレポート出力

---

## 🛠️ インストールと実行方法
### 1. リポジトリをクローン
```bash
git clone https://github.com/yourname/AutoWebTest.git
cd AutoWebTest
```

### 2. .envファイルの準備
```bash
cp config/.env.example config/.env
```
必要に応じて.envを編集してください。

### 3. 依存パッケージのインストール
```bash
pip install -r requirements.txt
```

### 4. 実行
```bash
python src/ui_launcher.py
```
PyInstallerでビルドされた .exe も利用可能です。

---

## 📄 シナリオファイルの書き方
- 各シートが1つのシナリオ
- アクション列、ターゲット列、値列などを記述
- 詳細は scenarios/sample_scenario.xlsx を参照
