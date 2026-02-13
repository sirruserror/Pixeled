import dom
import nodes


colors = {
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
}

def execute_dom(DOM:dom.DOM):
    textboxes = [node for node in DOM.Nodes if isinstance(node, nodes.TextBox)]
    textboxes.sort(key=lambda x: x.priority)
    
    for node in textboxes:
        print(colors.get(node.Color, "") + node.Text + colors.get("white", ""))