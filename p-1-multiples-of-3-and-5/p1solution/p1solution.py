#! /usr/bin/env python3
import time


class P1Solution:
    CEILING = 1000
    DIVIDER_THREE = 3
    DIVIDER_FIVE = 5

    def optimize_using_mem(self):
        start_time = time.time()
        multiples = set()

        multiples_3 = 3
        while multiples_3 < self.CEILING:
            multiples.add(multiples_3)
            multiples_3 += self.DIVIDER_THREE

        multiples_5 = 5
        while multiples_5 < self.CEILING:
            multiples.add(multiples_5)
            multiples_5 += self.DIVIDER_FIVE

        elapsed_time = time.time() - start_time

        print("%.20f, optimize_using_mem runtime" % elapsed_time)

        return sum(multiples)

    def naive(self):
        start_time = time.time()
        var_sum = 0

        for i in range(self.DIVIDER_THREE, self.CEILING):
            if i % self.DIVIDER_THREE == 0 or i % self.DIVIDER_FIVE == 0:
                var_sum = var_sum + i

        elapsed_time = time.time() - start_time

        print("%.20f, naive runtime" % elapsed_time)
        return var_sum

if __name__ == "__main__":
    p1solution = P1Solution()
    p1solution.naive()
