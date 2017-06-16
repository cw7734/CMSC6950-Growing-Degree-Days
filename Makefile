# Source folder path from root directory
r = ./
p = ./Plot
d = ./DataFiles

# Provide list of cities, id and year here
place = -p 'st johns, halifax, toronto, vancouver'
id = -i '48871 50620 48549 888'
year = -y '2013 2017'

LinearRegression: Different_T_base
	python $(r)secondary6.py

Different_T_base: accGDD
	python $(r)secondary3.py

# accGDD will plot the accumulated GDD for selected cities from year 2013 to 2016
accGDD: calculation_accGDD
	python $(r)accGDD.py

# plot_min_max will plot the max amd min daily temperature for selected cities in different cities.

plot_min_max: autodownload
	python $(r)min_max.py

#autodownload will download the data from web automatically.
autodownload : init
	python $(r)autodownload.py $(year) $(place) $(id)

calculation_accGDD: plot_min_max
	python $(r)calculationGDD.py

clean:
	rm -rf $(p)
	rm -rf $(d)

init:   clean
	mkdir -p $(p)
	mkdir -p $(d)
test: 
	python $(r)test_GDD.py  && echo "CALCULATE_GDD... PASSED" || echo "CALCULATE_GDD... FAILED"
      
	
all:   Different_T_base
