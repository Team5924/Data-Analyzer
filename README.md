# Data-Analysis

Custom Python solution for analyzing scouting data.

## Table of Contents

1. [Getting Started](#getting-started)
2. [How It Works](#how-it-works)
3. [Python Packages](#python-packages)

## Getting Started
- Branch off from `dev`
- Name the branch `[YYYY]-[name of season]-analysis`
  - e.g. `2022-Rapid-React-Analysis`
  
## How It Works
  This application utilizes Jupyter Notebooks and custom made Python packages to process data from scouting for analysis. Python packages are used to organize and define custom functions for data processing. i.e. `filter.team()`, `filter.match()`, etc... These functions are designed to be reproducible, republicable, and reusable. While the Python is used for defining functions, the Jupyter Notebook is where these functions will be called/used.
  
### Python Packages

#### Creating a directory to store Python packages
While a directory for storing Python packages already exists in this repo, here is how you can make them on your own from scratch

- Create a new directory (name does not matter)
- Create a new file `__init__.py` and store it in the directory
  - this informs Python that the directory contains packages

##### Naming Convention
TL;DR: `[verb].[noun]()`

`process.py` contains the function `entry()`. When called, it's written as `process.entry()`. This method of naming makes it clear what is being performed on and how.

Another example: `filter.py` contains the function `team()`. When called, it's `filter.team()`.

##### Using a Python package
```
# Importing the package from local directory
from [package_directory] import [package_name]

...

# Calling the function
[package_name].[method_name]()
```
