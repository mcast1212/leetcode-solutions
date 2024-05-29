class StockPrice(object):

    def __init__(self):
        self.prices = {}

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        self.prices[timestamp] = price

    def current(self):
        """
        :rtype: int
        """
        k = list(self.prices.keys())
        k.sort()
        last = self.prices[k[-1]]
        return last
        

    def maximum(self):
        """
        :rtype: int
        """
        k = self.prices.values()
        curr = k[0]
        for price in self.prices.values():
            if price > curr:
                curr = price
        return curr

    def minimum(self):
        """
        :rtype: int
        """
        k = self.prices.values()
        curr = k[0]
        for price in self.prices.values():
            if price < curr:
                curr = price
        return curr


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
