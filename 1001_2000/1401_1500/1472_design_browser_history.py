from typing import List


class BrowserHistory:
    def __init__(self, homepage: str):
        self.history: List[str] = [homepage]
        self.cur, self.last = 0, 0

    def visit(self, url: str) -> None:
        self.cur += 1
        if self.cur != len(self.history):
            self.history[self.cur] = url
        else:
            self.history.append(url)
        self.last = self.cur

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.history[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(self.cur + steps, self.last)
        return self.history[self.cur]


browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.visit("youtube.com")
print(browserHistory.back(1))
print(browserHistory.back(1))
print(browserHistory.forward(1))
browserHistory.visit("linkedin.com")
print(browserHistory.forward(2))
print(browserHistory.back(2))
print(browserHistory.back(7))
