Star Bakery which has an online delivery service that serves from 1000
branches across India. Bakery has also hired an analyst to check the health of your business
and provide use full information about health of its business
For this application I assumed just one simple order entity as following
Order Entity
Order entity has following properties :
• Item type : Cake, Cookies, Muffins
• Order State : Created, Shipped, Delivered, Canceled
• Last update time
• Branch : Branch location which this order belongs to. This could be simple id
from 1 to 1000
• Customer : id of customer who placed the order
Here are price of each item in the bakery
• Cake : Rs 500
• Cookies : Rs 50
• Muffins : Rs 100
An analyst can check the health of the business through a dashboard which consist of following
widgets
• Time selector widget to select which time range he wanted to view the data
• Time Series charts of order data
▪ number of order
▪ Total value of orders in Rupees
. Ability to select one or both the charts
• A bar chart widget showing orders divided each type (Cake, Muffin, Cookies)
• A bar chart widget showing order by state (Created, Shipped, Delivered, Canceled)
• A chart showing top 5 branches
• Allowing user to filter the output of order data time series chart by selecting type, state or
