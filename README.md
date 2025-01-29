Żeby program działał jak powinien, trzeba przejść do katalogu:

```path
ROOT_DIR/low_level_program/init_states
```

w którym omówię najważniejsze konfiguracje, a są nimi:

- emulatory / zaślepki urządzeń B i A, gdzie przekazywana jest:
  - ramka podana w bajtach,
  - częstotliwość wysyłania ramek,
  - przypisanie ***block_c_reserved=True***.
    Wymagane jest żeby jeden emulator urz. B i jedna zaślepka urz. A miała taką opcję wyznaczoną,
    żeby od razu po uruchomieniu programu operacja się wykonywała,
  - port do bramki (dla obiektów ***DeviceGatewayRunner*** - domyślnie dla urz. A - 5000, a urz. B - 4000) oraz ip;


- mechanizm watchdog, dla którego ustawia się w bajtach ramkę zerującą, żeby od razu po uruchomieniu programu operacja się wykonywała
  (***odczyt przesłanej jego ramki został pominięty, ponieważ wykonuje swoją pracę przez cały czas działania programu i w krótkim odstępie czasowym, zakrywając ważne logi***);


- operator dla operacji arytmetycznej, dozwolone:
  - ' + ' dodawanie (domyślnie),
  - ' - ' odejmowanie,
  - ' / ' dzielenie,
  - ' * ' mnożenie


- bramki, w tym przypadku obiektom ***DeviceGatewayRunner*** można zmienić domyślny port oraz ip (domyślnie '0.0.0.0')


Aby uruchomić serwer, należy przejść do katalogu głównego projektu, ponieważ znajduje się w nim plik 'manage.py':

```git bash
cd ROOT_DIR
```

i po tym dopiero:

```git bash
py manage.py runserver
```

Żeby projekt zaczął działać trzeba przejść do dowolnego, dostępnego adresu URL np. do głównego a jest nim: 

```url
http://localhost:8000/app
```

pozostałe dostępne adresy:

```urls
http://localhost:8000/app/device-a/state/
http://localhost:8000/app/device-b/state/
http://localhost:8000/app/block-c/state/
http://localhost:8000/app/device-b/frames-sender/
http://localhost:8000/app/edit-config/
```

***Dozwolone domeny: localhost oraz 127.0.0.1***

Interfejs aplikacji zawiera:

- odczyty stanu pracy urządzeń A i B oraz bloku C
- przesyłanie ramki / ramek dla urządzenia B
- edycję konfiguracji aplikacji - dynamiczną zmianę ramki zerującej dla mechanizmu watchdog oraz operatora arytmetycznego dla bloku C
