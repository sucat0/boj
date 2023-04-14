from sys import stdin


class Calc:
    @staticmethod
    def factorial(n: int) -> int:
        result = 1
        for num in range(1, n+1):
            result *= num

        return result
    
    @staticmethod
    def combination(n: int, m: int) -> int:
        return Calc.factorial(n) // (Calc.factorial(n - m) * Calc.factorial(m))


n, m = map(int, stdin.readline().split())

print(Calc.combination(n, m))
