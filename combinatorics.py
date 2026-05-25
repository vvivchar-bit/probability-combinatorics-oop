# -*- coding: utf-8 -*-


class CombinatoricsCalculator:
    """
    Class for calculating basic combinatorics formulas:
    factorials, permutations, arrangements and combinations.
    """

    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")

        result = 1

        for i in range(1, n + 1):
            result *= i

        return result

    def permutations(self, n):
        """
        P_n = n!
        """
        return self.factorial(n)

    def arrangements(self, n, m):
        """
        A_n^m = n! / (n - m)!
        """
        if m < 0 or m > n:
            raise ValueError("Invalid values: m must be between 0 and n.")

        return self.factorial(n) // self.factorial(n - m)

    def combinations(self, n, m):
        """
        C_n^m = n! / (m! * (n - m)!)
        """
        if m < 0 or m > n:
            raise ValueError("Invalid values: m must be between 0 and n.")

        return self.factorial(n) // (
            self.factorial(m) * self.factorial(n - m)
        )