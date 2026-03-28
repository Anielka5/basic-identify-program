# basic-identify-program
## spis treści:
* do czego jest ten program
* co ten program robi od strony backendu i co można zmienić
* co ma wpisać użytkownik
* wersje oprogramowania, biblioteki i ich wersje 
## do czego służy ten program
Ten program służy do sprawdzenia, czy na wysłanym zdięcie przez użytkownika jest kobieta czy mężczyzna i sprawdzenia wieku danej osoby. Dane wpisującego zapisuje albo do użytkowników, albo do oszustów. W Backendzie wytłumaczone jest działanie programu
## backend programu i zalecane zmiany
Po wywołaniu komendy i jej argumentów sprawdza, czy są jakieś załaczniki. Potem ten załącznik zapisuje w zmiennej i sprawdza płeć użytkownika. Jeżeli wiadomość o płci jest nieprzewidziana w programie, nadaje komunikat o tym, i trzeba znów wpisać komendę startu. Tak samo robi z wiekiem, podzielonym na 5 kategorii wiekowych. Gdy już bot wszystko sprawdził, to zapsuje załącznik na dysku twardym. Otwiera załącznik za pomocą biblioteki PIL i uruchamia funkcję get_class() z modelem keras, labelsami i linkiem do załączonego zdięcia (nie zPILowanego). Funkcja get_class to funkcja w pliku model.py, która wykorzystuje bilitokekę keras (tf-keras) i uprzednio wytrenowany model Teachable Machine, która identyfikuje obiekt na zdięciu i zwraca jego dane (wiek i płeć), jeżeli jego pewność jest większa niż 40%,np: Kobieta 69+ 35%, Mężczyzna 55-68 32%, Kobieta 55-68 29%,wtedy wysyła komunikat o nie rozpoznaniu zdięcia. Jeżeli model AI zdięcie rozpoznał, to program porównuje dane swoje z danymi użytkownika. Jeżeli dane się powielają, to program dodaje dane do listy users, w przeciwnym wypadku do listy oszustów.
Dodatkowo, program informuje nas w konsoli, że mamy dużo podejrzanych o oszustwo.
******* 
Zalecana jest zmiana modelu .h5, ponieważ jest to wczesna wersja modelu, która zawiera tylko identyfikację mężczyzn i wprowadzenie rozróżniania AI od prawdziwych.

