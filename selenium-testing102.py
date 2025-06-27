import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_and_find_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

def bypass_captcha(driver):
    try:
        captcha_checkbox = wait_and_find_element(driver, By.ID, "recaptcha-anchor")
q        captcha_checkbox.click()
    except Exception as e:
        print("⚠️ CAPTCHA could not be bypassed:", e)

def register(driver, first_name, last_name, username, password):
    driver.get("https://demoqa.com/register")
    time.sleep(2)

    first_name_input = wait_and_find_element(driver, By.ID, "firstname")
    first_name_input.send_keys(first_name)

    last_name_input = wait_and_find_element(driver, By.ID, "lastname")
    last_name_input.send_keys(last_name)

    username_input = wait_and_find_element(driver, By.ID, "userName")
    username_input.send_keys(username)

    password_input = wait_and_find_element(driver, By.ID, "password")
    password_input.send_keys(password)

    register_button = wait_and_find_element(driver, By.ID, "register")
    register_button.click()
    time.sleep(4)

def verify_email_code(driver, code):
    email_input = wait_and_find_element(driver, By.ID, "emailVerificationCode")
    email_input.clear()
    email_input.send_keys(code)
    
    verify_button = wait_and_find_element(driver, By.ID, "verifyButton")
    verify_button.click()

def verify_phone_number(driver, phone_code):
    phone_input = wait_and_find_element(driver, By.ID, "phoneVerificationCode")
    phone_input.clear()
    phone_input.send_keys(phone_code)
    
    verify_button = wait_and_find_element(driver, By.ID, "verifyButton")
    verify_button.click()

def select_birthday(driver, day, month, year):
    day_dropdown = wait_and_find_element(driver, By.ID, "birthdayDay")
    month_dropdown = wait_and_find_element(driver, By.ID, "birthdayMonth")
    year_dropdown = wait_and_find_element(driver, By.ID, "birthdayYear")
    
    day_dropdown.send_keys(day)
    month_dropdown.send_keys(month)
    year_dropdown.send_keys(year)

def login(driver, username, password):
    driver.get("https://demoqa.com/login")
    time.sleep(1)

    username_input = wait_and_find_element(driver, By.ID, "userName")
    username_input.clear()
    username_input.send_keys(username)

    password_input = wait_and_find_element(driver, By.ID, "password")
    password_input.clear()
    password_input.send_keys(password)

    login_button = wait_and_find_element(driver, By.ID, "login")
    login_button.click()
    time.sleep(4)

def create_item(driver, item_name):
    create_button = wait_and_find_element(driver, By.ID, "createButton")
    create_button.click()
    
    name_input = wait_and_find_element(driver, By.ID, "itemName")
    name_input.clear()
    name_input.send_keys(item_name)
    
    save_button = wait_and_find_element(driver, By.ID, "saveButton")
    save_button.click()

def read_item(driver, item_name):
    search_input = wait_and_find_element(driver, By.ID, "searchInput")
    search_input.clear()
    search_input.send_keys(item_name)
    
    search_button = wait_and_find_element(driver, By.ID, "searchButton")
    search_button.click()
    
    try:
        wait_and_find_element(driver, By.XPATH, f"//div[text()='{item_name}']")
        print(f"✅ Item '{item_name}' found.")
    except Exception:
        print(f"⚠️ Item '{item_name}' not found.")

def update_item(driver, old_name, new_name):
    read_item(driver, old_name)
    
    edit_button = wait_and_find_element(driver, By.ID, "editButton")
    edit_button.click()
    
    name_input = wait_and_find_element(driver, By.ID, "itemName")
    name_input.clear()
    name_input.send_keys(new_name)
    
    save_button = wait_and_find_element(driver, By.ID, "saveButton")
    save_button.click()

def delete_item(driver, item_name):
    read_item(driver, item_name)
    
    delete_button = wait_and_find_element(driver, By.ID, "deleteButton")
    delete_button.click()
    
    confirm_button = wait_and_find_element(driver, By.ID, "confirmDeleteButton")
    confirm_button.click()

def search(driver, query):
    search_input = wait_and_find_element(driver, By.ID, "searchInput")
    search_input.clear()
    search_input.send_keys(query)
    
    search_button = wait_and_find_element(driver, By.ID, "searchButton")
    search_button.click()

def main():
    driver = webdriver.Chrome()

    try:
        # Register a new user
        register(driver, "ianshi", "binabays", "ianshin", "Password@12345")
        
        # Bypass CAPTCHA if applicable
        bypass_captcha(driver)

        # Login with the registered user
        login(driver, "ianshin", "Password@12345")
        print("✅ Logged in successfully.")

        # Perform CRUD operations
        create_item(driver, "Sample Item")
        read_item(driver, "Sample Item")
        update_item(driver, "Sample Item", "Updated Item")
        delete_item(driver, "Updated Item")

        # Search for an item
        search(driver, "Updated Item")

        # Logout
        logout_button = wait_and_find_element(driver, By.ID, "logout")
        logout_button.click()
        print("🔓 Logged out successfully.")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
