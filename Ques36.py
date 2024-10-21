def count_names(filename):
    with open(filename, 'r') as file:
        names = file.read().splitlines()
    name_count = {name: names.count(name) for name in set(names)}
    for name, count in name_count.items():
        print(f"{name}: {count}")