import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_count(df: pd.DataFrame, column: str) -> None:
    plt.figure(figsize=(20, 10))
    fig = sns.countplot(data=df, x=column,
                        order=df[column].value_counts().index)
    fig.set_xticklabels(fig.get_xticklabels(), rotation=90, horizontalalignment='right')
    plt.title(f'Distribution of {column}', size=20, fontweight='bold')
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel(column, fontsize=20)
    plt.ylabel('Absolute frequencies', fontsize=20)
    for i in range(len(df[column].value_counts())):
        fig.text(i, (df[column].value_counts().values[i]), str('{:.1f}%'.format(100 * df[column].value_counts().values[i] / len(df[column]))),
                 fontdict=dict(color='black', fontsize=30), horizontalalignment='center')