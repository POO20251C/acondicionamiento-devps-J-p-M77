def is_palindrome():
    text = input()
    
    cleaned_text = ''.join(text.lower().split())
    
    left = 0
    right = len(cleaned_text) - 1
    
    while left < right:
        if cleaned_text[left] != cleaned_text[right]:
            print("No")
            return
        left += 1
        right -= 1
    
    print("Si")

is_palindrome()