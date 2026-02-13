import dom as dom
import nodes as nodes
import ntypes as ntypes

Nodes = [nodes.DOM_Node("TextBox1", 1, ntypes.NodeType, 0)]
DOM = dom.DOM(Nodes)
print(DOM)