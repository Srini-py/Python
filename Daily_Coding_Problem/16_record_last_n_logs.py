# You run an e-commerce website and want to record the last N order ids in a log. 
# Implement a data structure to accomplish this, with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. 
# i is guaranteed to be smaller than or equal to N.
            

class Log:
    def __init__(self, n):
        self.maxsize = n
        self.circularbuffer = [0] * n
        self.curr_index = 0
        
    def record(self, orderid):
        self.circularbuffer[self.curr_index] = orderid
        self.curr_index = (self.curr_index + 1) % maxsize
        
    def get_last(self, i):
        return circularbuffer[(curr_index - i + maxsize) % maxsize]