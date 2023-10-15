word = input()

vowels = ['a', 'o', 'u', 'e', 'i']

final_word = [word_new for word_new in word if word_new.lower() not in vowels]
print(''.join(final_word))
