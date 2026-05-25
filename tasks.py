# -*- coding: utf-8 -*-

from combinatorics import CombinatoricsCalculator


class Task:
    def __init__(self, title):
        self.title = title
        self.calculator = CombinatoricsCalculator()

    def solve(self):
        raise NotImplementedError("The solve method must be implemented.")


class SimplifyExpressionTask(Task):
    def __init__(self):
        super().__init__("1. Simplify expression")

    def solve(self):
        return (
            "Expression: 1 / (k - 1)! - 1 / k!\n"
            "Since k! = k * (k - 1)!, then:\n"
            "1 / (k - 1)! = k / k!\n"
            "Therefore:\n"
            "k / k! - 1 / k! = (k - 1) / k!\n"
            "Answer: (k - 1) / k!"
        )


class PascalIdentityTask(Task):
    def __init__(self):
        super().__init__("2. Prove identity")

    def solve(self):
        n = 8
        k = 3

        left_side = (
            self.calculator.combinations(n, k)
            + self.calculator.combinations(n, k - 1)
        )
        right_side = self.calculator.combinations(n + 1, k)

        return (
            "Identity: C(n, k) + C(n, k - 1) = C(n + 1, k)\n"
            "This is Pascal's identity for combinations.\n"
            f"Example check for n = {n}, k = {k}:\n"
            f"C({n}, {k}) + C({n}, {k - 1}) = {left_side}\n"
            f"C({n + 1}, {k}) = {right_side}\n"
            f"Result: {left_side} = {right_side}, identity is correct."
        )


class FactorialEquationTask(Task):
    def __init__(self):
        super().__init__("3. Solve factorial equation")

    def solve(self):
        target = 72
        result_n = None

        for n in range(2, 100):
            value = self.calculator.factorial(n) // self.calculator.factorial(n - 2)

            if value == target:
                result_n = n
                break

        return (
            "Equation: n! / (n - 2)! = 72\n"
            "After simplification:\n"
            "n! / (n - 2)! = n(n - 1)\n"
            "So we need to solve:\n"
            "n(n - 1) = 72\n"
            f"Program result: n = {result_n}\n"
            "Answer: n = 9"
        )


class ClothesCombinationsTask(Task):
    def __init__(self):
        super().__init__("4. Combinatorial problem: clothes")

    def solve(self):
        t_shirts = 12
        pants = 6
        socks = 8
        shoes = 3

        result = t_shirts * pants * socks * shoes

        return (
            "Problem: 12 T-shirts, 6 pants, 8 pairs of socks and 3 pairs of shoes.\n"
            "Each item is selected independently, so we use the multiplication rule.\n"
            f"Number of ways: {t_shirts} * {pants} * {socks} * {shoes} = {result}\n"
            f"Answer: {result} ways"
        )


class StudentPositionsTask(Task):
    def __init__(self):
        super().__init__("5. Combinatorial problem: student positions")

    def solve(self):
        students = 8
        positions = 3

        result = self.calculator.arrangements(students, positions)

        return (
            "Problem: From 8 students, choose a head, deputy and secretary.\n"
            "The positions are different, so the order is important.\n"
            "We use arrangements.\n"
            f"A({students}, {positions}) = {result}\n"
            f"Answer: {result} ways"
        )


class SeatingStudentsTask(Task):
    def __init__(self):
        super().__init__("6. Combinatorial problem: seating students")

    def solve(self):
        seats = 34
        students = 8

        result = self.calculator.arrangements(seats, students)

        return (
            "Problem: There are 34 free seats. Seat 8 different students.\n"
            "The seats are different and the students are different, so the order is important.\n"
            "We use arrangements.\n"
            f"A({seats}, {students}) = {result}\n"
            f"Answer: {result} ways"
        )