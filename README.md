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

## 📂 構成
```
AutoWebTest/
├── config(※配置必須)/
│   └── .env.example
│
├── scenarios(※指定可能)/
│   └── sample_scenario.xlsx
│
├── reports/
│
├── screenshots(※指定可能)/
│
├── logs/
│
├── src/
│   ├── actions.py
│   ├── main_runner.py
│   ├── ui_launcher.py
│   ├── utils.py
│   └── verify.py
│
├── .gitignore
│
└── README.md
```

---

## 📄 シナリオファイルの書き方
- 各シートが1つのシナリオ( 現在の実装では **アクティブシートのみが対象**（複数シートには未対応）)
- アクション列、ターゲット列、値列などを記述
- 詳細は [scenarios/sample_scenario.xlsx](https://github.com/tiwa2118/AutoWebTest/releases) を参照

### 1. sample_scenario.xlsx の説明
| 列名 | 説明 |
| ---- | ---- |
| Test Case ID | テストケースの識別子（空欄はスキップされる） |
| Action | 実行する操作（click, input, wait, assert_textなど） |
| Selector | 操作対象の要素（CSSセレクタで指定） |
| Value | 入力値や待機秒数など、アクションに応じた値 |
| Expected Result | 検証対象の文字列（通常テキスト or regex:パターン）。<br>アクションを行った後の期待値とする出力文字列を設定する。 |

### 2. シナリオの書き方（サンプル）
| Test Case ID | Action | Selector | Value | Expected Result |
| ---- | ---- | ---- | ---- | ---- |
| Test_001 | click | #xxxx |  | アカウント |
| Test_002 | click | #xxxx |  | ログイン |
| Test_003 | input | #xxxx | {your_id} |  |
| Test_004 | input | #xxxx | {your_password} |  |
| Test_005 | click | #xxxx |  |  |
| Test_006 | wait |  | 5 | ようこそ {your_id} さん！ |

---

## 📈 実行後のレポートファイルについて
- 実行後にはシナリオファイルに以下の列を追加する形式で、レポートファイルを出力します
- 詳細はreports/sample_reports.xlsx を参照

| 列名 | 説明 |
| ---- | ---- |
| Status | 成功/失敗（Success/Failed） |
| Error | エラーメッセージ（セレクター取得の失敗時など） |
| Screenshot | アクションの失敗時のスクリーンショットリンク |
| Verify Screenshot | 検証失敗時のスクリーンショットリンク。<br>アクションには成功したが、検索文字列が見つからないときなど。 |

---

## 📜 ライセンス
AutoWebTestは MIT License の下で公開されています。
