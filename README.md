# <h1 align='center'>Игры разума</h1>

### Hexlet tests and linter status, Maintainability Badge

[![Actions Status](https://github.com/Maksim-Uteev/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Maksim-Uteev/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/ac77e105adbde945526a/maintainability)](https://codeclimate.com/github/Maksim-Uteev/python-project-49/maintainability)

## Описание проекта

«Игры разума» — набор из пяти консольных игр, построенных по принципу популярных мобильных приложений для прокачки мозга. Каждая игра задает вопросы, на которые нужно дать правильные ответы. После трех правильных ответов считается, что игра пройдена. Неправильные ответы завершают игру и предлагают пройти её заново.

## Установка проекта

1. Клонировать репозиторий:

   ```
   git clone https://github.com/Maksim-Uteev/python-project-49.git
   ```

2. Установить пакет:

   ```
   make package-install
   ```

## Игра: «Проверка на чётность»

Суть игры в следующем: пользователю показывается случайное число. И ему нужно ответить yes, если число чётное или no — если нечётное.

Команда для запуска игры:

```
brain-even
```

Пример игры:

[![asciicast](https://asciinema.org/a/385LIVZFnQrwn4k5PXfpNhuUx.svg)](https://asciinema.org/a/385LIVZFnQrwn4k5PXfpNhuUx)

## Игра: «Калькулятор»

Суть игры в следующем: пользователю показывается случайное математическое выражение, например, 35 + 16, которое нужно вычислить и записать правильный ответ.

Команда для запуска игры:

```
brain-calc
```

Пример игры:

[![asciicast](https://asciinema.org/a/yHU8hc0PbRKWcrHwwLs9RPIBw.svg)](https://asciinema.org/a/yHU8hc0PbRKWcrHwwLs9RPIBw)

## Игра «НОД»

Суть игры в следующем: пользователю показывается два случайных числа, например, 25 50. Пользователь должен вычислить и ввести наибольший общий делитель этих чисел.

Команда для запуска игры:

```
brain-gcd
```

Пример игры:

[![asciicast](https://asciinema.org/a/oPMvhqk2X1F90btPsJUqIvIFg.svg)](https://asciinema.org/a/oPMvhqk2X1F90btPsJUqIvIFg)

## Игра «Арифметическая прогрессия»

Пользователь видит ряд чисел, который образует арифметическую прогрессию. Любое число из последовательности изменяется двумя точками, например, 5 .. 9. Пользователь должен определить это число.

Команда для запуска игры:

```
brain-progression
```

Пример игры:

[![asciicast](https://asciinema.org/a/6frKWUXQYesKZZ0k8TEMm9bGK.svg)](https://asciinema.org/a/6frKWUXQYesKZZ0k8TEMm9bGK)

## Игра «Простое ли число?»

Суть игры в следующем: пользователю показывается случайное число. И ему нужно ответить yes, если число простое или no — если число не является простым.

Команда для запуска игры:

```
brain-prime
```

Пример игры:

[![asciicast](https://asciinema.org/a/GyRMwZzzRdIJamtBL41Cex0ij.svg)](https://asciinema.org/a/GyRMwZzzRdIJamtBL41Cex0ij)
