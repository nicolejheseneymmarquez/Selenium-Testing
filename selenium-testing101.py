import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def wait_and_find_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

def handle_captcha(driver):
    try:
        captcha_element = driver.find_element(By.ID, "captcha")  # Adjust the selector as needed
        print("Captcha detected. Skipping...")
        # Logic to skip or handle captcha if possible
    except NoSuchElementException:
        print("No captcha found.")

def input_email_verification_code(driver, code):
    email_code_input = wait_and_find_element(driver, By.ID, "email-verification-code")  # Adjust the selector
    email_code_input.clear()
    email_code_input.send_keys(code)

def input_phone_verification_otp(driver, otp):
    otp_input = wait_and_find_element(driver, By.ID, "otp-input")  # Adjust the selector
    otp_input.clear()
    otp_input.send_keys(otp)

def select_birthday(driver, day, month, year):
    day_dropdown = wait_and_find_element(driver, By.ID, "birthday-day")  # Adjust the selector
    month_dropdown = wait_and_find_element(driver, By.ID, "birthday-month")  # Adjust the selector
    year_dropdown = wait_and_find_element(driver, By.ID, "birthday-year")  # Adjust the selector

    day_dropdown.send_keys(day)
    month_dropdown.send_keys(month)
    year_dropdown.send_keys(year)

def upload_file(driver, file_path):
    file_input = wait_and_find_element(driver, By.ID, "file-upload")  # Adjust the selector
    file_input.send_keys(file_path)

def handle_dynamic_elements(driver):
    try:
        modal = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "modal-id")))  # Adjust the selector
        print("Modal detected. Closing...")
        close_button = modal.find_element(By.CLASS_NAME, "close")  # Adjust the selector
        close_button.click()
    except TimeoutException:
        print("No modal found.")

def toggle_checkbox(driver, checkbox_id):
    checkbox = wait_and_find_element(driver, By.ID, checkbox_id)  # Adjust the selector
    if not checkbox.is_selected():
        checkbox.click()

def select_radio_button(driver, radio_id):
    radio_button = wait_and_find_element(driver, By.ID, radio_id)  # Adjust the selector
    if not radio_button.is_selected():
        radio_button.click()

def handle_alert(driver):
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print(f"[Alert] {alert.text}")
        alert.accept()  # or alert.dismiss() for cancel
    except TimeoutException:
        print("No alert found.")

def select_from_dropdown(driver, dropdown_id, value):
    dropdown = Select(wait_and_find_element(driver, By.ID, dropdown_id))  # Adjust the selector
    dropdown.select_by_visible_text(value)

def click_delayed_button(driver, button_id):
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, button_id)))  # Adjust the selector
    button.click()

def create_user(driver, user_data):
    driver.get("https://example.com/create-user")
    wait_and_find_element(driver, By.ID, "username").send_keys(user_data['username'])
    wait_and_find_element(driver, By.ID, "email").send_keys(user_data['email'])
    wait_and_find_element(driver, By.ID, "submit").click()

def read_user(driver, user_id):
    driver.get(f"https://example.com/user/{user_id}")
    # Logic to read user details

def update_user(driver, user_id, updated_data):
    driver.get(f"https://example.com/user/{user_id}/edit")
    wait_and_find_element(driver, By.ID, "username").clear()
    wait_and_find_element(driver, By.ID, "username").send_keys(updated_data['username'])
    wait_and_find_element(driver, By.ID, "submit").click()

def delete_user(driver, user_id):
    driver.get(f"https://example.com/user/{user_id}/delete")
    wait_and_find_element(driver, By.ID, "confirm").click()

def view_dashboard(driver):
    driver.get("https://example.com/dashboard")
    # Logic to extract and display dashboard info

def search_keyword(driver, keyword):
    search_box = wait_and_find_element(driver, By.ID, "search")  # Adjust the selector
    search_box.clear()
    search_box.send_keys(keyword)
    search_box.submit()  # or click the search button

def handle_pagination(driver):
    while True:
        # Logic to process items on the current page
        try:
            next_button = wait_and_find_element(driver, By.ID, "next-page")  # Adjust the selector
            next_button.click()
        except TimeoutException:
            print("No more pages.")
            break

def logout(driver):
    logout_button = wait_and_find_element(driver, By.ID, "logout")  # Adjust the selector
    logout_button.click()

# Example usage
if __name__ == "__main__":
    driver = webdriver.Chrome()
    try:
        driver.get("https://demoqa.com/login")
        time.sleep(1)

        # Example login process
        username = wait_and_find_element(driver, By.ID, "userName")
        username.clear()
        username.send_keys("your_username")
        password = wait_and_find_element(driver, By.ID, "password")
        password.clear()
        password.send_keys("your_password")
        login_button = wait_and_find_element(driver, By.ID, "login")
        login_button.click()
        time.sleep(4)

        # Call other functions as needed
        # e.g., view_dashboard(driver), search_keyword(driver, "example"), etc.

    finally:
        driver.quit()
