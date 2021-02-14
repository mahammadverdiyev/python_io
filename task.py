file_name = input("Enter file name")
if not file_name.endswith('.txt'):
    file_name += '.txt'

max_word_len = 0
line_count = 0
word_count = 0

with open(file_name, 'w') as fileObject:
    text = input('Enter some text ')
    fileObject.write(text)

with open(file_name, 'r') as fileObject:
    for line in fileObject.readlines():
        words = line.split()
        line_count += 1
        word_count += len(words)
        for word in words:
            max_word_len = max(max_word_len, len(word))
print(f'Number of lines: {line_count}')
print(f'Number of words: {word_count}')
print(f'Max word word length: {max_word_len}')
