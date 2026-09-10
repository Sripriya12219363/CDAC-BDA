def main():
    sentence = input("Enter the sentence:")
    char_count = len(sentence)
    print(char_count)
    word_count = len(sentence.split(" "))
    print(word_count)
main()