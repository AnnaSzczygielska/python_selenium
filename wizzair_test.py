# -*- coding: utf-8 -*-
"""
Przypadki testowe:

I Rejestracja z błędnie wprowadzonym adresem e-mail.

Warunki wstępne:
Wejść na stronę https://wizzair.com/pl-pl#/

Kroki:
1. Kliknij w prawym górnym rogu ZALOGUJ SIĘ
2. Wybierz REJESTRACJA
3. Wprowadź imię
4. Wprowadź nazwisko
5. Wybierz płeć
6. Wybierz kod kraju
7. Wprowadź numer telefonu
8. Wprowadź e-mail bez znaku małpa
9. Wprowadź hasło
10. Wybierz narodowość
11. Akceptuj politykę prywatności
12. Kliknij ZAREJESTRUJ SIĘ

Oczekiwany resultat:
System wyświetla informację o błędnie wprowadzonym adresie e-mail.

"""

import unittest, time
from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.select import Select


class RejestracjaWizzair(unittest.TestCase):

# Warunki wstępne:
# Wejść na stronę https://wizzair.com/pl-pl#/'
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://wizzair.com/pl-pl#/")
        self.driver.maximize_window()

    def test_bledny_email(self):
# Kroki:
# 1. Kliknij w prawym górnym rogu ZALOGUJ SIĘ
        sign_in_button = self.driver.find_element_by_xpath('//button[@data-test="navigation-menu-signin"]')
        sign_in_button.click()

# 2. Wybierz REJESTRACJA
        registration_button = self.driver.find_element_by_xpath('//button[contains(text(), "Rejestracja")]')
        registration_button.click()

# 3. Wprowadź imię
        first_name_field = self.driver.find_element_by_name('firstName')
        first_name_field.send_keys("Alina")

# 4. Wprowadź nazwisko
        surname_field = self.driver.find_element_by_xpath('//input[@placeholder="Nazwisko"]')
        surname_field.send_keys("Lina")

# 5. Wybierz płeć
        gender_button = self.driver.find_element_by_xpath('//label[@for="register-gender-female"]')
        gender_button.click()

# 6. Wybierz kod kraju
        code_to_choose = self.driver.find_element_by_xpath('//div[@data-test="booking-register-country-code"]').click()
        codes_list = self.driver.find_elements_by_xpath('//ul[@class="phone-number__calling-code-selector__dropdown phone-number__calling-code-selector__dropdown--covering"]/li')
        #countries = code_list.find_elements_by_tag_name("li")

        for li in codes_list:
            code = li.find_element_by_xpath('//div[@class="phone-number__calling-code-selector__dropdown__item__country"]')
            if code.get_attribute("innerText") == "Polska (+48)":
                code.location_once_scrolled_into_view
                time.sleep(10)
                code.click()
                break

# 7. Wprowadź numer telefonu
        #phone_number = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.NAME, "phoneNumberValidDigits"))
        phone_number_field = self.driver.find_element_by_name("phoneNumberValidDigits")
        phone_number_field.send_keys("666777888")

# 8. Wprowadź e-mail bez znaku małpa
        incorrect_email_field = self.driver.find_element_by_xpath('//input[@data-test="booking-register-email"]')
        incorrect_email_field.send_keys("alina.linawp.pl")

# 9. Wprowadź hasło
        password_field = self.driver.find_element_by_xpath('//input[@data-test="booking-register-password"]')
        password_field.send_keys("haslo123")

# 10. Wybierz narodowość
        country_to_choose = self.driver.find_element_by_xpath('//input[@data-test="booking-register-country"]').click()
        countries_list = self.driver.find_elements_by_xpath('//div[@data-test="register-form__country-container__locations"]/label')
        #countries = code_list.find_elements_by_tag_name("li")

        for label in countries_list:
            country = label.find_elements_by_tag_name('strong')
            if country.get_attribute("innerText") == "Polska":
                country.location_once_scrolled_into_view
                country.click()
                break

# 11. Akceptuj politykę prywatności
        privacy_policy = self.driver.find_element_by_xpath('//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]')
        privacy_policy.click()

# 12. Kliknij ZAREJESTRUJ SIĘ
        register_button = self.driver.find_element_by_xpath('//button[@data-test="booking-register-submit"]')
        register_button.click()

        self.driver.save_screenshot('screenshot_wizzair_test.png')

    def tearDown(self):
        self.driver.quit()

        time.sleep(2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
