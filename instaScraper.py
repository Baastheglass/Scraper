import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import requests
from bs4 import BeautifulSoup
import time


def searchHashtag(searchCriteria):
    driver = uc.Chrome()
    actions = ActionChains(driver)
    driver.get("https://www.instagram.com/")
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#loginForm > div > div:nth-child(1) > div > label > input")))
    driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(1) > div > label > input").send_keys("solace.vfx")
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#loginForm > div > div:nth-child(2) > div > label > input")))
    driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(2) > div > label > input").send_keys("baasilkindagay")
    print("About to wait")
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3) > button")))
    print("After waiting")
    driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3) > button").click()
    print("Login button has been clicked")
    time.sleep(5)
    print("Waiting to click Search button")
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='x1iyjqo2 xh8yej3'] div:nth-child(2) span:nth-child(1) div:nth-child(1) a:nth-child(1)")))
    driver.find_element(By.CSS_SELECTOR, "div[class='x1iyjqo2 xh8yej3'] div:nth-child(2) span:nth-child(1) div:nth-child(1) a:nth-child(1)").click()
    print("Search button clicked")
    print("About to wait to click searchBar")
    WebDriverWait(driver, 100).until(EC.presence_of_element_located, (By.CSS_SELECTOR, "input[placeholder='Search']"))
    print("Search Bar located")
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']").send_keys(searchCriteria)
    time.sleep(5)
    print("Waiting for presence of top searchBar")
    WebDriverWait(driver, 100).until(EC.presence_of_element_located, (By.XPATH, "(//div[@class='x9f619 x1ja2u2z x78zum5 x2lah0s x1n2onr6 x1qughib x6s0dn4 xozqiw3 x1q0g3np'])[1]"))
    driver.find_element(By.XPATH, "(//div[@class='x9f619 x1ja2u2z x78zum5 x2lah0s x1n2onr6 x1qughib x6s0dn4 xozqiw3 x1q0g3np'])[1]").click()
    print("Clicked top search element")
    time.sleep(10)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located, (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[2]/div/div[1]/div[2]/div/a"))
    post = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[2]/div/div[1]/div[2]/div/a")
    print("About to click top post")
    post.click()
    print("Top post clicked")
    time.sleep(10)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located, (By.XPATH, "(//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1'])[5]"))
    #comments = driver.find_element(By.CLASS_NAME, "_ap3a _aaco _aacu _aacx _aad7 _aade")
    #print(comments.text)
    #comments = []
    for i in range(100):
        while(driver.find_element(By.XPATH, "(//*[name()='svg'][@aria-label='Load more comments'])[1]") != None):
            scrollButton = driver.find_element(By.XPATH, "(//*[name()='svg'][@aria-label='Load more comments'])[1]")
            time.sleep(2.5)
            actions.move_to_element(scrollButton)
            time.sleep(2.5)
            scrollButton.click()
            time.sleep(2.5)
            spans = driver.find_elements(By.TAG_NAME, "span")
            count = 0
            for span in spans:
                if(span.get_attribute('dir') == "auto" and span.text and count > 47 and span != spans[-1]):
                    print(span.text)
                count += 1
            # comment = commentSection.find_elements(By.CLASS_NAME, "_a9zs")
            # time.sleep(2.5)
            # comments.append(comment)
            # for c in comment:
            #     print(c.text)
            # print('\n')
            try:
                driver.find_element(By.XPATH, "(//*[name()='svg'][@aria-label='Load more comments'])[1]")
            except:
                break
        print("While loop exited")
        #comments = list(dict.fromkeys(comments))
        #comments2 = dict.fromkeys(str(comments) for comment in comments)
        driver.find_element(By.XPATH, "(//*[name()='svg'][@aria-label='Next'])[1]").click()
        time.sleep(5)
        
        #print(comments.text)
        time.sleep(2.5)
            
    # driver.find_element(By.XPATH, "(//*[name()='svg'][@aria-label='Next'])[1]").click()
    # for i in range(5):
    #     commentSection = driver.find_element(By.XPATH, "(//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1'])[5]")
    #     comments = commentSection.find_elements(By.CLASS_NAME, "_a9zs")
    #     for comment in comments:
    #         print(comment.text)
    #     driver.find_element(By.XPATH, "(//*[name()='svg'][@aria-label='Next'])[1]").click()
    #     time.sleep(5)
    
searchHashtag("#pink")