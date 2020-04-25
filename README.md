# T-717-SPST exercises

This repository contains excercises and supporting code for the course T-717-SPST at Reykjavik University. (Work in progress)
* Exercise 1: Digital Audio
* Exercise 2: Audio Manipulation
* Exercise 3: Domain Specific TTS
* Exercise 4: Script Design
* Exercise 5: Record Your Data (*work in progress*)
* Exercise 6: Festival in Docker (*work in progress*)
* Exercise 7: Ossian in AWS (*work in progress*)

## Setting up environment

All the code in this repository is written in Python 3. The recommended approach is to create a python virtual environment:
* Create the virtual environment with one of the following:
    * macOS/Linux: `python3 -m venv .env` or `virtualenv -p python3 ..env`
    * Windows: `python -m venv ./env` or `py -3 -m venv .env`
* Activate it with `source ./env/bin/activate` if you are in the project directory. Otherwise you do `source /path/to/your/environment/bin/activate`.

You can however use Python in any way you see fit and perhaps you may have all the requirements already installed system wide.

Install Python requirements with `pip install -r requirements.txt`. You can of course install any additional python requirements using `pip`, just make sure you have your virtual environment activated when you do.

## Using VS Code + Python (Optional)
To get the best experience make sure that your VS Code workspace is using the correct Python interpreter. If you are using a virtual environment then the workspace setting `python.pythonPath` has to be set to `/path/to/venv/bin/python`. Normally VS Code takes care of doing this for you by recognizing that there is a virtual environment in the workspace. If not:
* Make sure you have the VSC Python extension installed (search for `ms-python.python` in the extension search)
* Press the settings cog in the bottom left inside VSC and select `settings`.
* Select `Workspace`
* search for `pythonpath` and edit the value to point to your python interpreter as explained above.

You can read a more detailed document about python environments in VSC [here](https://code.visualstudio.com/docs/python/environments).

## How to return the assignment
Each assignment has a `README.md` which includes the assignment description and what to turn in. You should return a PDF file where each question in `README.md` that is marked with `(*)` is answered. Try to adhere to the numbering in the `README.md` files. For example, label the answer to the first question in [this assignment](1_digital_audio/README.md) as `1.1`. Furthermore:
* Each assignment has a `template.py` file. This file should be included in your submission with your own code filled in as well as any other helper functions you write to generate your results.
* Some assignments have an `example.py` file that shows how to use some of the functions that are given in `tools.py`.
* In some of the assignments you are asked to generate and save waveforms to disk. In those cases, it is good to include those as well.
Turn in your assignment on the Canvas page for the course.