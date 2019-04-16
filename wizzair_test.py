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

import unittest
from selenium import webdriver
import time

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
        #country_code_button = self.driver.find_element_by_name("phone-number-country-code")
        #country_code_button.click()

        code_to_choose = self.driver.find_element_by_xpath('//div[@data-test="booking-register-country-code"]').click()
        countries = code_to_choose.find_elements_by_tag_name("li")

        for li in countries:

            if li.get_attribute("innerText") == "PL":
                li.location_once_scrolled_into_view
                li.click()
                break

        #elementToFocus = self.driver.find_element_by_xpath('//div[contains(text(), "PL")]')
        #self.driver.execute_script("arguments[0].focus();", elementToFocus)



# 7. Wprowadź numer telefonu


# 8. Wprowadź e-mail bez znaku małpa


# 9. Wprowadź hasło


# 10. Wybierz narodowość


# 11. Akceptuj politykę prywatności


# 12. Kliknij ZAREJESTRUJ SIĘ

    def tearDown(self):
        self.driver.quit()

        time.sleep(2)
