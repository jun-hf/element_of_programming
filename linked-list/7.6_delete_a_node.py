def node_deletion(node):
    node.data = node.next.data
    node.next = node.data.next.next