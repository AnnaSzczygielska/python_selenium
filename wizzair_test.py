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
5. Wybierz kod kraju
6. Wprowadź numer telefonu
7. Wprowadź e-mail bez znaku małpa
8. Wprowadź hasło
9. Wybierz narodowość
10. Akceptuj politykę prywatności
11. Kliknij ZAREJESTRUJ SIĘ

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
        zaloguj_button = self.driver.find_element_by_xpath('//button[@data-test="navigation-menu-signin"]')
        zaloguj_button.click()

# 2. Wybierz REJESTRACJA
        rejestracja_button = self.driver.find_element_by_xpath('//button[contains(text(), "Rejestracja")]')
        rejestracja_button.click()

# 3. Wprowadź imię
        imie_field = self.driver.find_element_by_name('firstName')
        imie_field.send_keys("Alina")

# 4. Wprowadź nazwisko
        nazwisko_field = self.driver.find_element_by_xpath('//input[@placeholder="Nazwisko"]')
        nazwisko_field.send_keys("Lina")

# 5. Wybierz kod kraju


# 6. Wprowadź numer telefonu


# 7. Wprowadź e-mail bez znaku małpa


# 8. Wprowadź hasło


# 9. Wybierz narodowość


# 10. Akceptuj politykę prywatności


# 11. Kliknij ZAREJESTRUJ SIĘ

    def tearDown(self):
        self.driver.quit()

        time.sleep(2)

# if __name__ == '__main__':
#    unittest.main(verbosity=2)
