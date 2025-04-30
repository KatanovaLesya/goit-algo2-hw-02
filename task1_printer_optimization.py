from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int

@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int

def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    jobs = [PrintJob(**job) for job in print_jobs]
    printer = PrinterConstraints(**constraints)

    # Сортуємо за пріоритетом та часом
    jobs.sort(key=lambda x: (x.priority, -x.print_time))

    total_time = 0
    print_order = []
    group = []
    group_volume = 0

    for job in jobs:
        if (len(group) < printer.max_items) and (group_volume + job.volume <= printer.max_volume):
            group.append(job)
            group_volume += job.volume
        else:
            if group:
                total_time += max(j.print_time for j in group)
                print_order.extend(j.id for j in group)
            group = [job]
            group_volume = job.volume

    if group:
        total_time += max(j.print_time for j in group)
        print_order.extend(j.id for j in group)

    return {
        "print_order": print_order,
        "total_time": total_time
    }

# Тестування
def test_printing_optimization():
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
    ]
    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}
    ]
    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
    ]
    constraints = {
        "max_volume": 300,
        "max_items": 2
    }

    print("Тест 1:")
    print(optimize_printing(test1_jobs, constraints))
    print("Тест 2:")
    print(optimize_printing(test2_jobs, constraints))
    print("Тест 3:")
    print(optimize_printing(test3_jobs, constraints))

if __name__ == "__main__":
    test_printing_optimization()
