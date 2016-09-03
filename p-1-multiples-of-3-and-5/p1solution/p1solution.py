#! /usr/bin/env python3


class P1Solution:
    CEILING = 1000
    SMALLEST_DIVIDER = 3
    BIGGEST_DIVIDER = 5

    def naive(self):
        var_sum = 0

        for i in range(self.SMALLEST_DIVIDER, self.CEILING):
            if i % self.SMALLEST_DIVIDER == 0 or i % self.BIGGEST_DIVIDER == 0:
                var_sum = var_sum + i

        print("sum is: %s" % var_sum)
        return var_sum

if __name__ == "__main__":
    p1solution = P1Solution()
    p1solution.naive()
