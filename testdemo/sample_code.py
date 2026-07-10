#!/usr/bin/env python3
"""Sample code for smoke test."""


def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


def main() -> None:
    """Main entry point."""
    a, b = 3, 5
    print(f"add({a}, {b}) = {add(a, b)}")
    print(f"multiply({a}, {b}) = {multiply(a, b)}")


if __name__ == "__main__":
    main()
