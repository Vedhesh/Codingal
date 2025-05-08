import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantManagement:

    def __init__(self, root):

        self.root = root
        self.root.title("Restaurant Menu")

        self.menu_items = {"PIZZA":6.5, "BURGER":4, "FRIES":3, "PEPSI":1, "FANTA":2, "SPRITE":1}
        self.exchange_rate = 85
        self.setup_background(root)

        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.menu_labels = {}
        self.menu_quantities = {}

        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(frame, text=f"{item} (${price})", font=("Arial",12))
            label.grid(row=i, column=0, padx=10, pady=5)
            
            self.menu_items[item] = label

            entry = ttk.Entry(frame, width=5)
            entry.grid(row=i, column=1, padx=10, pady=5)

            self.menu_quantities[item] = entry

            self.currency = tk.StringVar()

            ttk.Label(frame, text="Currency:", font=("Arial",12)).grid(row=len(self.menu_items)+1, column=0, padx=10, pady=5)
            
            dropdown = ttk.Combobox(frame, textvariable=self.currency, state="readonly", width=18, values=("USD", "INR"))
            dropdown.grid(row=len(self.menu_items)+1, column=1, padx=10, pady=5)
            dropdown.current(0)

            self.currency.trace("w", self.update_prices)

            order = ttk.Button(frame, text="Place Order", command=self.place_order)
            order.grid(row=len(self.menu_items)+2, columnspan=3, padx=10, pady=5)

    def setup_background(self, root):
        bg_w, bg_h = 800, 600

        canvas = tk.Canvas(root, width=bg_w, height=bg_h)
        canvas.pack()

        original_image = tk.PhotoImage(file="TKINTER\CLASS-6-TTK\\background.png")
        background_image = original_image.subsample(original_image.width() // bg_w, original_image.height() // bg_h)
