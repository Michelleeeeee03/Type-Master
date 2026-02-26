import random
words = ["Pneumonoultramicroscopicsilicovolcanoconiosis",
         "Supercalifragilisticexpialidocious",
         "Compassionate", "Enthusiastic", "Connoisseur",
         "Questionnaire", "Hello", "Yellow",
         "Sushi", "Nice", "Yeah", "The", "One",
         "Two", "Easy"]
random.shuffle(words)

correct = 0
wrong = 0

print("\nWelcome to the Typing Master Game!")
print("\nType the given word correctly to score points and win.")
for i in range(len(words)):
    print("\n")
    print(words[i])
    answer = input("\nType the given word correctly: ")
    if answer == words[i]:
        print("\nCorrect")
        correct += 1
    else:
        print ("\nIncorrect")
        wrong += 1

total_words = correct + wrong
correct_words_percent = (correct/total_words) * 100
wrong_words_percent = (wrong/total_words) * 100

total_words = correct + wrong
correct_words_percent = (correct/total_words) * 100
wrong_words_percent = (wrong/total_words) * 100