import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from utils import capture_screenshot


# アクション関数
def perform_action(driver, action, selector, value, wait_time, screenshot_dir, log_func=print):
    log_func(f"[ACTION] 実行: {action} | Selector: {selector} | Value: {value}")

    try:
        if action == "click":
            log_func("[ACTION] click 実行中...")
            WebDriverWait(driver, wait_time).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
            ).click()
        
        elif action == "input":
            log_func("[ACTION] input 実行中...")
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            ).send_keys(value)
        
        elif action == "wait":
            log_func(f"[ACTION] wait {value}秒 実行中...")
            time.sleep(float(value))
        
        elif action == "assert_text":
            log_func(f"[ACTION] assert_text '{value}' 実行中...")
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{value}')]"))
            )

        elif action == "hover":
            log_func(f"[ACTION] hover 実行中...")
            element = WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
            ActionChains(driver).move_to_element(element).perform()

        elif action == "hover_click":
            log_func(f"[ACTION] hover_click '{value}' 実行中...")

            # hover対象の要素
            hover_target = WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
            ActionChains(driver).move_to_element(hover_target).perform()
            log_func("[PASS] hver success")

            # click対象の要素
            click_target = WebDriverWait(driver, wait_time).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, value))
            )
            driver.execute_script("arguments[0].click();", click_target)
            log_func("[PASS] click success")

        else:
            log_func(f"[WARN] 未対応のアクション: {action}")
            return False, "Unsupported action", None

        return True, "", None
    except Exception as e:
        log_func(f"[ERROR] アクション失敗: {action} | Error: {e}")
        screenshot_path = capture_screenshot(driver, action, screenshot_dir)
        return False, str(e), screenshot_path