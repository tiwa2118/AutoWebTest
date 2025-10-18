import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import capture_screenshot


# 期待値検証
def verify_expected_text(driver, expected_raw, wait_time, use_regex, screenshot_dir, log_func=print):
    log_func(f"[VERIFY] 期待値検証開始: {expected_raw}")
    try:
        if not expected_raw:
            return True, "", None

        mode, expected_text = "text", expected_raw
        if ":" in expected_raw:
            mode, expected_text = expected_raw.split(":", 1)

        body = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        page_text = body.text

        if mode == "regex" and use_regex:
            log_func(f"[VERIFY] 正規表現モード | Pattern: {expected_text}")
            if re.search(expected_text, page_text):
                log_func("[VERIFY] 検証成功")
                return True, "", None
            else:
                log_func(f"[VERIFY] 検証失敗 | 条件不一致: {expected_text}")
                return False, f"Pattern '{expected_text}' not matched", capture_screenshot(driver, "verify_fail", screenshot_dir)
        else:
            log_func(f"[VERIFY] 通常テキストモード | Text: {expected_text}")
            if expected_text in page_text:
                log_func("[VERIFY] 検証成功")
                return True, "", None
            else:
                log_func(f"[VERIFY] 検証失敗 | 条件不一致: {expected_text}")
                return False, f"Text '{expected_text}' not found", capture_screenshot(driver, "verify_fail", screenshot_dir)
    
    except Exception as e:
        return False, str(e), capture_screenshot(driver, "verify_fail", screenshot_dir)