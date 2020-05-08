def find_smallest(arr):
    smallest = arr[0] #   <---- Для хранения наименьшего значения
    smallest_index = 0 #   <---- Для хранения индекса наименьшего значения

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []

    for in range(len(arr)):
        smallest = find_smallest(arr) # <---- Находит наименьший элемент в массиве и добавляет его в новый массив
        new_arr.append(arr.pop(smallest)) # <---- Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент

# Сортировка выбором выполняется за время O(n * n) (или n в квадрате).