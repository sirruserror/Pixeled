import ntypes as ntypes

class DOM_Node:
    def __init__(self, nodeName:str, nodeID:int, nodeType:ntypes.NodeType, priority:int):
        self.nodeName = nodeName
        self.nodeID = nodeID
        self.nodeType = nodeType
        self.priority = priority
        
    def __repr__(self):
        return str({"nodeName": self.nodeName, "nodeID": self.nodeID, "nodeType": self.nodeType, "priority": self.priority})
    
    def __str__(self):
        return f"[{self.nodeName}, {self.nodeID}, {self.nodeType}, {self.priority}]"
    
    def __destruct__(self):
        del(self)
    
class TextBox(DOM_Node):
    def __init__(self, nodeName:str, nodeID:int, priority:int, Text:str, Color: str):
        super().__init__(nodeName, nodeID, ntypes.TextBox(), priority)
        self.Text = Text
        self.Color = Color
    
    def __repr__(self):
        return str({"nodeName": self.nodeName, "nodeID": self.nodeID, "nodeType": self.nodeType, "priority": self.priority, "Text": self.Text, "Color": self.Color})

    def __str__(self):
        return self.__repr__()

class ErrorBox(DOM_Node):
    def __init__(self, nodeName:str, nodeID:int, priority:int, Text:str, endex:bool=False, ErrorCode:int=0):
        super().__init__(nodeName, nodeID, ntypes.ErrorBox(), priority)
        self.Text = Text
        self.endex = endex
        self.ErrorCode = ErrorCode

    def __repr__(self):
        return str({"nodeName": self.nodeName, "nodeID": self.nodeID, "nodeType": self.nodeType, "priority": self.priority, "Text": self.Text, "ErrorCode": self.ErrorCode, "EndExecution": self.endex})
    
    def __str__(self):
        return self.__repr__()



