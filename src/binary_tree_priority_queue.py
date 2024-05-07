class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None


class PriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):  # метод вставки, передаём значение и приоритет
        new_node = Node(value, priority)  # новый элемент - объект класса Элемент
        if not self.root:
            self.root = new_node  # если нет корня, то новый элемент корень
            return
        # если корень есть

        current = self.root
        while current:  # ищем место для нужного элемента

            if new_node.priority < current.priority:  # если элем меньше текущего, то идет вправо
                if not current.right:
                    current.right = new_node
                    break
                current = current.right

            else:  # если элем больше то идем влево
                if not current.left:
                    current.left = new_node
                    break
                current = current.left

    def remove_max(self):  # удаление максимального элемента
        if not self.root:  # если корня нет ничего не удаляем
            return None

        max_node = self.find_max()  # находим максимальный элемент
        value = max_node.value
        self.root = self.remove_node(self.root, max_node)  # запускаем удаление
        return value

    def find_max(self):  # поиск макс элемента
        if not self.root:
            return None
        current = self.root

        while current.left:
            current = current.left

        return current

    def remove_node(self, root, node):  # функция удаление
        if not root:  # если нет рута, то конец удаления
            return None

        if root == node:  # если рут это удаляемый элемент, то:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left

            root.value, root.priority = node.value, node.priority
            root.left = self.remove_node(root.left, node)  # меняем местами удаляемый с самым низким
            return root  # самый низкий удаляем

        root.left = self.remove_node(root.left, node)  # рекурсивно идем по левой ветви, пока не найдем удаляемы элемент
        return root

    def display(self):
        self.inorder_traversal(self.root)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(f"Value: {root.value}, Priority: {root.priority}")
            self.inorder_traversal(root.right)


"""
# Приклад використання
pq = PriorityQueue()
pq.insert(50, 5)
pq.insert(80, 8)
pq.insert(60, 10)
pq.insert(40, 4)
pq.insert(20, 2)


print("Priority Queue:")
pq.display()


print("Removing elements with highest priority:")
while pq.root:
    print(pq.remove_max())"""
