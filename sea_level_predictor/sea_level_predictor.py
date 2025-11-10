import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    fig, ax = plt.subplots(figsize=(10,6))
    ax.scatter(x, y, color='blue', s=10)

    # First line of best fit for all data
    slope1, intercept1, _, _, _ = linregress(x, y)
    predicted_all = slope1 * x + intercept1
    ax.plot(x, predicted_all, color='red')

    # Extend to year 2050
    x_extended = pd.Series(range(x.min(), 2051))
    y_extended_all = slope1 * x_extended + intercept1
    ax.plot(x_extended, y_extended_all, color='red')

    # Second line of best fit from year 2000 onward
    df_recent = df[df['Year'] >= 2000]
    x2 = df_recent['Year']
    y2 = df_recent['CSIRO Adjusted Sea Level']
    slope2, intercept2, _, _, _ = linregress(x2, y2)
    predicted_recent = slope2 * x2 + intercept2
    ax.plot(x2, predicted_recent, color='green')

    x_extended2 = pd.Series(range(2000, 2051))
    y_extended_recent = slope2 * x_extended2 + intercept2
    ax.plot(x_extended2, y_extended_recent, color='green')

    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    plt.tight_layout()
    fig.savefig('sea_level_plot.png')
    return fig
