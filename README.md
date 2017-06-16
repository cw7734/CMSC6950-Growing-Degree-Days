# CMSC6950-Growing-Degree-Days

This is a project for the course CMSC6950. From wikipedia.org: Growing degree day(s) (GDD), also called growing degree units (GDUs), are a heuristic tool in phenology. GDD are a measure of heat accumulation used by horticulturists, gardeners, and farmers to predict plant and animal development rates such as the date that a flower will bloom, or a crop will reach maturity.

### Group member (A~Z)
* chen wei
* Huizhong Liu
* Maulik Rawal
* Md Kamrul Hasan
* Thanjida Akhter
* Yuan Zhi
* Xiao Wang




### Install packages
* sudo apt install wget ( Mac or Linux)
* pip install wget (linux)
* pip install bokeh (windows)
* pip install pyqt5

### Use python packages
1. pandas
2. numpy
3. getopt
4. shutil
5. matplotlib
6. itertools
7. weget
8. time
9. os, sys, stat
10. csv
11. argparse
12. math

### repository
1. master:
     code, test

2. gh-page: 
     data, plot, report


### Create the local repository
1. cd desktop
2. mkdir folderName
3. git init
4. git remote add origin https://github.com/cw7734/CMSC6950-Growing-Degree-Days.git
5. git pull

### Create your own branch
1. git branch branch_name







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

```


Tasks Completed:
----------
 
<table>
<th colspan="2" align=left>Minimum Core Tasks</th>
<tr><td>1. download data automatically</td><td>autodownload.py (under master branch)</td></tr>
<tr><td>2. plot an annual cycle of min/max daily temperature</td><td>min_max.py (under master branch)</td></tr>
<tr><td>3. write a code to calculated GDD</td><td>calculationGDD.py (under master branch)</td></tr>
<tr><td>4. plot accumulated GDD</td><td>accGDD.py (under master branch)</td></tr>
<tr><td>5. use git hub</td><td>we are workig on the same repository in Git Hub</td></tr>
<tr><td>6. create a LaTex report</td><td>report.tex (under gh-pages branch)</td></tr>
<tr><td>7. create a web based presentation</td><td>CMSC6950_web_based_presentation.html (under gh-pages branch)</td></tr>
<tr><td>8. implement your workflow as a makefile</td><td>makefile (under master branch)</td></tr>
<tr><td>9. create a test suite</td><td>test_GDD.py (under master branch)</td></tr>
<tr><td>10 adding documentation in source code and Readme.md</td><td>we added commit and text to explian our work in overall files</td></tr>
<th colspan="2" align=left>Secondary Tasks</th>
<tr><td>secondary task 3</td><td>secondary3.py (under master branch)</td></tr>
<tr><td>secondary task 6</td><td>secondary6.py (under master branch)</td></tr>

### Tasks
1. Minimum Core Tasks

	* Download temperature 
	* Min/max temperature
	* Calculate the GDD
	* Plot the GDD
	* Plot the accumulated GDD
	* Use version control (git) and collaboration tools(GitHub) throught this project
	* Create a LaTeX report summarizing the results of your project
	* Create a web based presenation for our results
	* Implement our entire workflow as a Makefile and project is reproducible.
	* Create a test suite to demonstrate our GDD calculation works as intended
	* Create a Readme.md file to explain how to use/build your project.
2. Secondary Tasks

	* Explore how GDD calculation depends on the choice of T_base
	* Linear Regression
</table> 






