user_sentence = str(input("Enter a sentence: "))
clean_sentence = user_sentence.lower().replace(" "," ")
print(clean_sentence)
reversed_sentence = clean_sentence[::-1]
print(reversed_sentence)
is_palindrome = clean_sentence == reversed_sentence
print(f"The is palindrome: {is_palindrome}")





