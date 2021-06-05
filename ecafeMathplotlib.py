import matplotlib.pyplot as plt
from numpy.lib.arraypad import pad
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy import create_engine

# Access database
engine = sqlalchemy.create_engine(
    'mysql+pymysql://root:@localhost:3306/tupc_ecafe')

# Get table
data = pd.read_sql_table("ordered_items", engine)

# Get specific columns from table
item = pd.read_sql_table("ordered_items", engine, columns=[
                         'item', 'quantity_sold'])
itemName = pd.read_sql_table("ordered_items", engine, columns=[
                         'item'])
date = pd.read_sql_table("ordered_items", engine, columns=['date_current',
                         'hourly_sales', 'quantity_sold'])
day = pd.read_sql_table("ordered_items", engine, columns=[
                         'date_current'])
hourly = pd.read_sql_table("ordered_items", engine, columns=[
                         'hourly_sales'])
# hourlySold = pd.read_sql_table("ordered_items", engine, columns=['quantity_sold'])

dateGroup = date.groupby(['date_current','hourly_sales'])['quantity_sold'].sum()

# Group data under 'item' column
# Sum data in 'quantity_sold' column
mergedItem = data.groupby('item')['quantity_sold'].sum()

# BAR GRAPH ACTIVE HOURS
def activeTime():
    
    df = pd.DataFrame(data[['date_current', 'hourly_sales', 'quantity_sold']])
    df_pivot = pd.pivot_table(
        df, 
        values="quantity_sold",
        index="date_current",
        columns="hourly_sales", 
        aggfunc=np.sum,
        fill_value=0,
    )

    print(dateGroup)
    ax = df_pivot.plot(kind="bar")
    fig = ax.get_figure()
    fig.set_size_inches(10, 6)
    ax.set_title('Most active order time of a day', fontsize='18', fontweight='bold', color ='grey')
    ax.set_xlabel("Date", fontsize='14', fontweight='bold', color ='grey')
    ax.set_ylabel("Total item sold", fontsize='14', fontweight='bold', color ='grey')
    ax.grid(b = True, color ='grey',
            linestyle ='-.', linewidth = 0.5,
            alpha = 0.2)
    ax.xaxis.set_ticks_position('none')
    plt.legend(title="Hour", fontsize='small', fancybox=True)
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

#BAR GRAPH PER ITEM SOLD
def totalItemSold():


    itemSold = {
            'item': np.unique(np.concatenate(np.array(itemName))),
            'quantity' : mergedItem.to_numpy()
    }

    df3 = pd.DataFrame.from_dict(itemSold)
    ascending = df3.sort_values(by=['quantity'],ascending=False)

    print(df3)

    fig1, ax = plt.subplots(figsize =(10, 6))

    ax.set_title('Top selling items', fontsize='18', fontweight='bold', color ='grey')
    ax.set_ylabel('Items', fontsize='14', fontweight='bold', color ='grey')
    ax.set_xlabel('Quantity sold', fontsize='14', fontweight='bold', color ='grey')

    ax.grid(b = True, color ='grey',
            linestyle ='-.', linewidth = 0.5,
            alpha = 0.2)

    ax.invert_yaxis()

    ax.xaxis.set_ticks_position('none')

    ax.xaxis.set_tick_params(pad = 5)
    ax.yaxis.set_tick_params(pad = 10)

    ax.set_xlim(0, df3.quantity.max() * 1.2)

    ax.barh(ascending.item, ascending.quantity, color="coral")

    for Y,X in enumerate(ascending.quantity):
            ax.annotate("{:.1f}%".format(X * 100/np.sum(ascending.quantity)), xy=(X,Y), color='grey', fontsize='10', va='center')

    plt.tight_layout()
    plt.show()

def totalItemSoldInvert():
    

    itemSold = {
            'item': np.unique(np.concatenate(np.array(itemName))),
            'quantity' : mergedItem.to_numpy()
    }

    df3 = pd.DataFrame.from_dict(itemSold)
    ascending = df3.sort_values(by=['quantity'],ascending=False)

    print(df3)

    fig1, ax = plt.subplots(figsize =(10, 6))

    ax.set_title('Least selling items', fontsize='18', fontweight='bold', color ='grey')
    ax.set_ylabel('Items', fontsize='14', fontweight='bold', color ='grey')
    ax.set_xlabel('Quantity sold', fontsize='14', fontweight='bold', color ='grey')

    ax.grid(b = True, color ='grey',
            linestyle ='-.', linewidth = 0.5,
            alpha = 0.2)

    ax.xaxis.set_ticks_position('none')

    ax.xaxis.set_tick_params(pad = 5)
    ax.yaxis.set_tick_params(pad = 10)

    ax.set_xlim(0, df3.quantity.max() * 1.2)

    ax.barh(ascending.item, ascending.quantity, color="coral")

    for Y,X in enumerate(ascending.quantity):
            ax.annotate("{:.1f}%".format(X * 100/np.sum(ascending.quantity)), xy=(X,Y), color='grey', fontsize='10', va='center')

    plt.tight_layout()
    plt.show()

