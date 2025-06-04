System rezerwacji biletów na wydarzenia

Spis treści
Opis projektu
Funkcjonalności
Uruchomienie
Struktura projektu

Opis projektu
Aplikacja webowa służąca do zarządzania wydarzeniami z wykorzystaniem wzorca MVC. Pozwala dodawać, edytować i usuwać wydarzenia.

Funkcjonalności
- Dodawanie wydarzeń (nazwa, data, liczba miejsc)
- Edycja wydarzeń
- Usuwanie wydarzeń
- Przeglądanie listy wydarzeń

Uruchomienie

1. Zainstaluj zależności:
bash
pip install -r requirements.txt


2. Uruchom aplikację:
bash
python run.py


3. Otwórz w przeglądarce:

http://127.0.0.1:5000

Kod źródłowy:

run.py – główny plik uruchamiający aplikację Flask.

requirements.txt – lista zależności do zainstalowania (np. Flask).

README.md – dokumentacja projektu (opis, funkcjonalności, uruchamianie).

data/sample_data.json – przykładowe dane wejściowe (wydarzenia).

app/ – główna logika aplikacji (MVC)
__init__.py – tworzy i konfiguruje aplikację Flask.

models.py – logika danych (dodawanie, edycja, usuwanie wydarzeń).

controllers.py – logika przetwarzająca dane z formularzy i wywołująca model.

views.py – definicje tras (routing) i interakcje z widokami HTML.

app/templates/ – pliki HTML (widoki)
layout.html – szablon bazowy (nagłówek i struktura strony).

index.html – lista wydarzeń.

add_event.html – formularz dodawania wydarzenia.

edit_event.html – formularz edycji wydarzenia.

Dane przykładowe
W folderze `data/` znajduje się plik `sample_data.json` z przykładowymi wydarzeniami.
{
  "name": "Koncert rockowy",
  "date": "2025-06-20",
  "seats": 100
}
