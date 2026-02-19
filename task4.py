#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задача 4 (Вариант 13, №10)
Класс FibonacciSequence с методом generate(n),
генерирующим первые n чисел Фибоначчи с минимальными затратами ресурсов.
Используется инструкция yield.
"""

from typing import Generator, List
import sys


class FibonacciSequence:
    """
    Класс для генерации последовательности Фибоначчи.
    Использует генератор для экономии памяти.
    """
    
    def __init__(self):
        """Инициализация класса."""
        self._cache = {0: 0, 1: 1}  # Кэш для оптимизации рекурсивных вызовов
    
    def generate(self, n: int) -> Generator[int, None, None]:
        """
        Генерирует первые n чисел Фибоначчи.
        
        Args:
            n: Количество чисел для генерации (n >= 1)
            
        Yields:
            int: Следующее число Фибоначчи
            
        Raises:
            ValueError: Если n < 1
        """
        if n < 1:
            raise ValueError(f"n должно быть >= 1, получено {n}")
        
        a, b = 0, 1
        count = 0
        
        while count < n:
            yield a
            a, b = b, a + b
            count += 1
    
    def generate_with_index(self, n: int) -> Generator[tuple, None, None]:
        """
        Генерирует пары (индекс, число Фибоначчи).
        
        Args:
            n: Количество чисел для генерации
            
        Yields:
            tuple: (индекс, число)
        """
        for i, fib_num in enumerate(self.generate(n)):
            yield (i + 1, fib_num)
    
    def get_nth(self, n: int) -> int:
        """
        Возвращает n-е число Фибоначчи (рекурсивно с кэшированием).
        
        Args:
            n: Индекс числа (начиная с 1)
            
        Returns:
            int: n-е число Фибоначчи
        """
        if n < 1:
            raise ValueError(f"n должно быть >= 1, получено {n}")
        
        def _fib(k):
            if k in self._cache:
                return self._cache[k]
            self._cache[k] = _fib(k-1) + _fib(k-2)
            return self._cache[k]
        
        return _fib(n)
    
    def get_sequence_list(self, n: int) -> List[int]:
        """
        Возвращает список первых n чисел Фибоначчи.
        Использует генератор для создания списка.
        
        Args:
            n: Количество чисел
            
        Returns:
            List[int]: Список чисел Фибоначчи
        """
        return list(self.generate(n))
    
    def get_memory_efficient_description(self) -> str:
        """
        Возвращает описание эффективности использования памяти.
        
        Returns:
            str: Описание
        """
        return (
            "Генератор использует O(1) памяти, так как хранит только "
            "два последних числа, а не всю последовательность."
        )
    
    @staticmethod
    def calculate_golden_ratio_approximation(n: int) -> float:
        """
        Вычисляет приближение золотого сечения как отношение
        n-го и (n-1)-го чисел Фибоначчи.
        
        Args:
            n: Индекс числа (n >= 2)
            
        Returns:
            float: Приближение золотого сечения
        """
        if n < 2:
            raise ValueError("Для приближения золотого сечения нужно n >= 2")
        
        fib_seq = FibonacciSequence()
        fib_n = fib_seq.get_nth(n)
        fib_n_1 = fib_seq.get_nth(n - 1)
        
        return fib_n / fib_n_1 if fib_n_1 != 0 else float('inf')


def demonstrate_properties():
    """Демонстрирует свойства чисел Фибоначчи."""
    
    fib = FibonacciSequence()
    n = 20
    
    print(f"\nСвойства первых {n} чисел Фибоначчи:")
    print("-" * 50)
    
    # Получаем последовательность
    fib_nums = fib.get_sequence_list(n)
    
    # Выводим числа
    for i, num in enumerate(fib_nums, 1):
        print(f"  F({i:2d}) = {num:8d}", end="")
        if i % 3 == 0:
            print()
    
    print("\n\nОтношения последовательных чисел (приближение к золотому сечению):")
    print("-" * 60)
    
    for i in range(2, min(16, n)):
        ratio = fib.calculate_golden_ratio_approximation(i)
        print(f"  F({i})/F({i-1}) = {ratio:.10f}")
    
    print(f"\nЗолотое сечение φ ≈ 1.6180339887")


def main():
    """Основная функция."""
    
    print("\n" + "="*60)
    print("ЗАДАЧА 4: Генератор чисел Фибоначчи (FibonacciSequence)")
    print("="*60)
    
    # Создаем экземпляр класса
    fib = FibonacciSequence()
    
    print(f"\n{fib.get_memory_efficient_description()}")
    
    # Демонстрация 1: Базовое использование генератора
    print("\n1. Генерация первых 15 чисел Фибоначчи:")
    print("-" * 40)
    
    for i, fib_num in enumerate(fib.generate(15), 1):
        print(f"   {i:2d}. {fib_num}")
    
    # Демонстрация 2: Генерация с индексами
    print("\n2. Генерация с индексами (первые 10 чисел):")
    print("-" * 40)
    
    for index, fib_num in fib.generate_with_index(10):
        print(f"   F({index:2d}) = {fib_num}")
    
    # Демонстрация 3: Получение конкретного числа
    print("\n3. Получение конкретных чисел Фибоначчи:")
    print("-" * 40)
    
    test_indices = [1, 5, 10, 20, 30, 40]
    for idx in test_indices:
        try:
            value = fib.get_nth(idx)
            print(f"   F({idx:2d}) = {value}")
        except ValueError as e:
            print(f"   Ошибка: {e}")
    
    # Демонстрация 4: Сравнение разных способов получения последовательности
    print("\n4. Сравнение методов получения последовательности:")
    print("-" * 40)
    
    n = 10
    print(f"   Первые {n} чисел Фибоначчи:")
    print(f"   list(generate({n})) = {fib.get_sequence_list(n)}")
    
    # Демонстрация 5: Математические свойства
    demonstrate_properties()
    
    # Демонстрация 6: Интерактивный режим
    print("\n" + "-"*40)
    print("5. Интерактивный режим:")
    print("-" * 40)
    
    while True:
        try:
            user_input = input("\nСколько чисел Фибоначчи вывести? (0 для выхода): ").strip()
            
            if not user_input:
                continue
                
            n = int(user_input)
            
            if n == 0:
                break
                
            if n < 0:
                print("Ошибка: введите положительное число")
                continue
            
            print(f"\nПервые {n} чисел Фибоначчи:")
            
            # Используем генератор напрямую
            for i, fib_num in enumerate(fib.generate(n), 1):
                print(f"   {i:2d}. {fib_num}")
                
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except KeyboardInterrupt:
            print("\nВыход из программы")
            break
    
    print("\n" + "="*60)


if __name__ == "__main__":
    main()