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
# Wejść na stronę https://wizzair.com/pl-pl#/
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://wizzair.com/pl-pl#/")
        self.driver.maximize_window()

    def test_bledny_email(self):
# Kroki:
# 1. Kliknij w prawym górnym rogu ZALOGUJ SIĘ
        zaloguj_button = self.driver.find_element_by_xpath(//button[@data-test="navigation-menu-signin"])
        zaloguj_button.click()

# 2. Wybierz REJESTRACJA

    def tearDown(self):
        self.driver.quit()
