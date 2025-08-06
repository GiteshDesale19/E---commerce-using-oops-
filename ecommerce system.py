# 📦 E-commerce System Using OOP in Python


class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity

    def __str__(self):
        return f"{self.name} (₹{self.price}) - Stock: {self.stock}"


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.cart = []

    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            self.cart.append((product, quantity))
            product.update_stock(-quantity)
            print(f"✅ {quantity} x {product.name} added to cart.")
        else:
            print(f"❌ Not enough stock for {product.name}.")

    def view_cart(self):
        print(f"\n🛒 {self.name}'s Cart:")
        if not self.cart:
            print("Cart is empty.")
            return
        for product, quantity in self.cart:
            print(f"- {product.name} x {quantity} = ₹{product.price * quantity}")

    def checkout(self):
        total = sum(product.price * qty for product, qty in self.cart)
        print(f"\n💰 Total amount to pay: ₹{total}")
        self.cart.clear()
        print("✅ Checkout complete.")


class Store:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def display_products(self):
        print("\n🛍️ Available Products:")
        for product in self.products.values():
            print(product)

    def get_product_by_id(self, product_id):
        return self.products.get(product_id)


if __name__ == "__main__":
    
    store = Store()

    # Add products
    store.add_product(Product(1, "T-shirt", 499, 10))
    store.add_product(Product(2, "Jeans", 999, 5))
    store.add_product(Product(3, "Sneakers", 1999, 3))

    # Create a user
    user = User(101, "Geet")

    # Display products
    store.display_products()

    # User adds products to cart
    user.add_to_cart(store.get_product_by_id(1), 2)
    user.add_to_cart(store.get_product_by_id(2), 1)
    user.add_to_cart(store.get_product_by_id(3), 4)  

    # View cart and checkout
    user.view_cart()
    user.checkout()
    user.view_cart()
