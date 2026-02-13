import nodes as nodes

class DOM:
    def __init__(self, Nodes:list):
        for i in Nodes:
            if not isinstance(i, nodes.DOM_Node):
                raise TypeError("DOM Nodes <list> passed with non DOM_Node items")
        self.Nodes = Nodes
        
    def __str__(self):
        return f"{self.Nodes}"
    
    def __repr__(self):
        return self.__str__()