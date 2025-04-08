#import all necessary modules
from  Selenium_task_11 import GuviLogin, Data, Locators


#create an object from Task11 class
myguvilogin=GuviLogin()

# Positive test case to Validate if email box is visible
def test_email_box_visible():
  email_box=myguvilogin.email_box_visible()
  assert email_box is True
  print("Test Passed: Email box visible")
  
#Positive test case to Validate if password box is visible
def test_password_box_visible():
    assert myguvilogin.password_box_visible() is True
    print("Test Passed: Password box visible")

#Positive test cases to see if the submit button is visible
def test_submit_button_visible():
    assert myguvilogin.submit_button_visible() == True
    print("Test Passed:Submit button is visible")

#Positive test case to Validate if email box is enabled
def test_email_box_enabled():
      assert myguvilogin.email_box_enabled() == True
      print("Test Passed: Email box enabled")

#Positive test case to Validate if password box is enabled
def test_password_box_enabled():
    assert myguvilogin.password_box_enabled() == True
    print("Test Passed: Password box Enabled")

# #Positive test case to check if the submit button works for valid email and password
def test_submit_button_enabled():
    assert myguvilogin.submit_button_enabled() == True
    print("Test Passed: Password box Enabled")

#Positive Test cases to Validate URL of login button
def test_positive_login_url():
        expected_login_url = "https://www.guvi.in/courses/?current_tab=myCourses"
        actual_login_url=myguvilogin.login()
        assert actual_login_url== expected_login_url
        print("Test Passed:Positive Login URL")       

# Negative Test case to Validate  URL of login button with wrong credentials
def test_negative_login_url():
    expected_login_url = "https://www.guvi.in/courses/?current_tab"
    actual_login_url = myguvilogin.login_invalid_credentials()
    assert actual_login_url != expected_login_url
    print("Test Passed:Negative Login URL")









