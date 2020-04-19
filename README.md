# T-717-SPST exercises
This repository contains excercises and supporting code for the course T-717-SPST at Reykjavik University.

* Exercise 1: Create a reading list
* Exercise 2: Digital signals
* Exercise 3: Ossian in AWS

## Setting up environment

All the code in this repository is written in Python 3. The recommended approach is to create a python virtual environment:
* Create the virtual environment with one of the following:
    * macOS/Linux: `python3 -m venv .env` or `virtualenv -p python3 ..env`
    * Windows: `python -m venv ./env` or `py -3 -m venv .env`
* Activate it with `source env/bin/activate`

You can however use Python in any way you see fit and perhaps you may have all the requirements already installed system wide.

Install Python requirements with `pip install -r requirements.txt`. You can of course install any additional python requirements using `pip`, just make sure you have your virtual environment activated when you do.

## Using VS Code + Python
To get the best experience make sure that your VS Code workspace is using the correct Python interpreter. If you are using a virtual environment then the workspace setting `python.pythonPath` has to be set to `/path/to/venv/bin/python`. Normally VS Code takes care of doing this for you by recognizing that there is a virtual environment in the workspace. If not:
* Make sure you have the VSC Python extension installed (search for `ms-python.python` in the extension search)
* Press the settings cog in the bottom left inside VSC and select `settings`.
* Select `Workspace`
* search for `pythonpath` and edit the value to point to your python interpreter as explained above.

You can read a more detailed document about python environments in VSC [here](https://code.visualstudio.com/docs/python/environments).