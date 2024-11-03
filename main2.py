from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from io import StringIO
# tải và khởi tạo webdriver chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://fbref.com/en/squads/822bd0ba/2023-2024/Liverpool-Stats"
driver.get(url)

# xác định vị trí của bảng table
table = driver.find_element(By.XPATH, "//table[contains(@class, 'stats_table')]")
# trích suất nội dung của HTML
html_data = table.get_attribute('outerHTML')
df = pd.read_html(StringIO(html_data))[0]

# lưu vào file results.csv
df.to_csv('results.csv', index=False)


