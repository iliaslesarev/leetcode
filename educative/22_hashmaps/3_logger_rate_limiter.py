from typing import Dict


class RequestLogger:
    def __init__(self, time_limit):
        self.messages: Dict[str, int] = {}
        self.time_limit = time_limit

    def message_request_decision(self, timestamp, request):
        if request not in self.messages or timestamp - self.messages[request] >= self.time_limit:
            self.messages[request] = timestamp
            return True

        return False


rl = RequestLogger(7)

result = []
inp = [[1,"good morning"],[5,"good morning"],[9,"i need coffee"],[10,"hello world"],[11,"good morning"],[15,"i need coffee"],[17,"hello world"],[25,"i need coffee"]]
for pair in inp:
    result.append(rl.message_request_decision(pair[0], pair[1]))
print(result)
