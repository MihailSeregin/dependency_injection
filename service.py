class Service:
    def __init__(self, client, timeout:int):
        self.client = client
        self.timeout = timeout
    def report(self):
	    print(self.timeout)    
        
