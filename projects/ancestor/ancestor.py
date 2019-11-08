
def earliest_ancestor(ancestors, starting_node, index=0):
    parents = [];
    for a in ancestors:
        if(a[1] == starting_node):
            parents.append(a[0]);
    node = starting_node;
    value = index;
    for p in parents:
        n,v = earliest_ancestor(ancestors,p,index+1);
        if v > value:
            value = v;
            node = n;
        elif v == value and n < node:
            value = v;
            node = n;
    if index == 0:
        if starting_node == node:
            return -1;
        return node;
    return node, value;