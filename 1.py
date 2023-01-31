class queue:
    def __init__(self):
        self.queue = list()
    def addtoq(self,dataval):
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
            return False
    def size(self):
        return len(self.queue)
    def show(self):
        return self.queue    
    def pop(self):
        return self.queue.pop(0)
    def add1(self,value):
        self.queue.insert(0,value)
    def add2(self,value):
        self.queue.append(value)  
    def popend(self):
        return self.queue.pop()      


      
Thequeue = queue()
Thequeue.addtoq("faisal")
Thequeue.addtoq("abdullah")
Thequeue.addtoq("sh")
Thequeue.pop()
Thequeue.add1("sii")
Thequeue.add2("messi")
Thequeue.popend()
print(Thequeue)
print(Thequeue.show())


        