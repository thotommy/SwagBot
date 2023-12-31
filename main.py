from selenium import webdriver
import undetected_chromedriver as uc
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
import random

class SwagBot:
    def __init__(self, username, pw):
        print("Starting Chrome up")
        self.options = webdriver.ChromeOptions()
        self.driver = uc.Chrome(options=self.options)
        self.driver.maximize_window()
        self.username = username
        self.pw = pw
        self.driver.get("https://www.swagbucks.com/p/login")
        sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name=\"emailAddress\"]").send_keys(username)
        self.driver.find_element(By.XPATH, "//input[@name=\"password\"]").send_keys(pw)
        sleep(3)
        self.driver.find_element(By.XPATH, '//button[@id="loginBtn"]').click()
        sleep(100) # wait time for you to do the thing that proves you are not a bot

    def survey(self):
        '''
        Does the survey questions on the right side of the panel in /surveys
        '''
        print("Surveying..")
        self.driver.find_element(By.XPATH, "//a[contains(@href,'/surveys')]").click()
        sleep(2)
        for i in range(1000):
            
            x = random.randint(1,2)
            y = random.randint(1,4)
            sleep(y)
            self._try_and_click_if_exists(driver=self.driver, xpath='//button[@id="sbModalClose"]')
            
            sleep(y)
            self.driver.execute_script("window.scrollTo(0, 0);")
            element = self.driver.find_element(By.CLASS_NAME, "surveyDropdownVal")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()
            sleep(x)
            string1 = f"/html/body/div[2]/div[3]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/span[{str(x)}]"
            print(string1)
            self.driver.find_element(By.XPATH, string1).click()
            sleep(y)
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/div/div[2]/button").click()
            sleep(x)
            print(i)

    def ten_sb_quiz(self):
        '''
        Does the 10 sb quizzes
        '''
        # /html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div // English
        # /html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div/button // Start
        # /html/body/div[1]/div/div/div[3]/div/div[3]/div/button // Next button (Instructions)
        # /html/body/div[1]/div/div/div[3]/div/div[1]/div[2]/div/div/div[1]/div/div[*1-4 or 0-3*]/div/div[2]/div // 4 options or tab space and enter
        # /html/body/div[1]/div/div/div[3]/div/div[1]/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div
        # /html/body/div[1]/div/div/div[3]/div/div[1]/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div
        # /html/body/div[1]/div/div/div[3]/div/div[1]/div[2]/div/div/div[1]/div/div[3]/div/div[2]/div
        # /html/body/div[1]/div/div/div[3]/div/div[1]/div[2]/div/div/div[1]/div/div[4]/div/div[2]/div
        # /html/body/div[1]/div/div/div[3]/div/div[3]/div/button // Next button
        pass

    def _try_and_click_if_exists(self, driver, xpath):
        try:
            driver.find_element(By.XPATH, xpath).click()
        except ElementNotInteractableException:
            print("skipping no pop up")
            

if __name__ == "__main__":
    my_bot = SwagBot("USER_NAME", "PASSWORD")
    my_bot.survey()