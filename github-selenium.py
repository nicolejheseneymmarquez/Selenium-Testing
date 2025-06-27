import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_and_find_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

def login(driver, username, password):
    driver.get("https://github.com/login")
    time.sleep(2)

    username_input = wait_and_find_element(driver, By.ID, "login_field")
    username_input.clear()
    username_input.send_keys(username)

    password_input = wait_and_find_element(driver, By.ID, "password")
    password_input.clear()
    password_input.send_keys(password)

    login_button = wait_and_find_element(driver, By.NAME, "commit")
    login_button.click()
    time.sleep(4)

def create_repository(driver, repo_name, description):
    driver.get("https://github.com/new")
    time.sleep(2)

    repo_name_input = wait_and_find_element(driver, By.ID, "repository_name")
    repo_name_input.clear()
    repo_name_input.send_keys(repo_name)

    description_input = wait_and_find_element(driver, By.ID, "repository_description")
    description_input.clear()
    description_input.send_keys(description)

    # Optionally, set the repository to public or private
    public_radio = wait_and_find_element(driver, By.ID, "repository_visibility_public")
    public_radio.click()

    create_button = wait_and_find_element(driver, By.XPATH, "//button[contains(text(), 'Create repository')]")
    create_button.click()
    time.sleep(4)

def main():
    driver = webdriver.Chrome()

    try:
        # Login to GitHub
        login(driver, "your_username", "your_password")  # Replace with your GitHub credentials

        # Create a new repository
        create_repository(driver, "Test-Repo", "This is a test repository created by Selenium.")
        print("✅ Repository created successfully.")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
