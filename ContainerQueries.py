
def solution(queries):
    container = set()
    result = []
    for function, num in queries:
        if function == "ADD":
            container.add(num)
            result.append("")
        elif function == "EXISTS":
            result.append("true" if num in container else "false")

    return result





queries = [
    ["ADD", "1"],
    ["ADD", "2"],
    ["ADD", "5"],
    ["ADD", "2"],
    ["EXISTS", "2"],
    ["EXISTS", "5"],
    ["EXISTS", "1"],
    ["EXISTS", "4"],
    ["EXISTS", "3"],
    ["EXISTS", "0"]
]

result = solution(queries)
print(result)