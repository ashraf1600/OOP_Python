class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

#-------------------------------------------------------------------------------------------------------
class Shop:
    def __init__(self):
        self.products = []  # List to store available products

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
            print(f"Product {product.name} added to the shop.")
        else:
            print("Only objects of type 'Product' can be added.")

    def display_products(self):
        if not self.products:
            print("No products in the shop.")
        else:
            print("Products available in the shop:")
            for product in self.products:
                print(product)

    def buy_product(self, product_name, quantity):
        for product in self.products:
            if product.name == product_name:
                if product.quantity >= quantity:
                    product.quantity -= quantity
                    print(f"Congratulations! You successfully bought {quantity} {product_name}(s).")
                    # Remove the product if quantity becomes zero
                    if product.quantity == 0:
                        self.products.remove(product)
                    return
                else:
                    print(f"Sorry, only {product.quantity} {product_name}(s) are available.")
                    return
        print(f"Sorry, {product_name} is not available in the shop.")
#===================================================================================================================

# Example Usage
if __name__ == "__main__":
    shop = Shop()

    # Adding products to the shop
    product1 = Product("Laptop", 1000, 10)
    product2 = Product("Smartphone", 500, 20)

    shop.add_product(product1)
    shop.add_product(product2)

    # Display available products
    shop.display_products()

    # Buying products
    shop.buy_product("Laptop", 2)
    shop.buy_product("Smartphone", 5)
    shop.buy_product("Smartphone", 30)  # Not enough quantity
    shop.buy_product("Tablet", 1)  # Product not available

    # Display products after purchase
    shop.display_products()
