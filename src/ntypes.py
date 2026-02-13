class NodeType:
    def __init__(self, Name:str):
        self.Name = Name
    
    def __str__(self):
        return self.Name

    def __repr__(self):
        return self.__str__()
    
class TextBox(NodeType):
    def __init__(self):
        super().__init__("TextBox")
    