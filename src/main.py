import dom as dom
import nodes as nodes
import ntypes as ntypes
import execu as execu
import jstt, sys

if "-d" in sys.argv or "--debug" in sys.argv:
    debug = True
else:
    debug = False

try:
    file_to_parse = sys.argv[1]
except:
    print("fatal ERR! No file passed to execute")
    sys.exit(1)


with open(file_to_parse, 'r') as f:
    if debug:
        print("DEBUG: Read file")
    Nodes = jstt.JSON_to_tok(f.read(), debug=debug)
    if debug:
        print("DEBUG: RAW JSON turned into DOM nodes successfully")

DOM = dom.DOM(Nodes=Nodes)
if debug:
    print(f"DEBUG: DOM Tree: {DOM}")
if debug:
        print("DEBUG: Executing DOM..")
execu.execute_dom(DOM=DOM, debug=debug)
if debug:
        print("DEBUG: DOM Executed")