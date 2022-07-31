import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestMiniProfile(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_show_mini_profile(self):
        # steps
        browser = self.browser #buka web browse
        browser.get("https://opensource-demo.orangehrmlive.com/ ") #buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[2]/input").send_keys("Admin") #isi username
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#txtPassword").send_keys("admin123") #isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() #klik tombol login
        time.sleep(3)
        browser.find_element(By.ID,"menu_directory_viewDirectory").click() #go to menu admin
        time.sleep(3)


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__":
    unittest.main()