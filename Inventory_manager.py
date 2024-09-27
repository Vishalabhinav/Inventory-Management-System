import pandas as pd

class InventoryManager:
    def __init__(self):
        # Inventory structure: Item_ID, Item_Name, Category, Stock_Quantity, Price
        self.inventory = pd.DataFrame(columns=['Item_ID', 'Item_Name', 'Category', 'Stock_Quantity', 'Price'])
    
    def add_item(self, item_id, item_name, category, stock_quantity, price):
        """Adds a new item to the inventory."""
        new_item = {'Item_ID': item_id, 'Item_Name': item_name, 'Category': category, 'Stock_Quantity': stock_quantity, 'Price': price}
        self.inventory = self.inventory.append(new_item, ignore_index=True)
        print(f"Item {item_name} added to inventory.")
    
    def remove_item(self, item_id):
        """Removes an item from the inventory."""
        self.inventory = self.inventory[self.inventory['Item_ID'] != item_id]
        print(f"Item ID {item_id} removed from inventory.")
    
    def update_stock(self, item_id, new_quantity):
        """Updates stock quantity of an item."""
        self.inventory.loc[self.inventory['Item_ID'] == item_id, 'Stock_Quantity'] = new_quantity
        print(f"Stock for Item ID {item_id} updated to {new_quantity}.")
    
    def generate_low_stock_report(self, threshold):
        """Generates a report of items with stock below a threshold."""
        low_stock_items = self.inventory[self.inventory['Stock_Quantity'] < threshold]
        print("Low stock items:")
        return low_stock_items
    
    def show_inventory(self):
        """Displays current inventory."""
        print(self.inventory)

