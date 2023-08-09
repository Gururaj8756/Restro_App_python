
# from selenium import webdriver
# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = './chromedriver_linux64.zip'  # Update with the correct path

# chrome_browser = webdriver.Chrome(options=chrome_options)
# print(chrome_browser)

import tkinter as tk
from tkinter import messagebox
import sqlite3

class RestaurantBillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Billing App")

        self.conn = sqlite3.connect('restaurant.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS orders
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          item TEXT,
                          price REAL)''')
        self.conn.commit()

        self.item_label = tk.Label(root, text="Item:")
        self.item_label.pack()

        self.item_entry = tk.Entry(root)
        self.item_entry.pack()

        self.price_label = tk.Label(root, text="Price:")
        self.price_label.pack()

        self.price_entry = tk.Entry(root)
        self.price_entry.pack()

        self.add_button = tk.Button(root, text="Add Item", command=self.add_item)
        self.add_button.pack()

        self.calculate_button = tk.Button(root, text="Calculate Total", command=self.calculate_total)
        self.calculate_button.pack()

        self.total_label = tk.Label(root, text="Total: $0.00")
        self.total_label.pack()

    def add_item(self):
        item = self.item_entry.get()
        price = float(self.price_entry.get())

        self.c.execute("INSERT INTO orders (item, price) VALUES (?, ?)", (item, price))
        self.conn.commit()

        self.item_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def calculate_total(self):
        self.c.execute("SELECT SUM(price) FROM orders")
        total = self.c.fetchone()[0]
        self.conn.commit()

        self.total_label.config(text=f"Total: ${total:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantBillingApp(root)
    root.mainloop()
