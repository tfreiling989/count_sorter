from DoublyLinkedList import DoublyLinkedList
from typing import List, Tuple, Any
from collections import OrderedDict


class CountSorter:
    def __init__(self):
        self._list: DoublyLinkedList = DoublyLinkedList()
        self._item_nodes = {}

    def add_occurrence(self, item):
        """Adds an occurrence of an item. O(1)"""
        if item in self._item_nodes:
            node = self._item_nodes[item]
            node_count = node.data["count"]
            new_count = node_count + 1
            next_node = node.next
            if next_node and next_node.data["count"] == new_count:
                next_node.data["items"][item]=None
            else:
                self._list.insert_after(node,{"count":new_count, "items": OrderedDict({item:None})})
            del node.data["items"][item]
            if len(node.data["items"]) == 0:
                self._list.delete(node)
            new_node_location = node.next
        else:
            if not self._list.head or self._list.head.data["count"] > 1:
                self._list.push_front({"count": 1, "items": OrderedDict({item:None})})
            else:
                self._list.head.data["items"][item] = None
            new_node_location = self._list.head
        self._item_nodes[item] = new_node_location

    def get_most_frequent(self, num_items:int) -> OrderedDict[Any,int]:
        """
        Get most frequent items along with their counts. O(num_items)
        Example:
            [("a": 5, "b": 5, "c": 6]

        """
        res = OrderedDict()
        node = self._list.tail
        while len(res) < num_items:
            if not node:
                break
            else:
                for item in node.data["items"]:
                    if len(res) == num_items:
                        break
                    else:
                        res[item] = node.data["count"]
                node = node.prev

        return res
