# Flappy Bird – Genetic AI

Flappy Bird z ptakiem sterowanym przez algorytm genetyczny. Populacja ptaków uczy się grać przez kolejne generacje — bez sieci neuronowej, tylko prosta ewolucja wag wektora decyzyjnego.

![Python](https://img.shields.io/badge/Python-3.10+-blue) ![Pygame](https://img.shields.io/badge/Pygame-2.x-green)

## Jak to działa

Każdy ptak posiada "mózg" — wektor 4 wag. W każdej klatce ptak analizuje:
- odległość pionową od środka szczeliny rury
- odległość poziomą do najbliższej rury
- aktualną prędkość pionową
- bias (stała wartość 1.0)

Iloczyn skalarny tych wejść z wagami mózgu decyduje, czy ptak skacze (`> 0.5` → skok).

Po zakończeniu generacji najlepsi osobnicy są krzyżowani i mutowani, tworząc nową populację.

## Algorytm genetyczny

| Parametr | Wartość |
|---|---|
| Rozmiar populacji | 30 |
| Selekcja | Top 6 osobników |
| Krzyżowanie | Średnia arytmetyczna dwóch rodziców |
| Mutacja | Szum gaussowski (σ = 0.5 na początku, 0.15 po nauce) |
| Elityzm | 2 najlepsze osobniki przechodzą bez zmian |

## Funkcja oceny (fitness)

Fitness = wiek ptaka (liczba klatek przeżytych), a liczba przeleconych rur zapisywana jest oddzielnie jako wynik wizualny.

## Uruchomienie

```bash
pip install pygame numpy
python main.py
```

## Menu

- **Train** – uruchamia trening nowej/wczytanej populacji
- **Best** – odtwarza najlepszego dotąd wytrenowanego ptaka
- **Exit** – wyjście

Podczas treningu można nacisnąć `M`, aby przełączyć się między trybem AI a ręcznym sterowaniem.

## Zapisywanie postępu

| Plik | Zawartość |
|---|---|
| `brain/best_brain.pkl` | Wagi najlepszego ptaka |
| `brain/population.pkl` | Cała populacja z ostatniej generacji |
| `brain/statistics.csv` | Historia wyników (generacja, best, avg) |

## Struktura projektu

```
├── main.py          # Główna pętla programu
├── genetic.py       # Algorytm genetyczny
├── trainer.py       # Symulacja jednej generacji
├── player.py        # Logika ptaka i AI
├── pipe.py          # Rury
├── menu.py          # Menu startowe
├── visualization.py # Tryb odtwarzania najlepszego ptaka
├── config.py        # Stałe (rozmiar ekranu, grawitacja itp.)
├── brain/           # Zapisane modele
└── img/             # Grafiki
```

## Wymagania

- Python 3.10+
- pygame
- numpy
