#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задача 1 (Вариант 13, №1)
Работа со списком. Пользователь вводит список.
Реализовать:
1. Свою функцию custom_any, проверяющую наличие хотя бы одного положительного числа
2. С помощью встроенной функции all проверить, состоят ли все элементы только из чисел
3. Отсортировать список с помощью встроенной функции sorted
"""

from typing import List, Any


def custom_any(iterable) -> bool:
    """
    Собственная реализация функции any.
    Проверяет, содержит ли итерируемый объект хотя бы один истинный элемент.
    
    Args:
        iterable: Итерируемый объект для проверки
        
    Returns:
        bool: True, если хотя бы один элемент истинный, иначе False
    """
    for element in iterable:
        if element:
            return True
    return False


def has_positive_numbers(numbers: List[Any]) -> bool:
    """
    Проверяет, содержит ли список хотя бы одно положительное число.
    Нечисловые элементы игнорируются (считаются ложными).
    
    Args:
        numbers: Список для проверки
        
    Returns:
        bool: True, если есть хотя бы одно положительное число
    """
    # Генератор, который возвращает True для положительных чисел
    positive_checks = (isinstance(x, (int, float)) and x > 0 for x in numbers)
    return custom_any(positive_checks)


def are_all_numbers(elements: List[Any]) -> bool:
    """
    Проверяет, состоят ли все элементы списка только из чисел.
    Использует встроенную функцию all.
    
    Args:
        elements: Список для проверки
        
    Returns:
        bool: True, если все элементы являются числами
    """
    return all(isinstance(x, (int, float)) for x in elements)


def safe_sort(items: List[Any]) -> List[Any]:
    """
    Безопасная сортировка списка с разнородными элементами.
    Числа сортируются по значению, строки - по алфавиту.
    
    Args:
        items: Список для сортировки
        
    Returns:
        List[Any]: Отсортированный список
    """
    # Разделяем числа и строки
    numbers = [x for x in items if isinstance(x, (int, float))]
    strings = [x for x in items if isinstance(x, str)]
    
    # Сортируем каждую группу
    numbers.sort()
    strings.sort()
    
    # Объединяем (сначала числа, потом строки)
    return numbers + strings


def get_user_input() -> List[Any]:
    """
    Получает список от пользователя.
    Поддерживает ввод через пробел.
    
    Returns:
        List[Any]: Список введенных значений
    """
    print("\n" + "="*60)
    print("ЗАДАЧА 1: Работа со списком")
    print("="*60)
    
    while True:
        try:
            user_input = input("\nВведите элементы списка через пробел: ").strip()
            
            if not user_input:
                print("Ошибка: список не может быть пустым.")
                continue
            
            # Разделяем по пробелам
            items = user_input.split()
            
            # Преобразуем строки в числа, где это возможно
            result = []
            for item in items:
                try:
                    # Пробуем преобразовать в число
                    if '.' in item:
                        result.append(float(item))
                    else:
                        result.append(int(item))
                except ValueError:
                    # Если не число, оставляем как строку
                    result.append(item)
            
            return result
            
        except Exception as e:
            print(f"Ошибка ввода: {e}. Попробуйте снова.")


def main():
    """Основная функция программы."""
    
    # Получаем список от пользователя
    user_list = get_user_input()
    
    print(f"\nВведенный список: {user_list}")
    print(f"Типы элементов: {[type(x).__name__ for x in user_list]}")
    
    print("\n" + "-"*40)
    print("РЕЗУЛЬТАТЫ:")
    print("-"*40)
    
    # 1. Проверка наличия положительных чисел с custom_any
    has_positive = has_positive_numbers(user_list)
    print(f"1. Есть ли положительные числа? {has_positive}")
    
    # Показываем, какие элементы положительные
    if has_positive:
        pos_numbers = [x for x in user_list if isinstance(x, (int, float)) and x > 0]
        print(f"   Положительные числа: {pos_numbers}")
    
    # 2. Проверка, все ли элементы - числа с all
    all_numbers = are_all_numbers(user_list)
    print(f"2. Все элементы являются числами? {all_numbers}")
    
    if not all_numbers:
        non_numbers = [x for x in user_list if not isinstance(x, (int, float))]
        print(f"   Нечисловые элементы: {non_numbers}")
    
    # 3. Сортировка списка
    sorted_list = safe_sort(user_list.copy())
    print(f"3. Отсортированный список: {sorted_list}")
    
    print("\n" + "="*60)


if __name__ == "__main__":
    main()