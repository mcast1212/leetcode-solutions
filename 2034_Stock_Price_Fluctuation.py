class StockPrice(object):

    def __init__(self):
        self.prices = {}
        self.highest = 0

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        self.prices[timestamp] = price
        self.highest = max(self.highest, timestamp)

    def current(self):
        """
        :rtype: int
        """
        return self.prices[self.highest]
        

    def maximum(self):
        """
        :rtype: int
        """
        val = list(self.prices.values())
        k = list(self.prices.keys())[list(self.prices.values()).index(max(val))]
        return self.prices[k]

    def minimum(self):
        """
        :rtype: int
        """
        val = list(self.prices.values())
        k = list(self.prices.keys())[list(self.prices.values()).index(min(val))]
        return self.prices[k]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()