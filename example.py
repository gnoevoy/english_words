import pandas as pd

df = pd.read_csv("data.txt", header=None, names=["phrase"])
df["is_passed"] = False

df.to_csv("phrases.csv", index=False)
