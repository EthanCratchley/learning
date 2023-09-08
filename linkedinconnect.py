from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

def login(driver):
    # Navigate to the LinkedIn login page
    driver.get("https://www.linkedin.com/login")

    # Wait for the username input field to be present
    username_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )

    # Enter your username
    username_element.send_keys("username")  # Replace with your actual username

    # Find and enter the password
    password_element = driver.find_element(By.ID, "password")
    password_element.send_keys("password")  # Replace with your actual password

    # Click the login button
    driver.find_element(By.XPATH, "//button[text()='Sign in']").click()

def goto_network(driver):
    # Wait for the "My Network" icon to be present and click it
    my_network_element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "global-nav__primary-link"))
)
    my_network_element.click()

def send_requests(driver):
    # Number of requests you want to send
    n = int(input("Number of requests: "))

    for i in range(n):
        # position(in px) of connection button
        pyautogui.click(880, 770)
    print("Done!")

def main():
    # Create a WebDriver instance using the Chrome driver
    driver = webdriver.Chrome()

    # Call the login function to log in
    login(driver)

    # Call the function to go to the network page
    goto_network(driver)

    # Call the function to send requests
    send_requests(driver)

    # Close the browser when done
    driver.quit()

if __name__ == "__main__":
    main()
