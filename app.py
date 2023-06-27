import tkinter as tk
from parsing import *

root = tk.Tk()
root.title("Цены")


def App():
    def get_data():
        freezer = get_price(FREEZER)
        samsung = get_price(SAMSUNG)
        iphone = get_price(IPHONE)
        router = get_price(ROUTER)
        victus = get_price(VICTUS)
        macbook = get_price(MACBOOK)
        vacuum_cleaner = get_price(VACUUM_CLEANER)
        multicooker = get_price(MULTICOOKER)
        plate = get_price(PLATE)
        rectifier = get_price(RECTIFIER)
        ALL_DATA = [freezer, samsung, iphone, router, victus, macbook, vacuum_cleaner, multicooker, plate, rectifier]
        return ALL_DATA

    def add_values(ALL_DATA):
        global freezer_price, samsung_price, iphone_price, router_price, victus_price, macbook_price, vacuum_cleaner_price, multicooker_price, plate_price, rectifier_price

        freezer_price = tk.Label(root, text=f"{ALL_DATA[0][0]} тг.", font=("Arial", 15))
        freezer_price.grid(row=1, column=1, padx=10, pady=10)
        samsung_price = tk.Label(root, text=f"{ALL_DATA[1][0]} тг.", font=("Arial", 15))
        samsung_price.grid(row=2, column=1, padx=10, pady=10)
        iphone_price = tk.Label(root, text=f"{ALL_DATA[2][0]} тг.", font=("Arial", 15))
        iphone_price.grid(row=3, column=1, padx=10, pady=10)
        router_price = tk.Label(root, text=f"{ALL_DATA[3][0]} тг.", font=("Arial", 15))
        router_price.grid(row=4, column=1, padx=10, pady=10)
        victus_price = tk.Label(root, text=f"{ALL_DATA[4][0]} тг.", font=("Arial", 15))
        victus_price.grid(row=5, column=1, padx=10, pady=10)
        macbook_price = tk.Label(root, text=f"{ALL_DATA[5][0]} тг.", font=("Arial", 15))
        macbook_price.grid(row=6, column=1, padx=10, pady=10)
        vacuum_cleaner_price = tk.Label(root, text=f"{ALL_DATA[6][0]} тг.", font=("Arial", 15))
        vacuum_cleaner_price.grid(row=7, column=1, padx=10, pady=10)
        multicooker_price = tk.Label(root, text=f"{ALL_DATA[7][0]} тг.", font=("Arial", 15))
        multicooker_price.grid(row=8, column=1, padx=10, pady=10)
        plate_price = tk.Label(root, text=f"{ALL_DATA[8][0]} тг.", font=("Arial", 15))
        plate_price.grid(row=9, column=1, padx=10, pady=10)
        rectifier_price = tk.Label(root, text=f"{ALL_DATA[9][0]} тг.", font=("Arial", 15))
        rectifier_price.grid(row=10, column=1, padx=10, pady=10)

    add_values(get_data())

    # Заголовок
    label = tk.Label(root, text="Цены", font=("Arial", 20), background="red", foreground="black", border=10)
    label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    freezer_label = tk.Label(root, text="Цена холодильника: ", font=("Arial", 15))
    freezer_label.grid(row=1, column=0, padx=10, pady=10)

    samsung_label = tk.Label(root, text="Цена самсунга: ", font=("Arial", 15))
    samsung_label.grid(row=2, column=0, padx=10, pady=10)

    iphone_label = tk.Label(root, text="Цена айфона: ", font=("Arial", 15))
    iphone_label.grid(row=3, column=0, padx=10, pady=10)

    router_label = tk.Label(root, text="Цена роутера: ", font=("Arial", 15))
    router_label.grid(row=4, column=0, padx=10, pady=10)

    victus_label = tk.Label(root, text="Цена виктуса: ", font=("Arial", 15))
    victus_label.grid(row=5, column=0, padx=10, pady=10)
    
    macbook_label = tk.Label(root, text="Цена макбука: ", font=("Arial", 15))
    macbook_label.grid(row=6, column=0, padx=10, pady=10)

    vacuum_cleaner_label = tk.Label(root, text="Цена пылесоса: ", font=("Arial", 15))
    vacuum_cleaner_label.grid(row=7, column=0, padx=10, pady=10)

    multicooker_label = tk.Label(root, text="Цена мультиварки: ", font=("Arial", 15))
    multicooker_label.grid(row=8, column=0, padx=10, pady=10)

    plate_label = tk.Label(root, text="Цена плиты: ", font=("Arial", 15))
    plate_label.grid(row=9, column=0, padx=10, pady=10)

    rectifier_label = tk.Label(root, text="Цена плойки: ", font=("Arial", 15))
    rectifier_label.grid(row=10, column=0, padx=10, pady=10)


if __name__ == "__main__":
    App()
    root.mainloop()