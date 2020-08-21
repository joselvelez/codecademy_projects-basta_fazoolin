# Make the Menu Class
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "{kids} Menu is available at {start_time} and ends at {end_time}".format(kids=self.name, start_time=self.start_time, end_time=self.end_time)

    def calculate_bill(self, purchased_items):
        bill = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                bill += self.items[purchased_item]
        return bill

# Create a Franchise Class
class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    
    def __repr__(self):
        return "Located at {address}.".format(address=self.address)

    def available_menus(self, time):
        open_menus = []
        for menu in self.menus:
            if time >= menu.start_time and time < menu.end_time:
                open_menus.append(menu)
        return open_menus

# Creat a Business Class
class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

# Brunch Menu
brunch_menu_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
    'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
    }
brunch = Menu('Brunch', brunch_menu_items , 1100, 1600)
# Early Bird Menu
early_bird_menu_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
    }
early_bird = Menu('Early Bird Dinners', early_bird_menu_items , 1500, 1800)
# Dinner Menu
dinner_menu_items = {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
    }
dinner = Menu('Dinner', dinner_menu_items , 1700, 2300)
# Kids Menu
kids_menu_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
    }
kids = Menu('Kids', kids_menu_items , 1100, 2100)
# Arepas Menu
arepas_menu_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Take a' Arepa", arepas_menu_items, 1000, 2000)
# Menus Array
menus = [brunch, early_bird, dinner, kids]

# Franchise Objects
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
arepas_place = Franchise('189 Fitzgerald Avenue', arepas_menu)

# Business Objects
Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
Business("Take a' Arepa", arepas_place)

print(flagship_store.available_menus(1700))

