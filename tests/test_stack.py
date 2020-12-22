#!/usr/bin/env python

"""Tests for `python_data_structures` package."""

import pytest
from click.testing import CliRunner
from python_data_structures.stack import Stack

def test_stack_is_empty_when_initialized():
    stack = Stack()
    assert stack.isEmpty()

def test_stack_is_not_empty_after_push():
    stack = Stack()
    stack.push(1)
    assert not stack.isEmpty()

def test_stack_peek_returns_most_recent_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2

def test_stack_pop_gets_most_recent_push():
    stack = Stack()
    stack.push(123)
    stack.push(456)
    assert stack.pop() == 456

def test_stack_pop_shows_second_most_recent_on_peek():
    stack = Stack()
    stack.push(123)
    stack.push(456)
    stack.pop()
    assert stack.peek() == 123

def test_stack_peek_on_empty_stack_throws_error():
    stack = Stack()

    assert stack.peek() == 123