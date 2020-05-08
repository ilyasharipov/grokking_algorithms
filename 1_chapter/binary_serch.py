from math import floor
#Бинарный поиск
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binary_serch(coll, num):
  low = 0 #low и high - это границы списка
  high = len(coll) -1

  while low <= high:
    mid = floor((low + high) / 2) # если значение не чётно, окр. в меньшую сторону
    #print(mid)
    guess = coll[mid]
    if guess == num:
      print(mid)
      return mid # значение(index) найдено
    elif guess > num:
      high = mid - 1
    else:
      low = mid + 1
    #print(guess)
  return None

binary_serch(numbers, 10)

#Бинарный поиск выполняется за время O(log n).