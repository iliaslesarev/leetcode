def exclusive_time(n, logs):
    stack = []
    result = [0] * n
    for log in logs:
        process, state, timestamp = log.split(":")
        if state == "start":
            stack.append((int(process), int(timestamp)))
        else:
            begin_process, begin_timestamp = stack.pop()
            process_len = int(timestamp) - begin_timestamp + 1
            result[int(process)] += process_len
            if len(stack) > 0:
                result[stack[-1][0]] -= process_len
    return result


print(exclusive_time(1, ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]))
print(exclusive_time(2, ["0:start:0", "1:start:3", "1:end:6", "0:end:10"]))
