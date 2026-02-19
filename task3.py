#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задача 3 (Вариант 13, №9, N=12)
Класс Movie.
У Movie есть название и расписание, по каким дням он идёт в кинотеатрах.
Расписание хранится периодами дат.
Реализовать метод schedule, генерирующий дни показа фильма.
"""

from datetime import datetime, timedelta
from typing import List, Tuple, Generator
import calendar


class Movie:
    """
    Класс фильма с расписанием показов.
    """
    
    def __init__(self, title: str):
        """
        Инициализация фильма.
        
        Args:
            title: Название фильма
        """
        self.title = title
        self.schedule_periods: List[Tuple[datetime, datetime]] = []
    
    def add_schedule_period(self, start_date: datetime, end_date: datetime) -> None:
        """
        Добавляет период показа фильма.
        
        Args:
            start_date: Дата начала показа
            end_date: Дата окончания показа
            
        Raises:
            ValueError: Если дата начала позже даты окончания
        """
        if start_date > end_date:
            raise ValueError(f"Дата начала {start_date} позже даты окончания {end_date}")
        
        self.schedule_periods.append((start_date, end_date))
        # Сортируем периоды по дате начала
        self.schedule_periods.sort(key=lambda x: x[0])
    
    def schedule(self) -> Generator[datetime, None, None]:
        """
        Генератор, возвращающий все дни показа фильма по порядку.
        
        Yields:
            datetime: Следующая дата показа
        """
        for start_date, end_date in self.schedule_periods:
            current_date = start_date
            while current_date <= end_date:
                yield current_date
                current_date += timedelta(days=1)
    
    def get_schedule_summary(self) -> str:
        """
        Возвращает текстовое описание расписания.
        
        Returns:
            str: Описание расписания
        """
        if not self.schedule_periods:
            return "Нет запланированных показов"
        
        summary = []
        for i, (start, end) in enumerate(self.schedule_periods, 1):
            days_count = (end - start).days + 1
            summary.append(
                f"Период {i}: {start.strftime('%d.%m.%Y')} - {end.strftime('%d.%m.%Y')} "
                f"({days_count} {self._pluralize_days(days_count)})"
            )
        return "\n".join(summary)
    
    @staticmethod
    def _pluralize_days(n: int) -> str:
        """Склонение слова 'день'."""
        if n % 10 == 1 and n % 100 != 11:
            return "день"
        elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
            return "дня"
        else:
            return "дней"
    
    def __str__(self) -> str:
        """Строковое представление фильма."""
        periods_count = len(self.schedule_periods)
        if periods_count == 0:
            periods_str = "нет периодов"
        else:
            total_days = sum((end - start).days + 1 for start, end in self.schedule_periods)
            periods_str = f"{periods_count} {self._pluralize_periods(periods_count)}, всего {total_days} {self._pluralize_days(total_days)}"
        
        return f"Фильм '{self.title}' ({periods_str})"
    
    @staticmethod
    def _pluralize_periods(n: int) -> str:
        """Склонение слова 'период'."""
        if n % 10 == 1 and n % 100 != 11:
            return "период"
        elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
            return "периода"
        else:
            return "периодов"


def create_demo_schedule() -> Movie:
    """
    Создает демонстрационный фильм с расписанием.
    
    Returns:
        Movie: Фильм с тестовым расписанием
    """
    movie = Movie("Аватар: Путь воды")
    
    # Период 1: новогодние праздники
    movie.add_schedule_period(
        datetime(2024, 12, 25),
        datetime(2025, 1, 8)
    )
    
    # Период 2: февральские праздники
    movie.add_schedule_period(
        datetime(2025, 2, 20),
        datetime(2025, 2, 25)
    )
    
    # Период 3: мартовские праздники
    movie.add_schedule_period(
        datetime(2025, 3, 6),
        datetime(2025, 3, 10)
    )
    
    return movie


def demonstrate_with_n_months(n: int = 12):
    """
    Демонстрирует работу генератора для N месяцев.
    
    Args:
        n: Количество месяцев для демонстрации (по варианту N=12)
    """
    print(f"\n--- Демонстрация для {n} месяцев ---")
    
    # Создаем фильм с расписанием на год
    movie = Movie("Годовой киномарафон")
    
    # Добавляем периоды на каждый месяц
    current_year = datetime.now().year
    
    for month in range(1, n + 1):
        # Последний день месяца
        last_day = calendar.monthrange(current_year, month)[1]
        
        # Показы в середине месяца (с 10 по 15 число)
        start_date = datetime(current_year, month, 10)
        end_date = datetime(current_year, month, 15)
        
        movie.add_schedule_period(start_date, end_date)
    
    print(f"Создан {movie}")
    print(movie.get_schedule_summary())
    
    # Выводим первые несколько дат из генератора
    print(f"\nПервые 20 дат показа:")
    schedule_gen = movie.schedule()
    for i in range(20):
        try:
            date = next(schedule_gen)
            print(f"  {i+1:2d}. {date.strftime('%d.%m.%Y')}")
        except StopIteration:
            print("  ... конец расписания")
            break


def main():
    """Основная функция."""
    
    print("\n" + "="*60)
    print("ЗАДАЧА 3: Класс Movie с генератором расписания")
    print(f"Вариант 13, N=12")
    print("="*60)
    
    # Демонстрация 1: Базовый пример из задания
    print("\n1. Базовый пример из задания:")
    movie1 = Movie("Дюна 2")
    movie1.add_schedule_period(datetime(2024, 11, 1), datetime(2024, 11, 7))
    movie1.add_schedule_period(datetime(2024, 12, 15), datetime(2024, 12, 31))
    
    print(str(movie1))
    print("\nРасписание показов:")
    for i, date in enumerate(movie1.schedule(), 1):
        print(f"  {i:2d}. {date.strftime('%d.%m.%Y')}")
    
    # Демонстрация 2: Более сложный пример
    print("\n" + "-"*40)
    print("2. Демонстрационный фильм с несколькими периодами:")
    movie2 = create_demo_schedule()
    print(str(movie2))
    print("\nДетальное расписание:")
    print(movie2.get_schedule_summary())
    
    print("\nПервые 15 дат показа:")
    for i, date in enumerate(movie2.schedule()):
        if i >= 15:
            break
        print(f"  {i+1:2d}. {date.strftime('%d.%m.%Y')} ({calendar.day_name[date.weekday()]})")
    
    # Демонстрация 3: Для N=12 месяцев
    print("\n" + "-"*40)
    demonstrate_with_n_months(12)
    
    print("\n" + "="*60)


if __name__ == "__main__":
    main()