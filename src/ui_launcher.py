import os, time
import tkinter as tk
from tkinter import filedialog, ttk
from dotenv import load_dotenv
from pathlib import Path
from main_runner import run_test_scenario


def select_file():
    path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    file_path_var.set(path)

def get_log_path():
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    log_dir = Path("./logs")
    log_dir.mkdir(exist_ok=True)
    return log_dir / f"log_{timestamp}.txt"

def log(message: str):
    with open(log_file_path, "a", encoding="utf-8") as f:
        f.write(message + "\n")

def open_log_folder():
    os.startfile(os.path.dirname(log_file_path)) # for Windows

def run_test():
    try:
        url = url_entry.get()
        file_path = file_path_var.get()
        wait_time = int(wait_time_entry.get())
        use_regex = regex_var.get()
        verify_enabled = verify_var.get()
        screenshot_dir = screenshot_entry.get()
        browser = browser_var.get()

        status_label.config(text="", fg="black", bg=root["bg"], height=2)
        root.update_idletasks()

        print(f"実行開始： URL={url}, File={file_path}")
        status_label.config(text="テスト実行中...", fg="blue")
        root.update_idletasks()
        
        report_path = run_test_scenario(url, file_path, wait_time, use_regex, verify_enabled,
                                        screenshot_dir, browser, log_func=log)
        status_label.config(text=f"✅テスト完了！レポート:{report_path}", fg="green")
    except Exception as e:
        status_label.config(text=f"❌エラー発生:{e}", fg="red")


# .envファイルから初期値を読み出し
env_path = Path.cwd().parent / "config" / ".env"
if env_path.exists():
    load_dotenv(env_path)
else:
    print(f"⚠️ .envファイルが見つかりません{env_path}") 
WAIT_TIME = os.getenv("WAIT_TIME")
USE_REGEX = os.getenv("USE_REGEX", "False").lower() == "true"
VERIFY_ENABLED = os.getenv("VERIFY_ENABLED", "False").lower() == "true"
SCREENSHOT_DIR = os.getenv("SCREENSHOT_DIR")

# ログファイルパスを保持
log_file_path = get_log_path()

root = tk.Tk()
root.title("AutoWebTest")
root.geometry('700x400')
root.resizable(True, True)

# 共通パラメータ
ENTRY_WIDTH = 50
PAD_X = 10
PAD_Y = 5

# 画面アイテムの配置行(row)
ROW_URL = 0
ROW_BROWSER_COMBO = ROW_URL + 1
ROW_SCENARIO_FILE = ROW_BROWSER_COMBO + 1
ROW_WAIT_TIME = ROW_SCENARIO_FILE + 1
ROW_USE_REGEX = ROW_WAIT_TIME + 1
ROW_VERIFY_ENABLED = ROW_USE_REGEX + 1
ROW_SCREENSHOT_DIR = ROW_VERIFY_ENABLED + 1
ROW_EXE_BUTTON = ROW_SCREENSHOT_DIR + 1
ROW_STATUS_LABEL = ROW_EXE_BUTTON + 1
ROW_LOG_PATH = ROW_STATUS_LABEL + 1

# URL入力欄
tk.Label(root, text="URL:").grid(row=ROW_URL, column=0, sticky="w", padx=PAD_X, pady=PAD_Y)
url_entry = tk.Entry(root, width=ENTRY_WIDTH)
url_entry.grid(row=ROW_URL, column=1, sticky="w", padx=PAD_X, pady=PAD_Y)

# ブラウザ選択
tk.Label(root, text="使用ブラウザ:").grid(row=ROW_BROWSER_COMBO, column=0, sticky="w", padx=PAD_X, pady=PAD_Y)
browser_var = tk.StringVar(value="Chrome")
browser_combo = ttk.Combobox(root, textvariable=browser_var, values=["Chrome", "Edge", "Safari"], state="readonly", width=15)
browser_combo.grid(row=ROW_BROWSER_COMBO, column=1, sticky="w", padx=PAD_X, pady=PAD_Y)

# ファイル選択
tk.Label(root, text="シナリオファイル (.xlsx):").grid(row=ROW_SCENARIO_FILE, column=0, sticky="w", padx=PAD_X, pady=PAD_Y)
file_path_var = tk.StringVar()
tk.Entry(root, textvariable=file_path_var, width=ENTRY_WIDTH).grid(row=ROW_SCENARIO_FILE, column=1, padx=PAD_X, pady=PAD_Y)
tk.Button(root, text="選択", command=lambda: file_path_var.set(
    filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")]))
).grid(row=ROW_SCENARIO_FILE, column=2, padx=PAD_X, pady=PAD_Y)

# 待機時間入力欄
tk.Label(root, text="待機時間 (秒):").grid(row=ROW_WAIT_TIME, column=0, sticky="w", padx=PAD_X, pady=PAD_Y)
wait_time_entry = tk.Entry(root, width=10)
wait_time_entry.insert(0, WAIT_TIME)
wait_time_entry.grid(row=ROW_WAIT_TIME, column=1, sticky="w", padx=PAD_X, pady=PAD_Y)

# 正規表現チェック
regex_var = tk.BooleanVar(value=USE_REGEX)
tk.Checkbutton(root, text="正規表現を使用", variable=regex_var).grid(row=ROW_USE_REGEX, column=1, sticky="w", padx=PAD_X, pady=PAD_Y)

# 期待結果チェック
verify_var = tk.BooleanVar(value=VERIFY_ENABLED)
tk.Checkbutton(root, text="期待結果を確認する", variable=verify_var).grid(row=ROW_VERIFY_ENABLED, column=1, sticky="w", padx=PAD_X, pady=PAD_Y)

# スクリーンショット保存先入力欄
tk.Label(root, text="スクリーンショット保存先:").grid(row=ROW_SCREENSHOT_DIR, column=0, sticky="w", padx=PAD_X, pady=PAD_Y)
screenshot_entry = tk.Entry(root, width=ENTRY_WIDTH)
screenshot_entry.insert(0, SCREENSHOT_DIR)
screenshot_entry.grid(row=ROW_SCREENSHOT_DIR, column=1, sticky="w", padx=PAD_X, pady=PAD_Y)

# 実行ボタン
tk.Button(root, text="実行", command=run_test, width=20).grid(
    row=ROW_EXE_BUTTON, column=1, pady=20
)

# 状態表示ラベル
status_label = tk.Label(root, text="", bg=root["bg"], height=2)
status_label.grid(row=ROW_STATUS_LABEL, column=0, columnspan=3, sticky="w", padx=PAD_X, pady=PAD_Y)

# ログ保存先表示欄
log_path_var = tk.StringVar(value=str(log_file_path))
tk.Label(root, text="ログ保存先:").grid(row=ROW_LOG_PATH, column=0, sticky="w", padx=PAD_X, pady=PAD_Y)
tk.Entry(root, textvariable=log_path_var, width=ENTRY_WIDTH, state="readonly").grid(row=ROW_LOG_PATH, column=1, padx=PAD_X, pady=PAD_Y)
tk.Button(root, text="ログフォルダを開く", command=open_log_folder).grid(row=ROW_LOG_PATH, column=2, padx=PAD_X, pady=PAD_Y)

root.mainloop()