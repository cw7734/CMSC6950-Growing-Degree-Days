# CMSC6950-Growing-Degree-Days

This is a project for the course CMSC6950.

### Group member
*  chen wei
*
*
*
*
*
*




##### Clone GitHub Repository:

```bash
# Make a clone of the repository in a local directory
$ git clone https://github.com/cw7734/CMSC6950-Growing-Degree-Days.git
```


##### Run:

```bash
# To call the Makefile and execute all.
$ make

# To removing all the downloaded data and complied files.
$ make clean

# To run the test case. If there is no reply, that means success.  
$ make test

# To generate files by file name (Ex. report.pdf). 
$ make report.pdf

# To generate interactive plot for Optional Task # 5.
$ bokeh serve source/opTask5.py --show
```



### Follow the "Git Config" file to set up the local git env

### Install wget
* sudo apt install wget
* sudo pip install wget

### clone the branch to your local
1. git fetch origin
2. git checkout -b xiaowang origin/xiaowang, ofcourse you can name your local branch to XXX

### change the autodownload.py to Allow executing file as program
* python autodownload.py
* The all csv file of the 4 cities from 2012 to 2017 will in current file , 24 file in total
