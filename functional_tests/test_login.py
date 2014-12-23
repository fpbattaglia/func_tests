__author__ = 'fpbatta'
from .base import FunctionalTest
from selenium.webdriver.support.ui import WebDriverWait
import time


class LoginTest(FunctionalTest):
    def switch_to_new_window(self, text_in_title):
        retries = 60
        while retries > 0:
            for handle in self.browser.window_handles:
                self.browser.switch_to.window(handle)
                if text_in_title in self.browser.title:
                    return
            retries -= 1
            time.sleep(0.5)
        self.fail('could not find window')

    def wait_for_element_with_id(self, element_id):
        WebDriverWait(self.browser, timeout=30).until(
            lambda b: b.find_element_by_id(element_id),
            'Could not find element with id {}. Page text was {}'.format(
                element_id, self.browser.find_element_by_tag_name('body').text
            )
        )

    def wait_to_be_logged_in(self):
        self.wait_for_element_with_id('id_logout')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn('fpb@mockmyid.com', navbar.text)

    def wait_to_be_logged_out(self):
        self.wait_for_element_with_id('id_login')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertNotIn('fpb@mockmyid.com', navbar.text)

    def test_login_with_persona(self):
        #finds a sign in link and clicks it
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_login').click()

        # A personal window appears, switch to it
        self.switch_to_new_window('Mozilla Persona')

        #Edith logs in with her email address
        self.browser.find_element_by_id('authentication_email'
        ).send_keys('fpb@mockmyid.com')
        self.browser.find_element_by_tag_name('button').click()

        # close the Persona window
        self.switch_to_new_window('To-Do')

        #she's logged in
        self.wait_to_be_logged_in()

        # refresh the page and try again
        self.browser.refresh()
        self.wait_to_be_logged_in()

        self.browser.find_element_by_id('id_logout').click()
        self.wait_to_be_logged_out()

        # refresh and try again
        self.browser.refresh()
        self.wait_to_be_logged_out()
