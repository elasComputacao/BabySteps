# URI: 1607 - Avance Letras


def solve(string1, string2):
    count = 0 
    for chr1, chr2 in zip(string1, string2):
        x, y = ord(chr1), ord(chr2)
        if x <= y:
            count += y - x 
        else:
            count += ord('z') - x + 1 + y - ord('a')

    return count


def main():
    n =  int(input())
    for _ in range(n):
        a, b = input().split()
        print(solve(a, b))


if __name__ == "__main__":
    main()


