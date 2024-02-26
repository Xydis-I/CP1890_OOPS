from dataclasses import dataclass


@dataclass
class Node:
    data: object = None
    next: object = None

    def __repr__(self):
        return f'Node: {self.data}'


test1 = Node(2)
print(test1)


@dataclass
class LinkedList:
    head: Node = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return '->'.join(nodes)

    def insert_at_head(self, node: Node) -> None:
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    # insert using position of existing Node
    # def insert(self, node: Node, position: Node) -> None:
    #     if self.head is None:
    #         self.head = node
    #         return
    #     data = self.head
    #     while data != position:
    #         data = data.next
    #     nextNode = data.next
    #     data.next = node
    #     node.next = nextNode

    # insert using a pseudo-index
    def insert(self, node: Node, position: int) -> None:
        data = self.head
        pos = 0

        if position == pos:
            self.insert_at_head(node)
            return

        while pos+1 < position:
            data = data.next
            pos += 1

        try:
            nextNode = data.next
            data.next = node
            node.next = nextNode
        except AttributeError:
            print('Position out of range.')

    def insert_at_end(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            return
        data = self.head
        while data.next is not None:
            data = data.next
        data.next = node


linkedList = LinkedList()
print(linkedList)

firstNode = Node('a')
linkedList.head = firstNode

secondNode = Node('b')
thirdNode = Node('c')

firstNode.next = secondNode
secondNode.next = thirdNode

print(linkedList)

newStartNode = Node('start')
newEndNode = Node('end')
newInsertNode = Node('insert')

linkedList.insert_at_head(newStartNode)
print(linkedList)

linkedList.insert_at_end(newEndNode)
print(linkedList)

linkedList.insert(newInsertNode, 5)
print(linkedList)
