def get_next(num, nums):
    next_val = ''
    for n in nums:
        if n > num:
            next_val = n
            return str(next_val)
    return next_val 


def solution(queries):
    container = {}
    result = []
    for function, num in queries:
        if function == "ADD":
            if num in container:
                container[num] += 1
            else:
                container[num] = 1
            result.append("")
        elif function == "REMOVE":
            if num in container:
                container[num] -=1
                result.append('true')
                if container[num] == 0:
                    container.pop(num)
            else:
                result.append("false")
        elif function == "EXISTS":
            result.append("true" if num in container.keys() else "false")
        elif function == "GET_NEXT":
            nums = [int(key) for key in container.keys()]
            nums.sort()
            result.append(get_next(int(num), nums))
            
    return result

queries = [
    ["ADD","0"], 
    ["ADD","1"], 
    ["ADD","1"], 
    ["ADD","11"], 
    ["ADD","22"], 
    ["ADD","3"], 
    ["ADD","5"], 
    ["GET_NEXT","0"], 
    ["GET_NEXT","1"], 
    ["REMOVE","1"], 
    ["GET_NEXT","1"], 
    ["ADD","0"], 
    ["ADD","1"], 
    ["ADD","2"], 
    ["ADD","1"], 
    ["GET_NEXT","1"], 
    ["GET_NEXT","2"], 
    ["GET_NEXT","3"], 
    ["GET_NEXT","5"]
]


result = solution(queries)
print(result)