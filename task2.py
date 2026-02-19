#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задача 2 (Вариант 13, №6)
Класс CyclicTupleIterator.
Итератор должен итерировать по итерируемому объекту tuple,
и когда достигнет последнего элемента, начинать сначала.
"""

from typing import Tuple, Any, Iterator


class CyclicTupleIterator:
    """
    Циклический итератор для кортежа.
    При достижении конца кортежа начинает итерацию сначала.
    
    Реализует протокол итератора Python (методы __iter__ и __next__).
    """
    
    def __init__(self, data: Tuple[Any, ...]):
        """
        Инициализация итератора.
        
        Args:
            data: Кортеж для итерации
            
        Raises:
            TypeError: Если data не является кортежем
        """
        if not isinstance(data, tuple):
            raise TypeError(f"Ожидается кортеж, получен {type(data).__name__}")
        
        self.data = data
        self.index = 0
        
    def __iter__(self) -> Iterator:
        """
        Возвращает итератор (сам объект).
        Необходим для использования в циклах for.
        
        Returns:
            Iterator: Ссылка на себя
        """
        return self
    
    def __next__(self) -> Any:
        """
        Возвращает следующий элемент кортежа.
        При достижении конца начинает сначала.
        
        Returns:
            Any: Следующий элемент кортежа
            
        Raises:
            StopIteration: Если кортеж пуст
        """
        if not self.data:
            raise StopIteration("Кортеж пуст")
        
        # Получаем текущий элемент
        result = self.data[self.index]
        
        # Обновляем индекс для следующего вызова
        self.index += 1
        
        # Если дошли до конца, начинаем сначала
        if self.index >= len(self.data):
            self.index = 0
            
        return result
    
    def reset(self) -> None:
        """Сбрасывает итератор в начало."""
        self.index = 0
    
    def get_current_index(self) -> int:
        """
        Возвращает текущий индекс итератора.
        
        Returns:
            int: Текущий индекс
        """
        return self.index


def demonstrate_iterator():
    """Демонстрирует работу циклического итератора."""
    
    print("\n" + "="*60)
    print("ЗАДАЧА 2: Циклический итератор для кортежа (CyclicTupleIterator)")
    print("="*60)
    
    # Тестовые данные
    test_tuples = [
        (1, 2, 3, 4, 5),
        ('a', 'b', 'c'),
        (True, False, None, 42),
        (),
        (3.14, 2.71, 1.41)
    ]
    
    for i, tpl in enumerate(test_tuples, 1):
        print(f"\n--- Тест {i}: {tpl} ---")
        
        try:
            # Создаем итератор
            cyclic_iter = CyclicTupleIterator(tpl)
            
            print(f"Выводим элементы в 2 цикла:")
            
            # Выводим элементы в 2 полных цикла
            for j in range(len(tpl) * 2):
                if j < len(tpl):
                    cycle = 1
                else:
                    cycle = 2
                    
                element = next(cyclic_iter)
                print(f"  Цикл {cycle}, элемент {j % len(tpl) + 1}: {element}")
                
        except StopIteration as e:
            print(f"  Ошибка: {e}")
        except TypeError as e:
            print(f"  Ошибка: {e}")
    
    print("\n" + "="*60)


def interactive_mode():
    """Интерактивный режим для пользовательского ввода."""
    
    print("\nИНТЕРАКТИВНЫЙ РЕЖИМ")
    print("-"*40)
    
    while True:
        try:
            # Получаем ввод от пользователя
            user_input = input("\nВведите элементы кортежа через пробел (или 'exit' для выхода): ").strip()
            
            if user_input.lower() == 'exit':
                break
            
            if not user_input:
                print("Ошибка: введите хотя бы один элемент")
                continue
            
            # Преобразуем ввод в кортеж
            items = user_input.split()
            
            # Пробуем преобразовать в числа, где возможно
            processed_items = []
            for item in items:
                try:
                    if '.' in item:
                        processed_items.append(float(item))
                    else:
                        processed_items.append(int(item))
                except ValueError:
                    processed_items.append(item)
            
            tpl = tuple(processed_items)
            
            print(f"Создан кортеж: {tpl}")
            
            # Создаем итератор
            cyclic_iter = CyclicTupleIterator(tpl)
            
            # Запрашиваем количество элементов для вывода
            n = int(input("Сколько элементов вывести? (целое число): "))
            
            print(f"\nРезультат (циклический вывод {n} элементов):")
            for i in range(n):
                element = next(cyclic_iter)
                print(f"  Элемент {i+1}: {element}")
                
        except ValueError as e:
            print(f"Ошибка ввода числа: {e}")
        except KeyboardInterrupt:
            print("\nВыход из программы")
            break
        except Exception as e:
            print(f"Ошибка: {e}")


def main():
    """Основная функция."""
    
    demonstrate_iterator()
    
    # Спрашиваем, хочет ли пользователь интерактивный режим
    choice = input("\nХотите протестировать свой кортеж? (y/n): ").strip().lower()
    if choice == 'y' or choice == 'yes':
        interactive_mode()
    
    print("\n" + "="*60)


if __name__ == "__main__":
    main()