import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def draw_cat_plot():
    
    df = pd.read_csv('medical_examination.csv')

    bmi = df['weight'] / ((df['height'] / 100) ** 2)
    df['overweight'] = (bmi > 25).astype(int)

    df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
    df['gluc'] = (df['gluc'] > 1).astype(int)

    #Create DataFrame for cat plot using pd.melt
    df_cat = pd.melt(df,
                     id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],
                     var_name='variable',
                     value_name='value')

    # Group and reformat the data to get counts
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    #Draw the categorical plot with seaborn
    fig = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar',
        height=5,
        aspect=1
    ).fig

    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    df = pd.read_csv('medical_examination.csv')

    bmi = df['weight'] / ((df['height'] / 100) ** 2)
    df['overweight'] = (bmi > 25).astype(int)

    df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
    df['gluc'] = (df['gluc'] > 1).astype(int)

    df_heat = df[df['ap_lo'] <= df['ap_hi']].copy()

    h_low = df_heat['height'].quantile(0.025)
    h_high = df_heat['height'].quantile(0.975)
    df_heat = df_heat[(df_heat['height'] >= h_low) & (df_heat['height'] <= h_high)]

    w_low = df_heat['weight'].quantile(0.025)
    w_high = df_heat['weight'].quantile(0.975)
    df_heat = df_heat[(df_heat['weight'] >= w_low) & (df_heat['weight'] <= w_high)]

    corr = df_heat.corr()

    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(12, 10))

    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        vmax=0.3,
        center=0,
        square=True,
        linewidths=.5,
        cbar_kws={"shrink": .5},
        ax=ax
    )
    
    fig.savefig('heatmap.png')
    return fig
