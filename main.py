import random


def get_words():
    with open("words.txt", "r") as f:
        data = f.read()
        words = [word for word in data.splitlines()]
    return words


def select_words(n, lst):
    with open("source.txt", "r") as f:
        data = f.read()
        words = [word for word in data.splitlines() if word not in lst]
        random_words = random.sample(words, n)
    return random_words


def add_new_words(lst):
    with open("words.txt", "a") as f:
        for word in lst:
            f.write(word + "\n")


def main():
    words = get_words()
    selected_words = select_words(10, words)
    print(f"Selected words: {selected_words}")
    add_new_words(selected_words)


if __name__ == "__main__":
    main()
