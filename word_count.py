def count_words():
    try:
        with open("Read File.txt", "r") as file:
            content = file.read()
            words = content.split()
            print("Number of words:", len(words))

    except FileNotFoundError:
        print("File not found.")
