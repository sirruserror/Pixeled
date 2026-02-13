import dom as dom
import nodes as nodes
import ntypes as ntypes
import execu as execu
import jstt, sys

try:
    file_to_parse = sys.argv[1]
except:
    print("fatal ERR! No file passed to execute")
    sys.exit(1)

with open(file_to_parse, 'r') as f:
    Nodes = jstt.JSON_to_tok(f.read())

DOM = dom.DOM(Nodes=Nodes)
execu.execute_dom(DOM=DOM)