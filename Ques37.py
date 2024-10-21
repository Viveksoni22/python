def remove_newlines(filename):
    with open(filename, 'r') as file:
        content = file.read().replace('\n', '')
    with open(filename, 'w') as file:
        file.write(content)