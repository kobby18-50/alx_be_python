number = int(input(" Enter a number to see its multiplication table:"))

i = 1

while(i < 10):
    for num in range(1,11):
        print(f"{number} * {num} = {number * num}")
        i = i + 1
    
