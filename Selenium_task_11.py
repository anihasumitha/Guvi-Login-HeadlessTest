#importing all necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import  sleep

#Creating Data class to store all data 
class Data:
    url = "https://www.guvi.in"
    user_email = "aniha2525@gmail.com"
    user_password = "Aniha@guvi123"
    wrong_user_email = "ani25@gmail.com"
    wrong_user_password = "34343"

#Creating Locators class to store all information regarding the web locators
class Locators:
    email_locator="email"
    password_locator="password"
    login_button_locator='//*[@id="login-btn"]'
    submit_button_locator= '//*[@id="login-btn"]'
    profile_icon='dropdown_title'
    sign_out_button="//div[@id='dropdown_contents' and text()='Sign Out']"

#
class GuviLogin(Data,Locators):
    def __init__(self):
        self.driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    #start method to launch automation
    def start(self):
        try:
            self.driver.maximize_window()
            self.driver.get(Data.url)
            sleep(5)
            print("Homepage URL:",self.driver.current_url)
            return True
        except Exception as error:
            print("Automation failed to start",error)

    def click_login_page(self):
            try:
                self.start()
                sleep(5) # Wait up to 5 seconds
                login_button = self.driver.find_element(by=By.XPATH,value=Locators.login_button_locator)
                login_button.click()
                print("Login URL:", self.driver.current_url)
                return True

            except Exception as e:
                print("Error: Login button not found", e)
                return False


    def login(self):
        try:
                self.click_login_page()
                sleep(5)
                self.driver.find_element(by=By.ID,value=Locators.email_locator).send_keys(Data.user_email)
                self.driver.find_element(by=By.ID,value=Locators.password_locator).send_keys(Data.user_password)
                self.driver.find_element(by=By.XPATH,value=Locators.submit_button_locator).click()
                sleep(5)
                if self.driver.current_url=="https://www.guvi.in/courses/?current_tab=myCourses":
                    print("Login was successful")
                    return self.driver.current_url
                else:
                    print("Login unsuccessful")
                    return False
        except Exception as e:
            print("Automation Flow error",e)
            return False

    def logout(self):

        try:
            # Click the profile icon
            profile_icon = self.driver.find_element(by=By.ID,value=Locators.profile_icon )
            profile_icon.click()
            sleep(2)

            # Click the "Sign Out" button from the dropdown
            sign_out_button = self.driver.find_element(by=By.XPATH, value=Locators.sign_out_button)
            sign_out_button.click()
            sleep(2)

            # Confirm if logout was successful
            print("Current URL after logout:", self.driver.current_url)
            
            if self.driver.current_url == "https://www.guvi.in" :
                print("Logout successful",)
                return True
        
        except Exception as e:
            print("Logout unsuccessful:", e)
            return False

    def login_invalid_credentials(self):
        try:
            self.logout()
           
            sleep(5)
            login_button = self.driver.find_element(by=By.XPATH, value=Locators.login_button_locator)
            login_button.click()
            self.driver.find_element(by=By.ID, value=Locators.email_locator).send_keys(Data.wrong_user_email)
            self.driver.find_element(by=By.ID, value=Locators.password_locator).send_keys(Data.wrong_user_password)
            self.driver.find_element(by=By.XPATH, value=Locators.submit_button_locator).click()
            sleep(5)
            if self.driver.current_url == "https://www.guvi.in/courses/?current_tab=myCourses":
                print("Login was successful")
                return self.driver.current_url
            else:
                print("Login unsuccessful")
                return False

        except Exception as e:
            print("Automation Flow error", e)
            return False
        
        finally:
            self.stop()

    def email_box_visible(self):
        self.click_login_page()
        email_input_box=self.driver.find_element(by=By.ID,value=Locators.email_locator)
        sleep(3)
        if email_input_box.is_displayed():
            return True
        else:
            return False

    def password_box_visible(self):
        password_input_box=self.driver.find_element(by=By.ID,value=Locators.password_locator)
        sleep(3)
        if password_input_box.is_displayed():
            return  True
        else:
            return False

    def submit_button_visible(self):
        submit_button_box = self.driver.find_element(by=By.XPATH, value=Locators.submit_button_locator)
        sleep(3)
        if submit_button_box.is_displayed():
            return True
        else:
            return False

    def email_box_enabled(self):
        email_box=self.driver.find_element(by=By.ID,value=Locators.email_locator)
        sleep(3)
        if email_box.is_enabled():
            return True
        else:
            return False

    def password_box_enabled(self):
        password_input_box=self.driver.find_element(by=By.ID,value=Locators.password_locator)
        sleep(5)
        if password_input_box.is_enabled():
            return  True
        else:
            return False

    def submit_button_enabled(self):
        submit_button_box=self.driver.find_element(by=By.XPATH,value=Locators.submit_button_locator)
        sleep(3)
        if submit_button_box.is_enabled():
            return True
        else:
            return False

    def stop(self):
        self.driver.quit()






