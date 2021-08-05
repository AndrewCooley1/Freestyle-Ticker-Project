# Freestyle-Ticker-Project

Freestyle Project based on stock ticker inputs (ADD MORE HERE)

Trying to update my repository. I could update it in Andrew's repo. but mine is not happenning. '


## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](https://github.com/AndrewCooley1/Freestyle-Ticker-Project) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd freestyle-ticker-project
```

Use Anaconda to create and activate a new virtual environment, perhaps called "stock-sentiments-env":

```sh
conda create -n stock-sentiments-env 
conda activate stock-sentiments-env 
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above).

## Setup

ADD NOTES ABOUT TICKER INPUT HERE

## Usage

Run the Python script:

```py
python stock.py

```

 Please input any stock ticker symbol and the progam will pull the applicable information and provide an investor sentiment.

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment.
