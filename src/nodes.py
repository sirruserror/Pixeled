import ntypes as ntypes

class DOM_Node:
    def __init__(self, nodeName:str, nodeID:int, nodeType:ntypes.NodeType, priority:int):
        self.nodeName = nodeName
        self.nodeID = nodeID
        self.nodeType = nodeType
        self.priority = priority
        
    def __repr__(self):
        return {"nodeName": self.nodeName, "nodeID": self.nodeID, "nodeType": self.nodeType, "priority": self.priority}
    
    def __str__(self):
        return f"{self.__repr__()}"
    
    def __destruct__(self):
        del(self)
    
