from sys import stdin

n, m = map(int, stdin.readline().split())

passwd_dict = {}
for _ in range(n):
    site, passwd = stdin.readline().split()
    passwd_dict[site] = passwd

for _ in range(m):
    site = stdin.readline().rstrip()
    print(passwd_dict[site])