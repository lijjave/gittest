from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# ========== 启动浏览器 ==========
options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)

try:
    # ========== 打开本地 HTML 文件 ==========
    driver.get("file:///" + os.path.abspath("动态元素.html"))
    time.sleep(1)

    # ==================== 1. 使用相对路径 ====================
    # 不写 /html/body/div/div/div 这种绝对路径
    # 直接用 //div[@class='dynamic_class']，不管它在哪一层
    el1 = driver.find_element(By.XPATH, "//div[@class='dynamic_class']")
    print("1. 相对路径找到：", el1.text)

    # ==================== 2. 使用部分匹配 ====================
    # id 是 dynamic_part_12345，后面数字会变
    # 用 contains 匹配固定部分 'dynamic_part'
    el2 = driver.find_element(By.XPATH, "//div[contains(@id, 'dynamic_part')]")
    print("2. 部分匹配找到：", el2.text)

    # ==================== 3. 使用等待机制 ====================
    # dynamic_id 这个元素 2 秒后才出现
    # 用 WebDriverWait 最多等 10 秒，出现了立刻继续
    el3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "dynamic_id"))
    )
    print("3. 等待机制找到：", el3.text)

    # ==================== 4. 使用 JavaScript 定位 ====================
    # 直接用 JS 的 querySelector 找元素
    el4 = driver.execute_script("return document.querySelector('.js-target');")
    print("4. JS 定位找到：", el4.text)

    time.sleep(3)

except Exception as e:
    print("出现异常：", e)

finally:
    driver.quit()
    print("浏览器已关闭")