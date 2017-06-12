# Source folder path from root directory
<<<<<<< HEAD
s = ./source/
r = ./source/Report/
d = ./DataFiles/
p = ./Plots/
t = ./source/Test/

# Input variables and their values
startYear = 2015
endYear = 2015
baseTemp = 10
# Provide list of Station ID and City Name for GDD Calculation
stationId = -st 50089 51157 50430 
cityName = -ct 'St_Johns' 'HALIFAX' 'TORONTO' 
# Define the color each city. 
gColor = -gc 'blue' 'red' 'green'

all : report.pdf

# First we need to download data from web and calculate the GDD value
$(d)GDD_Data_St_Johns.csv : $(s)download_data.py $(s)calculate_GDD.py
	python $(s)download_data.py $(startYear) $(endYear) $(stationId) $(cityName) 
	python $(s)calculate_GDD.py $(baseTemp) $(stationId) $(cityName)
	
$(d)GDD_Data_HALIFAX.csv : $(s)download_data.py $(s)calculate_GDD.py
	python $(s)download_data.py $(startYear) $(endYear) $(stationId) $(cityName)
	python $(s)calculate_GDD.py $(baseTemp) $(stationId) $(cityName)	

$(d)GDD_Data_TORONTO.csv : $(s)download_data.py $(s)calculate_GDD.py
	python $(s)download_data.py $(startYear) $(endYear) $(stationId) $(cityName) 
	python $(s)calculate_GDD.py $(baseTemp) $(stationId) $(cityName)

# After calculate the GDD value, we store the data in a csv file, and we will extract data and do the plot
# for minimun and maximun daily temperature for our cities.	

$(p)min_max_plot_St_Johns.png : $(s)extract_data_from_csv.py $(s)min_max_plot.py $(d)GDD_Data_St_Johns.csv
	mkdir -p Plots
	python $(s)min_max_plot.py $(stationId) $(cityName)
	
$(p)min_max_plot_HALIFAX.png : $(s)extract_data_from_csv.py $(s)min_max_plot.py $(d)GDD_Data_HALIFAX.csv
	mkdir -p Plots
	python $(s)min_max_plot.py $(stationId) $(cityName)

$(p)min_max_plot_TORONTO.png : $(s)extract_data_from_csv.py $(s)min_max_plot.py $(d)GDD_Data_TORONTO.csv
	mkdir -p Plots
	python $(s)min_max_plot.py $(stationId) $(cityName)

# Here we will do the GDD plot for each city and plot in one graph.
$(p)GDD_Plot.png : $(s)extract_data_from_csv.py $(s)gdd_plot.py $(d)GDD_Data_St_Johns.csv $(d)GDD_Data_HALIFAX.csv $(d)GDD_Data_TORONTO.csv
	mkdir -p Plots
	python $(s)gdd_plot.py $(stationId) $(cityName) $(gColor)



# Save images into report file and update the Latex file
	
report.pdf : $(r)report.tex $(p)GDD_Plot.png $(p)min_max_plot_St_Johns.png $(p)min_max_plot_HALIFAX.png $(p)min_max_plot_TORONTO.png 

	

# Remove the redundant file	
clean : 
	rm -rf *.csv $(s)__pycache__ DataFiles Plots
	rm -f report.log report.aux report.pdf report.toc


help:
	@echo "Please make sure you have installed pdflatex program.
	@echo "# Calling the Makefile"
	@echo "$ make"
	@echo "# Clean the complied and data files"
	@echo "#$ make clean"
	@echo "# Calling by file name"
	@echo "#$ make report.pdf"
=======
r = ./


# Provide list of cities, id and year here
place = -p 'st johns, halifax, toronto, vancouver'
id = -i '48871 50620 48549 888'
year = -y '2013 2017'

autodownload :
	python $(r)autodownload.py $(year) $(place) $(id)
plot_min_max:
	python $(r)min_max.py

all: autodownload plot_min_max
>>>>>>> xiaowang
