class Queue:
    def __init__(self):
        self.orders = []

    def is_empty(self):
        return len(self.orders) == 0

    def enqueue(self, order):
        self.orders.append(order)
    
    def dequeue(self):
        if not self.is_empty():
            return self.orders.pop(0)
        else:
            return (f'There are no orders in your queue.')
        
    def peek(self):
        if not self.is_empty():
            return self.orders[0]
        else:
            return (f'There are no orders in your queue.')

class Order:
    def __init__(self, id, items, customer):
        self.id = id
        self.items = items
        self.customer = customer

        
class Restaraunt:
    def __init__(self):
        self.kitchen = Queue()
        self.customer = Queue()
        self.order_count = 0

    def add_order(self, items, customer):
        self.order_count += 1
        order = Order(self.order_count, items, customer)
        self.kitchen.enqueue(order)
        print(f'{customer} ordered {items}')

    def order_complete(self):
        if not self.kitchen.is_empty():
            order = self.kitchen.dequeue()
            print(f'Order complete for: {order.customer}')
            self.customer.enqueue(order)
        else:
            print('There are no orders to complete.')

    def notify_customer(self):
        if not self.customer.is_empty():
            order = self.customer.dequeue()
            print(f"Order {order.id} is ready for customer {order.customer}")
        else:
            print("No orders in the customer queue")
            return
            

order = Restaraunt()

order.add_order(['pizza', 'burger'], 'chris')
order.add_order('burger','ayden')
order.add_order('salad','savvy')

order.order_complete()
order.order_complete()

order.notify_customer()
order.notify_customer()
order.notify_customer()
