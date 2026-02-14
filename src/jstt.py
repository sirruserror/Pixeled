import nodes
import json

def JSON_to_tok(jsons, debug:bool):
    if debug:
        print("DEBUG: Loading JSON")
    jsl = json.loads(jsons)
    Nodes = []
    if debug:
        print("DEBUG: TOKENIZE loop element/s")
    for item in jsl:
        if item.get("type") == "TextBox":
            if debug:
                print("DEBUG: <TextBox> element/s TOKENIZING")
            Nodes.append(nodes.TextBox(item["nodeName"], item["nodeID"], item["priority"], item["Text"], item["Color"]))
        elif item.get("type") == "ErrorBox":
            if debug:
                print("DEBUG: <ErrorBox> element/s TOKENIZING")
            Nodes.append(nodes.ErrorBox(item["nodeName"], item["nodeID"], item["priority"], item["Text"], item["endex"], item["ErrorCode"]))
        
    return Nodes