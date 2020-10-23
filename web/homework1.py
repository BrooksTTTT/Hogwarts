import shelve

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


class TestCeshiren():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_method(self, method):
        self.driver.quit()

    def test_cookies(self):
        # shelve python 内置模块,数据持久化存储的库
        # 可以通过key value 来
        db = shelve.open("cookies")
        cookies = db['cookie']
        db.close
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index/")
        sleep(3)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index/")
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys(
            "c://Users/82506/Desktop/x1.xlsx")
        sleep(3)
        filename = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        assert "x1.xlsx" == filename
        sleep(3)
