from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains



class AltusMenu:
    def __init__(self, driver) -> None:
        self.driver = driver
        
        #Locators
        self.solutions_menu_locator = (By.LINK_TEXT, "Solutions")
        self.altus_valuation_solution_locator = (By.PARTIAL_LINK_TEXT, "Altus Valuation")
        self.altus_market_insights_solution_locator = (By.PARTIAL_LINK_TEXT, "Altus Market Insights")
        self.altus_language_icon_locator = (By.CLASS_NAME, "langDiv")
        self.altus_french_locator = (By.LINK_TEXT, "French")
        self.altus_french_button_locator = (By.LINK_TEXT, "Apprendre encore plus")

    def click_altus_valuation_solution(self):
        self.driver.set_window_size(1500,1000)
        WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located(self.solutions_menu_locator))
        solutions_menu_element = self.driver.find_element(*self.solutions_menu_locator)
        hover = ActionChains(self.driver).move_to_element(solutions_menu_element)
        hover.perform()
        WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located(self.altus_valuation_solution_locator))
        self.driver.find_element(*self.altus_valuation_solution_locator).click()

    def click_altus_market_insights_solution(self):
        self.driver.set_window_size(1500,1000)
        WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located(self.altus_market_insights_solution_locator))
        solutions_menu_element = self.driver.find_element(*self.solutions_menu_locator)
        hover = ActionChains(self.driver).move_to_element(solutions_menu_element)
        hover.perform()
        WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located(self.altus_market_insights_solution_locator))
        self.driver.find_element(*self.altus_market_insights_solution_locator).click()

    def switch_language(self):
        WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located(self.altus_language_icon_locator))
        language_element = self.driver.find_element(*self.altus_language_icon_locator)
        hover = ActionChains(self.driver, 2).move_to_element(language_element)
        hover.perform()
        WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located(self.altus_french_locator))
        self.driver.find_element(*self.altus_french_locator).click()
    
    def get_french_button_text(self):
        WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located(self.altus_french_button_locator))
        return self.driver.find_element(*self.altus_french_button_locator).text


