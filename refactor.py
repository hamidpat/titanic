import numpy as np
import pandas as pd


train_df = pd.read_csv("train_df.csv")
test_df = pd.read_csv("test_df.csv.csv")
combine = [train_df, test_df]


guess_ages = np.zeros((2, 3))
for df in combine:
    for i in range(0, 2):
        for j in range(0, 3):
            guess_df = df[(df['Sex'] == i) & (
                df['Pclass'] == j + 1)]['Age'].dropna()
            age_guess = guess_df.median()
            guess_ages[i, j] = int(age_guess/0.5 + 0.5) * 0.5
    for i in range(0, 2):
        for j in range(0, 3):
            df.loc[(df.Age.isnull()) & (df.Sex == i) & (
                df.Pclass == j + 1), 'Age'] = guess_ages[i, j]

    df.Age = df.Age.astype(int)
