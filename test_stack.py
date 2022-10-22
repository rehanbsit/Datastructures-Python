import pytest
from stack import Stack
from exceptions import NoneElementException, EmptyStackException


class TestStack:

    def test_size(self):
        stack = Stack()
        assert stack.size() == 0
        stack.push(2)
        assert stack.size() == 1

    def test_push(self):
        element = None
        stack = Stack()
        with pytest.raises(NoneElementException):
            stack.push(element)
        assert stack.size() == 0
        element = 1
        stack.push(element)
        assert stack.size() == 1

    def test_pop(self):
        stack = Stack()
        with pytest.raises(EmptyStackException):
            stack.pop()
        assert stack.size() == 0
        stack.push(2)
        assert stack.pop() == 2

    def test_peek(self):
        stack = Stack()
        with pytest.raises(EmptyStackException):
            stack.peek()
        assert stack.size() == 0
        stack.push(25)
        assert stack.peek() == 25

    def test_empty(self):
        stack = Stack()
        assert stack.empty() is True
        stack.push(1)
        assert stack.empty() is False
