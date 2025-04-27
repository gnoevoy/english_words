import pandas as pd
import numpy as np
import random


def get_new_words(df):
    num = 20
    new_words = df.query("is_passed == False")
    lst = new_words["word"].to_list()
    res = random.choices(lst, k=num)
    return res


def get_passed_words(df, lst):
    # update table
    df["is_passed"] = np.where(df["word"].isin(lst), True, df["is_passed"])

    num = 10
    new_words = df.query("is_passed == True")
    lst = new_words["word"].to_list()
    res = random.choices(lst, k=num)
    return res


def main():
    df = pd.read_csv("words.csv")
    new_words = get_new_words(df)
    passed_words = get_passed_words(df, new_words)

    print("New words:", new_words)
    print("Passed words:", passed_words)


if __name__ == "__main__":
    main()
