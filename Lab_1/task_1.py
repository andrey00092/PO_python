numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

Num = len(numbers)
sum = 0
missed_element = 0

for i in range(Num):
    if numbers[i] == None:
        missed_element = i
    else:
        sum = sum + numbers[i]

average = sum/Num

numbers[missed_element] = average

print("Измененный список:", numbers)
