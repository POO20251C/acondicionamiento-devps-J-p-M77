def find_max_min():
    numbers = list(map(int, input().split()))
    
    maximum = max(numbers)
    minimum = min(numbers)
    
    print(maximum, minimum)

find_max_min()