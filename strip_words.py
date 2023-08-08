def strip_words_from_file(file_path, words_to_remove):
    with open(file_path, 'r') as file:
        content = file.read()

    # Process the content to remove the target words
    for word in words_to_remove:
        content = content.replace(word, '')

    with open(file_path, 'w') as file:
        file.write(content)

# Example usage
file_path = 'example.txt'  # Replace with the path to your text file
words_to_remove = ['example', 'word', 'another']  # List of words to remove
strip_words_from_file(file_path, words_to_remove)
