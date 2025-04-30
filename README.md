# Домашнє завдання 2

## Тема: Жадібні алгоритми та динамічне програмування

## Завдання 1: Оптимізація черги 3D-принтера

### Файл: `task1_printer_optimization.py`

### Опис

- Пріоритети: 1 (високий) → 2 → 3
- Групування моделей відповідно до:
  - `max_volume`
  - `max_items`
- Час друку групи = максимальний `print_time` з групи
- Моделі з вищим пріоритетом друкуються раніше

### Формат результату:

```python
{
  "print_order": ["M1", "M2", "M3"],
  "total_time": 270
}
```

### Приклад запуску

python3 task1_printer_optimization.py

## Завдання 2: Оптимальне розрізання стрижня

### Частина 1 — Мемoізація

Файл: task2_rod_cutting.py

Функція:
def rod_cutting_memo(length: int, prices: List[int]) -> Dict

Повертає:

``` paython
{
  "max_profit": 12,
  "cuts": [2, 2, 1],
  "number_of_cuts": 2
}
```

Приклад запуску:
python3 task2_rod_cutting.py

### Частина 2 — Табуляція

Файл: task2_rod_cutting_tabulation.py

Функція:
def rod_cutting_table(length: int, prices: List[int]) -> Dict

Приклад запуску:
python3 task2_rod_cutting_tabulation.py

Тести:

Базовий випадок (довжина = 5)
Не потрібно різати (довжина = 3)
Всі розрізи по 1 (довжина = 4)

### Структура проєкту

goit-algo2-hw-02/
├── task1_printer_optimization.py
├── task2_rod_cutting.py
├── task2_rod_cutting_tabulation.py
├── README.md

### Автор

Катанова Леся
