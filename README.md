Alex C. Viana
=============

This project is intended to serve as a software engineering portfolio for Alex C. Viana. You can find my [LinkedIn here](https://www.linkedin.com/in/alex-viana-0831b849/) and a copy of my latest [resume here](https://www.dropbox.com/s/ylec8nsxv3jnht8/alex-viana-resume-2019-01-v3-technical.pdf?dl=0).

### Production Code

My most recent public production code contributions can be found in [this repository](https://github.com/TerbiumLabs/python-matchlightsdk/commits?author=acviana), specifically in 2019 Q1. My latest MRs against the project are [here](https://github.com/TerbiumLabs/python-matchlightsdk/pulls?q=is%3Apr+is%3Aclosed+author%3Aacviana).

They are a mix of bug fixes, incremental feature updates, new features, extensive example documentation, and tech debt issues. This is one of the [larger MRs](https://github.com/TerbiumLabs/python-matchlightsdk/pull/75) where I rewrote our test suite to use a more modern framework and unblock a downstream MR to fix a critical security vulnerability.

I also served as the release manager for this product.

### Larger Projects

These are two larger projects I think provide good insight into my thought process and organization:

- HubBucket: [This repository](https://github.com/acviana/hub-bucket) contains a project that runs a Flask REST API that returns and calculates GitHub user statistics gathered from either the GitHub v3 REST or v4 GraphQL APIs

- `aws_big_data_architecture.md`: This writing assignment in this repo lays out a potential AWS architecture intended to solve a variety of different use big data use cases in data science, production deployment, analytics, and monitoring.

### Programming Exercises

The following modules in this repo are mostly self-motived attempts to work through coding puzzles and computer science problems. All modules were written with Python 3.7 and contain tests where ever appropriate.

This module in an attempt to implement a binary object class:

 - `binary_math.py`: A class that implements binary math using strings at the underlaying data structure [Work in Progress].

These problems were taken from the book "Classic Computer Science Problems in Python" (CCSPIP):

 - `fibonacci.py`: Various ways of generating the Fibonacci series.
 - `dna_compression.py`: ASCII to binary DNA compression exercise from CCSPIP.
 - `binary_search.py`: Implements binary search on sorted iterables.

Problems are taking from around the Internet, interview questions, things I'm interested in:

 - `calculator.py`: Puzzle to write an "calculator" that performs addition and subtraction on an input string of numbers.
 - `generator.py`: A number vision puzzle using generators.
 - `knights_walk.py`: Check if a knight's walk is possible for an arbitrary chessboard using recursion.
 - `password_checker.py`: A password input validation puzzle.
 - `robot.py`: An object orienting programming puzzle that moves a "robot" with text input.
 - `word_frequency.py`: A word frequency counter puzzle.
