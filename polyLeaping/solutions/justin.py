# Copyright 2021
# Justin Baum

from math import gcd

def sol(n, j):
    return n - (n // gcd(n,j))

def main():
    case_count = int(input())
    for i in range(case_count):
        (n,j) = map(int, input().split())
        print(sol(n,j))

if __name__ == "__main__":
    main()
