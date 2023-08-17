class Order:
    def __init__(self, order_id, products, total_amount):
        self.order_id = order_id
        self.products = products
        self.total_amount = total_amount
        
    def calculate_total(self):
        total_sum = sum(self.total_amount)
        return total_sum
    
product = ['product1', 'product2', 'product3']
total = [10, 20, 30]

Order1 = Order('001', product, total)

print('Total payment', Order1.calculate_total())
    