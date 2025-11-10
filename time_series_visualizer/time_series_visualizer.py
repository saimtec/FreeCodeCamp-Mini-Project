import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

def draw_line_plot():
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df = df.dropna(subset=['value'])
    lower = df['value'].quantile(0.025)
    upper = df['value'].quantile(0.975)
    df_clean = df[(df['value'] >= lower) & (df['value'] <= upper)].copy()
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df_clean.index, df_clean['value'], color='red', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.tight_layout()
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df = df.dropna(subset=['value'])
    lower = df['value'].quantile(0.025)
    upper = df['value'].quantile(0.975)
    df_clean = df[(df['value'] >= lower) & (df['value'] <= upper)].copy()
    df_clean['year'] = df_clean.index.year
    df_clean['month'] = df_clean.index.month
    grouped = df_clean.groupby(['year', 'month'])['value'].mean().unstack()
    month_order = ['January','February','March','April','May','June',
                   'July','August','September','October','November','December']
    grouped.columns = [pd.to_datetime(m, format='%m').strftime('%B') for m in grouped.columns]
    grouped = grouped[month_order]
    fig = grouped.plot(kind='bar', figsize=(12, 8)).get_figure()
    ax = fig.axes[0]
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')
    plt.tight_layout()
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df = df.dropna(subset=['value'])
    lower = df['value'].quantile(0.025)
    upper = df['value'].quantile(0.975)
    df_clean = df[(df['value'] >= lower) & (df['value'] <= upper)].copy()
    df_box = df_clean.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    df_box['month_num'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_num')
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    sns.boxplot(x='month', y='value', data=df_box, order=month_order, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    plt.tight_layout()
    fig.savefig('box_plot.png')
    return fig
