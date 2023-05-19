if __name__ == '__main__':
    n = int(input())
    string = ''
    for i in range(1, n):
        to_string = str(i)
        string += to_string
    n = str(n)
    print(string + n)