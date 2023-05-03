from entities import Product, Item, Shop

if __name__=="__main__":
    test_products = [ 
        Product("Yerba", 300),
        Product("Aceite", 200),
        Product("Jugo", 150)
    ]

    shop = Shop("2023-04-28")

    shop.add_item( Item(2, test_products[0]) )
    shop.add_item( Item(4, test_products[1]) )
    shop.add_item( Item(1, test_products[2]) )

    for item in shop.items:
        print(item)

    total = shop.get_total()
    total_increment_15 = round(total * (1+0.15), 2)
    print(f"### Total: {total_increment_15} ###")

