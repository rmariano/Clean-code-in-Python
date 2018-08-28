Clean Code in Python
--------------------

Setup
=====

Create a virtual environment, and once activated run::

    make setup

This will install the common dependencies. Besides this, each chapter might
have additional ones, for which another ``make setup`` will have to be run
inside that particular directory.

Each chapter has its corresponding directory given by its number.

Inside each chapter directory, tests can be run by::

    make test

This requires the ``make`` application installed (in Unix environments).
In environments without access to the ``make`` command, the same code can be
tested by running the commands on the ``Makefile``::

    python -m doctest *.py
    python -m unittest *.py


Chapters Index
==============

* Chapter 01; Introduction, Code Formatting, and Tools
* Chapter 02: Pythonic Code
* Chapter 03: Traits of Clean Code
* Chapter 04: The SOLID Principles
* Chapter 05: Decorators
* Chapter 06: Getting More out of our Objects with Descriptors
* Chapter 07: Using Generators
* Chapter 08: Unit Testing and Refactoring
* Chapter 09: Common Design Patterns
* Chapter 10: Clean Architecture
