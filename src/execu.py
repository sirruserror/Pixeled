import dom, sys
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

def execute_dom(DOM:dom.DOM, debug:bool):
    if debug:
        print("DEBUG: Sort <TextBox> element/s")
    textboxes = [node for node in DOM.Nodes if isinstance(node, nodes.TextBox)]
    textboxes.sort(key=lambda x: x.priority)
    if debug:
        print("DEBUG: Sorted <TextBox> element/s")
    
    if debug:
        print("DEBUG: Sort <ErrorBox> element/s")
    errorboxes = [node for node in DOM.Nodes if isinstance(node, nodes.ErrorBox)]
    errorboxes.sort(key=lambda x: x.priority)
    if debug:
        print("DEBUG: Sorted <ErrorBox> element/s")
    
    if debug:
        print("DEBUG: PARSE loop <TextBox> element/s")
    for node in textboxes:
        print(colors.get(node.Color, "") + node.Text + colors.get("white", ""))
    if debug:
        print("DEBUG: Parsed <TextBox> element/s")

    if debug:
        print("DEBUG: PARSE loop <ErrorBox> element/s")
    for node in errorboxes:
        sys.stderr.write(colors.get("red", "") + node.Text + colors.get("white", ""))
        if node.endex == True:
            if debug:
                print(f"DEBUG: EXIT parse <ErrorBox> element/s, ErrorCode: {node.ErrorCode}")
            sys.exit(node.ErrorCode)
    if debug:
        print("DEBUG: Parsed loop <ErrorBox> element/s")
