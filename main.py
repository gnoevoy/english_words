import pandas as pd
import numpy as np
import random


def get_values(df, num1, num2):
    # pick up new random values
    new_values = df.query("is_passed == False")
    new_values_lst = random.choices(new_values["value"].to_list(), k=num1)

    # update table
    df["is_passed"] = np.where(df["value"].isin(new_values_lst), True, df["is_passed"])

    # select passed values
    passed_values = df.query("is_passed == True")
    passed_values_lst = random.choices(passed_values["value"].to_list(), k=num2)

    return new_values_lst, passed_values_lst


def main():
    words = pd.read_csv("words.csv")
    phrases = pd.read_csv("phrases.csv")

    new_words, passed_words = get_values(words, 20, 10)
    new_phrases, passed_phrases = get_values(phrases, 3, 1)

    print("New words:", new_words)
    print("Passed words:", passed_words)
    print("")
    print("New phrases:", new_phrases)
    print("Passed phrases:", passed_phrases)


if __name__ == "__main__":
    main()
