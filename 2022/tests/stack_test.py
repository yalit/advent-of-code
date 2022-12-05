import unittest
from libraries.stack import Stack


class TestStack(unittest.TestCase):
    def test_create_stack(self):
        stack = Stack()
        self.assertEqual(0, stack.len())

    def test_add_and_peek(self):
        stack = Stack()
        stack.add("A")
        self.assertEqual(1, stack.len())
        self.assertEqual("A", stack.peek())
        self.assertEqual(1, stack.len())

    def test_pop(self):
        stack = Stack()
        stack.add("A")
        self.assertEqual(1, stack.len())
        popped = stack.pop()
        self.assertEqual(0, stack.len())
        self.assertEqual("A", popped)


if __name__ == "__main__":
    unittest.main()
