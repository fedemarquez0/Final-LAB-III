from django.conf import settings

from Cavovich.models import Vino
 
class Cart(object):
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, vino, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        print("intentando agregar el producto")
        product_id = str(vino.pk)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(vino.precio)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()
    
    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True
    
    def remove(self, vino):
        """
        Remove a product from the cart
        :param product: 
        :return: 
        """
        product_id = str(vino.pk)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Vino.objects.filter(id__in=product_ids)
        for vino in products:
            self.cart[str(vino.pk)]['product'] = vino
    
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
    
    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values()) 
    
    def clear(self):
        """
        remove cart from session
        :return:
        """
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True