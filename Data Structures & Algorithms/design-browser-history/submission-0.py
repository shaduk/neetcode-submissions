
class Node:

    def __init__(self, website, nextp = None, prev = None):
        self.nextp = nextp
        self.prev = prev
        self.website = website

class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = Node(homepage)

    def visit(self, url: str) -> None:
        new_node = Node(url, None, self.current)
        self.current.nextp = new_node      # bug 1 fix
        self.current = new_node

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev:   # bug 2 fix
            self.current = self.current.prev
            steps -= 1
        return self.current.website

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.nextp:
            self.current = self.current.nextp
            steps -= 1
        return self.current.website


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)