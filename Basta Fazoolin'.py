# QUESTION: You’ve started a position as the lead programmer for the family-style Italian restaurant Basta Fazoolin’ with My Heart. 
# The restaurant has been doing fantastically and seen a lot of growth lately. You’ve been hired to keep things organized.


#-----------------------------------------------------------------------------------------------
# CODE STARTS HERE!
# --- START FIRST CLASS ---
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return self.name + " menu is available from " + str(self.start_time) + " to " + str(self.end_time)

  def calculate_bill(self, purchased_items):
    total_bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        total_bill += self.items[purchased_item]
    return total_bill
# --- END FIRST CLASS ---

# --- START SECOND CLASS ---
class Francise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address 
  
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if (time >= menu.start_time and time <= menu.end_time):
        available_menus.append(menu)
    return available_menus
  
# --- END SECOND CLASS ---

# -- START THRID CLASS ---
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

# --- END THIRD CLASS ---

# Declaration of Variables
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

# Creation of Menu objects
brunch = Menu("brunch", brunch_items, 1100, 1600)
early_bird = Menu("early bird", early_bird_items, 1500, 1800)
dinner = Menu("dinner", dinner_items, 1700, 2300)
kids = Menu("kids", kids_items, 1100, 2100)
arepas_menu = Menu("Take a’ Arepa", arepas_items, 1000, 2000)

# Try out your Code Here
#print(brunch)
#print(kids)

# Testing the Menu.calculate_bill() method
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# Create two francise objects
menus = [brunch, early_bird, dinner, kids]

# Second constructor objects
flagship_store = Francise("1232 West End Road", menus)
new_installment = Francise("12 East Mulberry Street", menus)

# Step 23
arepas_place = Francise("189 Fitzgerald Avenue", arepas_menu)
# Third constructor objects
franchises = [flagship_store, new_installment]
first_business = Business("Basta Fazoolin' with my Heart", franchises)
new_business = Business("Take a' Arepa", arepas_place)
# Testing the available_menus() method
print(flagship_store.available_menus(1200))
print(flagship_store.available_menus(1700))