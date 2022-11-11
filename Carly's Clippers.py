# You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. 
# Your job is to go through the lists of data that have been collected in the past couple of weeks. 
# You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Loop through prices list and add each to total price
total_price = 0
for price in prices:
  total_price += price

average_price= total_price / len(prices)
print("Average Haircut Pice " + str(average_price))

# Each price in prices minus 5
new_prices = [price - 5 for price in prices]
print(new_prices)

# Find total revenue
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: " + str(total_revenue))

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)