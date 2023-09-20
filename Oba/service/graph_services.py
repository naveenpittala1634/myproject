import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
# Load the order data
from Oba.db_module.db_operations import MysqlDB


"""
. A bar chart widget showing orders divided each type (Cake, Muffin, Cookies)
• A bar chart widget showing order by state (Created, Shipped, Delivered, Canceled) • 
. A chart showing top 5 branches

"""
def order_by_item_type():
    #finding cakes count and displaying the bar graph
    mysqldb = MysqlDB()
    # mysqldb.upload_data()
    db_data= mysqldb.fetch_data_from_db("select * from sys.orders")
    df = pd.DataFrame(db_data,columns=["item_type", "order_state", "last_update_time", "branch", "customer", "price"])
    grouped_df = df.groupby('item_type')
    df = grouped_df['item_type'].count()
    cols = df.index.to_list()
    values = df.to_list()
    # Create a bar chart of the top 4 order states with highest sale
    plt.bar(cols, values)
    plt.xlabel("Item Type")
    plt.ylabel("Total Count")
    return plt.show()


def order_by_state():
    mysqldb = MysqlDB()
    # mysqldb.upload_data()
    db_data= mysqldb.fetch_data_from_db("select * from sys.orders")
    df = pd.DataFrame(db_data,columns=["item_type", "order_state", "last_update_time", "branch", "customer", "price"])
    total_sale_per_state = df.groupby('order_state')['price'].sum()

    # Get top 4 order states with highest sale
    top_4_states = total_sale_per_state.sort_values(ascending=True).head(4)

    # Get order state names and total sale
    state_names = top_4_states.index.to_list()
    total_sale = top_4_states.to_list()

    # Create a bar chart of the top 4 order states with highest sale
    plt.bar(state_names, total_sale)
    plt.xlabel("Order State")
    plt.ylabel("Total Sale")
    plt.title("Top 4 Order States with Highest Sale")
    return plt.show()

def top_5_branches():
    mysqldb = MysqlDB()
    # mysqldb.upload_data()
    db_data= mysqldb.fetch_data_from_db("select * from sys.orders")
    df = pd.DataFrame(db_data,columns=["item_type", "order_state", "last_update_time", "branch", "customer", "price"])
    total_sale_per_branch = df.groupby('branch')['price'].sum()
    # Get top 5 branches with highest sale
    top_5_branches = total_sale_per_branch.sort_values(ascending=False).head(5)
    # Get branch names and total sale
    branch_names = top_5_branches.index.to_list()
    total_sale = top_5_branches.to_list()
    # Create a bar chart of the top 5 branches with highest sale
    plt.bar(branch_names, total_sale)
    plt.xlabel("Branch")
    plt.ylabel("Total Sale")
    plt.title("Top 5 Branches with Highest Sale")
    return plt.show()
