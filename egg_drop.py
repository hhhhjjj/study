class Solution:
    def superEggDrop(self, K, N, S=0):
    #     import math
    #     N = N + 1
    #     if N % K == 0 and N > K:
    #         every_layer = N / K
    #         if every_layer == N:
    #             return N - 1 + S
    #         elif 2 < every_layer <= 4:
    #             return K - 1 + 2 + S
    #         elif 1 <= every_layer <=2:
    #             return K - 1 + S + 1
    #         elif every_layer > 4:
    #             return Solution().superEggDrop(K, every_layer - 1, S + K - 1)
    #     elif N <= K:
    #         return S + math.ceil(math.log(N, 2))
    #
    #     elif N % K != 0 and N > K:
    #         max_layer = math.ceil(N/K)
    #         if max_layer == N:
    #             return N - 1 + S
    #         elif 2 < max_layer <= 4:
    #             return 2 + K - 1 + S
    #         elif 1 <= max_layer <=2:
    #             return K - 1 + S + 1
    #         elif max_layer > 4:
    #             return Solution().superEggDrop(K, max_layer - 1, S + K - 1)
        ts = [0] * K
        ts.append(0)
        for i in range(1, K + 1):
            ts[i] = ts[i - 1] * 2 + 1
        if N <= ts[-1]:
            for i in ts:
                if i >= N:
                    m = ts.index(i)
                    break
        else:
            ans = ts[-1]
            m = K
            while N > ans:
                m += 1
                ans = self.bss(K, m)
        return m

    def ass(self, i):
        ts = 1
        for i in range(1, i):
            ts = ts * 2 + 1
        return ts

    def bss(self, i, j):
        if i == j:
            return self.ass(i)
        elif i == 1 and j > i:
            return j
        else:
            ans = self.bss(i, j - 1) + self.bss(i - 1, j - 1) + 1
        return ans


print(Solution().superEggDrop(2, 100))



