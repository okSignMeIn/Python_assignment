def count_word_frequency(file_path):
    word_frequency = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                # Remove any punctuation and convert to lowercase
                word = word.strip('.,!?()[]{}\'"').lower()
                if word:
                    word_frequency[word] = word_frequency.get(word, 0) + 1

    return word_frequency

def top_5_words(word_frequency):
    return sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)[:5]

def main():
    file_path = '1/text_file.txt'  # Replace 'sample.txt' with the path to your text file
    
    word_frequency = count_word_frequency(file_path)
    top_words = top_5_words(word_frequency)

    print("Top 5 most frequently occurring words:")
    for word, frequency in top_words:
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    main()
