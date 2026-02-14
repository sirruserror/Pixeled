import nodes
import json

def JSON_to_tok(jsons):
    jsl = json.loads(jsons)
    Nodes = []
    for item in jsl:
        if item.get("type") == "TextBox":
            Nodes.append(nodes.TextBox(item["nodeName"], item["nodeID"], item["priority"], item["Text"], item["Color"]))
        elif item.get("type") == "ErrorBox":
            Nodes.append(nodes.ErrorBox(item["nodeName"], item["nodeID"], item["priority"], item["Text"], item["endex"], item["ErrorCode"]))
        
    return Nodes