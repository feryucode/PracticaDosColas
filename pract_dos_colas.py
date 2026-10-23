from abc import ABC, abstractmethod


class Order:
    def __init__(self, qtty: int, customer: str):
        self.customer = customer
        self.qtty = qtty

    def print(self):
        print("     Customer: " + self.getCustomer())
        print("     Quantity: " + str(self.getQtty()))
        print("     ------------")

    def getQtty(self) -> int:
        return self.qtty

    def getCustomer(self) -> str:
        return self.customer


class Node:
    def __init__(self, info, next_node=None):
        self.info = info
        self.next = next_node

    def getInfo(self):
        return self.info

    def setInfo(self, info):
        self.info = info

    def getNext(self):
        return self.next

    def setNext(self, next_node):
        self.next = next_node


class QueueInterface(ABC):
    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def isEmpty(self) -> bool:
        pass

    @abstractmethod
    def front(self):
        pass

    @abstractmethod
    def enqueue(self, info):
        pass

    @abstractmethod
    def dequeue(self):
        pass


class Queue(QueueInterface):
    def __init__(self):
        self.top = None
        self.tail = None
        self._size = 0

    def size(self) -> int:
        return self._size

    def isEmpty(self) -> bool:
        return self.top is None

    def front(self):
        if self.isEmpty():
            return None
        return self.top.getInfo()

    def enqueue(self, info):
        new_node = Node(info)
        if self.isEmpty():
            self.top = new_node
            self.tail = new_node
        else:
            self.tail.setNext(new_node)
            self.tail = new_node
        self._size += 1

    def dequeue(self):
        if self.isEmpty():
            return None

        info = self.top.getInfo()
        self.top = self.top.getNext()
        self._size -= 1

        if self.top is None:
            self.tail = None

        return info

    def printInfo(self):
        print("********* QUEUE DUMP *********")
        print(f"   Size: {self.size()}")
        node = self.top
        index = 1
        while node is not None:
            print(f"   ** Element {index}")
            info = node.getInfo()
            if hasattr(info, "print"):
                info.print()
            else:
                print(f"     {info}")
            node = node.getNext()
            index += 1
        print("******************************")

    def getNth(self, pos: int):
        if pos < 1 or pos > self.size():
            return None

        node = self.top
        current_pos = 1
        while node is not None and current_pos < pos:
            node = node.getNext()
            current_pos += 1

        return node.getInfo() if node is not None else None


class TestQueue:
    @staticmethod
    def main():
        queue = Queue()

        queue.enqueue(Order(20, "cust1"))
        queue.printInfo()

        queue.enqueue(Order(30, "cust2"))
        queue.printInfo()

        queue.enqueue(Order(40, "cust3"))
        queue.printInfo()

        first = queue.front()
        if first is not None:
            first.print()
        queue.printInfo()

        removed = queue.dequeue()
        if removed is not None:
            removed.print()
        queue.printInfo()

        queue_cuatro = Queue()
        queue_cuatro.enqueue(Order(20, "cust1"))
        queue_cuatro.enqueue(Order(30, "cust2"))
        queue_cuatro.enqueue(Order(40, "cust3"))
        queue_cuatro.enqueue(Order(50, "cust3"))
        queue_cuatro.printInfo()

        tercer_elemento = queue_cuatro.getNth(3)
        if tercer_elemento is not None:
            tercer_elemento.print()

        print(queue_cuatro.getNth(10))


if __name__ == "__main__":
    TestQueue.main()