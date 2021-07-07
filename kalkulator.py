import logging
logging.basicConfig(level=logging.DEBUG)
number1 = float(input("Wpisz pierwszą liczbę:  "))
number2 = float(input("Wpisz drugą liczbę:  "))

zadanie = input("Wybierz operację podając cyfrę:\n"
                "1. Dodawanie \n"
                "2. Odejmowanie\n"
                "3. Mnożenie\n"
                "4. Dzielenie\n")

if zadanie == "1":
    logging.critical( "wynik: %s" % (number1 + number2))
elif zadanie == "2":
    logging.info("wynik : ", number1 - number2)
elif zadanie == "3":
    logging.debug("wynik : ", number1 * number2)
elif zadanie == "4":
    logging.debug("wynik to : ", number1 / number2)
else:
    logging.debug("proszę wybierz działanie z listy")
