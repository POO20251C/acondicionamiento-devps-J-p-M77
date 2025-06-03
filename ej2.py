def count_vowels():
    text = input().lower()
    count = 0
    for char in text:
        if char in 'aeiou':
            count += 1
    print(count)

count_vowels()