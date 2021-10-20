__author__ = "Alexandre Corlet"


def solve(mat, op):
    ans = 0
    count = 0
    for i in range(11, -1, -1):
        for j in range(12):
            if j > 11 - i:
                count += 1
                ans += mat[i][j]

    return ans if op == 'S' else ans / count
            

def main():
    op = input()
    mat = [[float(input()) for j in range(12)] for i in range(12)]
    print(f"{solve(mat, op):.1f}")


if __name__ == "__main__":
    main()

