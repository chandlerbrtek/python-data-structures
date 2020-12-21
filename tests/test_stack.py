#!/usr/bin/env python

"""Tests for `python_data_structures` package."""

import pytest
from click.testing import CliRunner
from python_data_structures.stack import Stack

def test_stack_is_empty_when_initialized():
    mystack = Stack()
    assert mystack.isEmpty()