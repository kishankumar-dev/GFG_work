import math

class Solution:
    def isPrime(self, n: int) -> bool:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def factors(self, k: int) -> list[int]:
        factors_list = []
        for i in range(2, k + 1):
            if k % i == 0 and self.isPrime(i):
                factors_list.append(i)
        return factors_list

    def maxKPower(self, N: int, K: int) -> int:
        factors_of_k = self.factors(K)
        n = len(factors_of_k)
        count_of_factors = [0] * n

        for i in range(n):
            factor = factors_of_k[i]
            count = 0
            for j in range(factor, N + 1, factor):
                num = j
                while num >= factor and num % factor == 0:
                    num //= factor
                    count += 1
            count_of_factors[i] = count

        min_count_req = [0] * n
        for i in range(n):
            factor = factors_of_k[i]
            count = 0
            num = K
            while num >= factor and num % factor == 0:
                num //= factor
                count += 1
            min_count_req[i] = count

        ans = float('inf')
        for i in range(n):
            total_count = count_of_factors[i]
            required_count = min_count_req[i]
            ans = min(ans, total_count // required_count)

        return 0 if ans == float('inf') else ans
