import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight']/(df['height']/100)**2>25).astype(int)


# 3
df['gluc'] = (df['gluc']>1).astype(int)
df['cholesterol'] = (df['cholesterol']>1).astype(int)
# 4
def draw_cat_plot():
    # 5
    #df_cat = df[['active','alco','cholesterol','gluc','overweight','smoke','cardio']]
    #value_counts = df_cat.apply(lambda col: col.value_counts()).T.fillna(0)
    #value_counts.columns = ['0', '1']
    #value_counts = value_counts.reset_index().melt(id_vars='index', var_name='Value', value_name='Count')
    #value_counts.rename(columns={'index': 'Condition'}, inplace=True)
    #plt.title('Cardio = 0')

    # Plot
    #fig = sns.barplot(data=value_counts, x='Condition', y='Count', hue='Value')
    # 6
    df_cat = df[['active','alco','cholesterol','gluc','overweight','smoke','cardio']]
    df_melted = df_cat.melt(id_vars='cardio', var_name='Condition', value_name='Value')
    counts = df_melted.groupby(['cardio', 'Condition', 'Value']).size().reset_index(name='total')
    

    # 7



    # 8
    fig = sns.catplot(data=counts,kind='bar', x='Condition', y='total', hue='Value',col='cardio')


    # 9
    plt.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[df['ap_lo']<=df['ap_hi']]
    df_heat = df_heat[df_heat['height'] >= df_heat['height'].quantile(0.025)]
    df_heat = df_heat[df_heat['height'] <= df_heat['height'].quantile(0.975)]
    df_heat = df_heat[df_heat['weight'] >= df_heat['weight'].quantile(0.025)]
    df_heat = df_heat[df_heat['weight'] <= df_heat['weight'].quantile(0.975)]
    # 12
    corr = df_heat.corr()
    plt.clf()
    # 13
    mask = mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    #fig, ax = sns.heatmap(corr,annot=True)
    fig = sns.heatmap(corr,mask=mask,annot=True,fmt=".2f")
    # 15



    # 16
    plt.savefig('heatmap.png')
    return fig
