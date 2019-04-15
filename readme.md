## Testy w języku python, przy użyciu biblioteki selenium.

### wizzair_test.py  
Test rejestracji nowego użytkownika na stronie [https://wizzair.com/pl-pl#/](https://wizzair.com/pl-pl#/)

Testowane przypadki testowe:

* I Rejestracja z błędnie wprowadzonym adresem e-mail.

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

* II Rejestracja z błędnym numerem telefonu

Warunki wstępne:
Wejść na stronę https://wizzair.com/pl-pl#/

Kroki:
1. Kliknij w prawym górnym rogu ZALOGUJ SIĘ
2. Wybierz REJESTRACJA
3. Wprowadź imię
4. Wprowadź nazwisko
5. Wybierz kod kraju
6. Wprowadź numer telefonu składający się tylko z jednej cyfry
7. Wprowadź e-mail
8. Wprowadź hasło
9. Wybierz narodowość
10. Akceptuj politykę prywatności
11. Kliknij ZAREJESTRUJ SIĘ

Oczekiwany resultat:
System wyświetla informację o błędnie wprowadzonym numerze telefonu.
