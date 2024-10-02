import pdb

def solution(line):
    atLeastOneDigit = False
    if line[len(line) - 1] == '#':
        i = 0
        base = 0
        ...
        line = line.replace('_', '')
        if len(line) == 0:
            return False
        if line[0] == '#':
            return False

        base = int(line.split('#')[0])
        line = line.replace('#', '')

        letter_list = ['a', 'b', 'c', 'd', 'e', 'f']
        letter_list2 = ['A', 'B', 'C', 'D', 'E', 'F']
        is_valid = True
        for d in line:
            if d.isdigit():
                continue
            else:
                if d not in letter_list and d not in letter_list2:
                    is_valid = False
        if not is_valid:
            return False

        i += 1
        while i < len(line) - 1:
            if line[i] != '_':
                digit = -1
                if 'a' <= line[i] and line[i] <= 'f':
                    digit = ord(line[i]) - ord('a') + 10
                if 'A' <= line[i] and line[i] <= 'F':
                    digit = ord(line[i]) - ord('A') + 10
                if '0' <= line[i] and line[i] <= '9':
                    digit = ord(line[i]) - ord('0')
                if 0 <= digit and digit < base:
                    atLeastOneDigit = True
                else:
                    return False
            i += 1
    else:
        for i in range(len(line)):
            if line[i] != '_':
                if '0' <= line[i] and line[i] <= '9':
                    atLeastOneDigit = True
                else:
                    return False
    return atLeastOneDigit

def main():
    line = "123_456_789"
    line = "__________"
    line = "16#123'#"
    print(solution(line))


if __name__ == "__main__":
    main()