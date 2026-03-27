# basic-identify-program
## spis treści:
* do czego jest ten program
* co ten program robi od strony backendu i co można zmienić
* co ma wpisać użytkownik
* wersje oprogramowania, biblioteki i ich wersje 
## do czego służy ten program
Ten program służy do sprawdzenia, czy na wysłanym zdięcie przez użytkownika jest kobieta czy mężczyzna i sprawdzenia wieku danej osoby.
## backend programu i zalecane zmiany
Po wywołaniu komendy i jej argumentów sprawdza, czy są jakieś załaczniki. Potem ten załącznik zapisuje w zmiennej i sprawdza płeć użytkownika. Jeżeli wiadomość o płci jest nieprzewidziana w programie, nadaje komunikat o tym, i trzeba znów wpisać komendę startu. Tak samo robi z wiekiem, podzielonym na 5 kategorii wiekowych. Gdy już bot wszystko sprawdził, to zapsuje załącznik na dysku twardym. Otwiera załącznik za pomocą biblioteki PIL i uruchamia funkcję get_class() z modelem keras, labelsami i linkiem do załączonego zdięcia. Funkcja get_class