class AltusContactUsPage:
    def __init__(self, driver):
        self.driver = driver
    
        #Locators
        self.contact_us_button_locator = (By.PARTIAL_LINK_TEXT, "Contact us today")
        self.slide_in_title_locator = (By.TAG_NAME, "h2")
        self.after_submit_success_locator = (By.TAG_NAME, "h2")
        self.interest_select_locator = (By.ID, "interest")
        self.offer_interest_select_locator = (By.ID, "offerinterest")
        self.first_name_locator = (By.NAME, "firstname")
        self.last_name_locator = (By.NAME, "lastname")
        self.email_locator = (By.NAME, "Email")
        self.phone_locator = (By.NAME, "phone")
        self.seniority_select_locator = (By.ID, "seniority")
        self.company_locator = (By.ID, "company")
        self.country_select_locator = (By.ID, "country")
        self.province_select_locator = (By.ID, "state")
        self.comments_locator = (By.NAME, "comments")
        self.error_locator = (By.CLASS_NAME, "error-message")
        self.submit_button_locator = (By.XPATH, "//button[@type='submit']")

    #Methods 
        
    #helper method to find a specific element based on text from an array of elements
    def find_element_text_in_elements(self, elements, target):
        for elm in elements:
            print("elm text: " + elm.text)
            if elm.text == target:
                return elm.text 
        return "" 

    def get_error_message(self):
        element = ""
        
        try:
            WebDriverWait(self.driver, 1).until(EC.presence_of_all_elements_located(self.error_locator))
        except TimeoutException:
            print("no error on the page")
        else:
            element = self.driver.find_element(*self.error_locator).text

        print("error message: " + element)
        return element
    
    def click_contact_us(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.contact_us_button_locator))
        element = self.driver.find_element(*self.contact_us_button_locator)
        element.click()
    
    def verify_slide_in_form(self) -> str:
        time.sleep(2)
        # WebDriverWait(self.driver, 2).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, "formContainer.slideIn")))
        elements = self.driver.find_elements(*self.slide_in_title_locator)
        return self.find_element_text_in_elements(elements, "Get in touch with Altus Group")

    def select_interest(self, interest):
        time.sleep(2)
        select = Select(self.driver.find_element(*self.interest_select_locator))
        select.select_by_value(interest)

    def select_offer_interest(self, offer_interest):
        select = Select(self.driver.find_element(*self.offer_interest_select_locator))
        select.select_by_value(offer_interest)

    def enter_first_name(self, first_name):
        first_name_input = self.driver.find_element(*self.first_name_locator)
        first_name_input.clear()
        first_name_input.send_keys(first_name)

    def enter_last_name(self, last_name):
        last_name_input = self.driver.find_element(*self.last_name_locator)
        last_name_input.clear()
        last_name_input.send_keys(last_name)

    def enter_email(self, email):
        time.sleep(1)
        email_input = self.driver.find_element(*self.email_locator)
        email_input.clear()
        email_input.send_keys(email)

    def enter_phone(self, phone):
        time.sleep(1)
        phone_input = self.driver.find_element(*self.phone_locator)
        phone_input.clear()
        phone_input.send_keys(phone)
        return phone_input.get_attribute("value")

    def select_seniority(self, seniority):
        select = Select(self.driver.find_element(*self.seniority_select_locator))
        select.select_by_value(seniority)
    
    def enter_company(self, company):
        company_input = self.driver.find_element(*self.company_locator)
        company_input.clear()
        company_input.send_keys(company)

    def select_country(self, country):
        select = Select(self.driver.find_element(*self.country_select_locator))
        select.select_by_value(country)

    def select_province(self, province):
        select = Select(self.driver.find_element(*self.province_select_locator))
        select.select_by_value(province)

    def enter_comments(self, comments):
        comments_input = self.driver.find_element(*self.comments_locator)
        comments_input.clear()
        comments_input.send_keys(comments)

    def click_submit_button(self):
        time.sleep(1)
        self.driver.find_element(*self.submit_button_locator).click()

    def verify_submit_success(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, "insights")))
        elements = self.driver.find_elements(*self.after_submit_success_locator)
        return self.find_element_text_in_elements(elements, "Thank you for your inquiry")


class ContactUsPageTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(ContactUsPageTests, self).__init__(*args, **kwargs)
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.altusgroup.com/contact-us/")
        print("Title: " + self.driver.title)

    def tearDown(self):
        self.driver.quit()
        return super().tearDown()


    def test_slide_in_form(self):
        contact_us_page = AltusContactUsPage(self.driver)
        contact_us_page.click_contact_us()
        res = contact_us_page.verify_slide_in_form()
        print("element text: " + res)
        self.assertEqual("Get in touch with Altus Group", res)
    

    def test_mandatory_fields(self):
        contact_us_page = AltusContactUsPage(self.driver)
        contact_us_page.click_contact_us()
        contact_us_page.select_interest("Altus Solution")
        contact_us_page.select_offer_interest("Altus Valuation")
        contact_us_page.enter_first_name("Luke")
        contact_us_page.enter_last_name("Skywalker")
        contact_us_page.enter_email("Skywalker@gmail.com")
        contact_us_page.enter_phone("6488208456")
        contact_us_page.enter_company("New Republic")
        contact_us_page.select_country("Canada")
        contact_us_page.select_province("Ontario")
        contact_us_page.enter_comments("May the force be with you!")
        contact_us_page.click_submit_button()
        submit_success_elm = contact_us_page.verify_submit_success()
        print("submit success text: " + submit_success_elm)
        self.assertEqual("Thank you for your inquiry", submit_success_elm)

    def verify_field_error_msg_helper(self, page, expected_err_msg):
        err_msg = page.get_error_message()
        self.assertEqual(err_msg, expected_err_msg)

    def test_mandatory_fields_negative(self):
        contact_us_page = AltusContactUsPage(self.driver)
        contact_us_page.click_contact_us()
        contact_us_page.click_submit_button()

        self.verify_field_error_msg_helper(contact_us_page, "This is a required field")
        
        contact_us_page.select_interest("Altus Solution")
        self.verify_field_error_msg_helper(contact_us_page, "This is a required field")
        
        contact_us_page.select_offer_interest("Altus Valuation")
        self.verify_field_error_msg_helper(contact_us_page, "This is a required field")

        contact_us_page.enter_first_name("Luke")
        self.verify_field_error_msg_helper(contact_us_page, "This is a required field")

        contact_us_page.enter_last_name("Skywalker")
        self.verify_field_error_msg_helper(contact_us_page, "This is a required field")

        contact_us_page.enter_email("Skywalker@gmail.com")
        self.verify_field_error_msg_helper(contact_us_page, "This is a required field")

        contact_us_page.enter_phone("6488208456")
        self.verify_field_error_msg_helper(contact_us_page, "This is a required field")

        contact_us_page.enter_company("New Republic")
        self.verify_field_error_msg_helper(contact_us_page, "This is a required field")

        contact_us_page.select_country("Israel")
        self.verify_field_error_msg_helper(contact_us_page, "This is a required field")

        contact_us_page.enter_comments("May the force be with you!")
        err_msg = contact_us_page.get_error_message()
        self.assertEqual(err_msg, "")


    def test_email_field(self):
        contact_us_page = AltusContactUsPage(self.driver)
        contact_us_page.click_contact_us()
        contact_us_page.enter_email("John")
        self.verify_field_error_msg_helper(contact_us_page, "Please use a valid email address")
        contact_us_page.enter_email("John@")
        self.verify_field_error_msg_helper(contact_us_page, "Please use a valid email address")
        contact_us_page.enter_email("John@mail")
        self.verify_field_error_msg_helper(contact_us_page, "Please use a valid email address")
        contact_us_page.enter_email("John@mail.c")
        self.verify_field_error_msg_helper(contact_us_page, "Please use a valid email address")
        contact_us_page.enter_email("John@mail.co")
        err_msg = contact_us_page.get_error_message()
        self.assertEqual(err_msg, "")
        
    def test_phone_field(self):
        contact_us_page = AltusContactUsPage(self.driver)
        contact_us_page.click_contact_us()
        phone_input_result = contact_us_page.enter_phone("asdkvdsdf!@#$*)(_")
        self.assertEqual(phone_input_result, "")
        phone_input_result = contact_us_page.enter_phone("6429981314")
        self.assertEqual(phone_input_result, "6429981314")

class MenuPageTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(MenuPageTests, self).__init__(*args, **kwargs)
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.altusgroup.com/")
        print("Title: " + self.driver.title)

    def tearDown(self):
        self.driver.quit()
        return super().tearDown()
    
    # currently can only handle expanded menu
    def test_navigation(self):
        altus_menu_page = AltusMenu(self.driver)
        altus_menu_page.click_altus_valuation_solution()
        WebDriverWait(altus_menu_page.driver, 2).until(EC.url_to_be("https://www.altusgroup.com/altus-valuation/"))
        self.assertEqual(altus_menu_page.driver.current_url, "https://www.altusgroup.com/altus-valuation/", "Wrong page")
        altus_menu_page.click_altus_market_insights_solution()
        WebDriverWait(altus_menu_page.driver, 2).until(EC.url_to_be("https://www.altusgroup.com/altus-market-insights/"))
        self.assertEqual(altus_menu_page.driver.current_url, "https://www.altusgroup.com/altus-market-insights/")

    def test_language_switch(self):
        altus_menu_page = AltusMenu(self.driver)
        altus_menu_page.switch_language()
        WebDriverWait(altus_menu_page.driver, 2).until(EC.url_to_be("https://www.altusgroup.com/?lang=fr"))
        self.assertEqual(altus_menu_page.driver.current_url, "https://www.altusgroup.com/?lang=fr")
        french_button_text = altus_menu_page.get_french_button_text()
        self.assertEqual(french_button_text, "Apprendre encore plus")
        
unittest.main()
