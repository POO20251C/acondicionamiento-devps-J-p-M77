def reverse_list():
    numbers = input().split()

    reversed_numbers = numbers[-1::-1]
    
    print(' '.join(reversed_numbers))

reverse_list()