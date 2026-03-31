class MyStack:

    def __init__(self):
        self.in_q = deque()
        self.out_q = deque()

    def push(self, x: int) -> None:
        self.in_q.append(x)

    def pop(self) -> int:
        while len(self.in_q) != 1:
            x = self.in_q.popleft()
            self.out_q.append(x)
        y = self.in_q.popleft()
        self.in_q = self.out_q
        self.out_q = deque()
        return y

    def top(self) -> int:
        x = 0
        while self.in_q:
            x = self.in_q.popleft()
            self.out_q.append(x)
        self.in_q = self.out_q
        self.out_q = deque()
        return x

    def empty(self) -> bool:
        if len(self.in_q) is 0 and len(self.out_q) is 0:
            return True
        else:
            return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()