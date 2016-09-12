class EvenFibonacciNumbersAdder:

    @staticmethod
    def get_sum():
        '''
        :return: the sum of all even Fibonnaci numbers not exceeding 4 million, starting from 1, 2
        '''

        tail = 2
        current = 3

        sum_even = 2

        thousand = 1000
        ceiling = 4 * thousand * thousand  # 4 million

        while current <= ceiling:
            if current % 2 == 0:
                sum_even += current

            head = tail
            tail = current
            current = head + tail

        return sum_even

if __name__ == '__main__':
    print(EvenFibonacciNumbersAdder.get_sum())
