from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @classmethod
    def load(cls, data: dict) -> "Product":
        return cls(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> list[Product]:
    """Fetches all products from the database and returns them as a list of Product objects."""
    return [Product.load(product) for product in dao.list_products()]


def get_product(product_id: int) -> Product:
    """Fetches a single product by its ID and returns it as a Product object."""
    product_data = dao.get_product(product_id)
    return Product.load(product_data) if product_data else None


def add_product(product: dict):
    """Adds a new product to the database."""
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    """Updates the quantity of a product. Raises an error if quantity is negative."""
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)
