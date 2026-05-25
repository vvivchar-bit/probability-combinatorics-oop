# -*- coding: utf-8 -*-

from tasks import (
    SimplifyExpressionTask,
    PascalIdentityTask,
    FactorialEquationTask,
    ClothesCombinationsTask,
    StudentPositionsTask,
    SeatingStudentsTask,
)


def print_separator():
    print("-" * 70)


def main():
    print("Independent Work")
    print("Topic 1. Probability Theory and Mathematical Statistics")
    print("Object-Oriented Programming Example")
    print_separator()

    tasks = [
        SimplifyExpressionTask(),
        PascalIdentityTask(),
        FactorialEquationTask(),
        ClothesCombinationsTask(),
        StudentPositionsTask(),
        SeatingStudentsTask(),
    ]

    for task in tasks:
        print(task.title)
        print(task.solve())
        print_separator()


if __name__ == "__main__":
    main()