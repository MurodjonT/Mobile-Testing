import time

from appium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "11.0",
    "deviceName": "Pixel_6_Pro_API_30_11.0",
    "automationName": "UiAutomator2",
    "app": "C://Users//MSI_63//Desktop//app//Anor-27_02_2023-1.1.6-debug.apk",
    "appPackage": "uz.anormobile.retail",
    "appActivity": "uz.anorbank.retail.ui.main.MainActivity"
}

lang_uz = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout" \
          "/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup" \
          "/android.widget.LinearLayout[1][@class=\"android.widget.LinearLayout\"]"
input_number = "uz.anormobile.retail:id/editTextPhoneNumber"
checkbox_icon = "uz.anormobile.retail:id/checkBox"
register_btn = "uz.anormobile.retail:id/rvBtnRegister"
input_mahfiy = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout" \
               "/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout" \
               "/android.widget.LinearLayout/android.widget.LinearLayout" \
               "/android.widget.EditText[@text=\"Mahfiy soʻzni kiriting\"]"
cont_btn = "uz.anormobile.retail:id/rvBtnContinue"
pin1 = "uz.anormobile.retail:id/text4"
pin2 = "uz.anormobile.retail:id/text2"
pin3 = "uz.anormobile.retail:id/text0"
pin4 = "uz.anormobile.retail:id/text2"



mobile_driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
mobile_driver.implicitly_wait(60)
WebDriverWait(mobile_driver, 50).until(ec.element_to_be_clickable((MobileBy.XPATH, lang_uz))).click()
time.sleep(2)
WebDriverWait(mobile_driver, 50).until(ec.visibility_of_element_located((MobileBy.ID, input_number))).send_keys("#")
WebDriverWait(mobile_driver, 50).until(ec.element_to_be_clickable((MobileBy.ID, checkbox_icon))).click()
WebDriverWait(mobile_driver, 50).until(ec.element_to_be_clickable((MobileBy.ID, register_btn))).click()
time.sleep(2)
WebDriverWait(mobile_driver, 50).until(ec.visibility_of_element_located((MobileBy.XPATH, input_mahfiy))).send_keys("#")
WebDriverWait(mobile_driver, 50).until(ec.element_to_be_clickable((MobileBy.ID, cont_btn))).click()
for i in range(0, 2):
    WebDriverWait(mobile_driver, 50).until(ec.element_to_be_clickable((MobileBy.ID, pin1))).click()
    time.sleep(1)
    WebDriverWait(mobile_driver, 50).until(ec.element_to_be_clickable((MobileBy.ID, pin2))).click()
    time.sleep(1)
    WebDriverWait(mobile_driver, 50).until(ec.element_to_be_clickable((MobileBy.ID, pin3))).click()
    time.sleep(1)
    WebDriverWait(mobile_driver, 50).until(ec.element_to_be_clickable((MobileBy.ID, pin4))).click()
list_pin = [pin1, pin2, pin3, pin4]
# for i in range(0, 2):
#     for j in range(0, 4):
#         WebDriverWait(mobile_driver, 50).until(ec.element_to_be_clickable((MobileBy.ID, list_pin[]))).click()






