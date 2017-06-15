# Source folder path from root directory
r = ./
p = ./Plot
d = ./DataFiles

# Provide list of cities, id and year here
place = -p 'st johns, halifax, toronto, vancouver'
id = -i '48871 50620 48549 888'
year = -y '2013 2017'

accGDD: calculation_accGDD
	python $(r)accGDD.py

plot_min_max: autodownload
	python $(r)min_max.py

autodownload : init
	python $(r)autodownload.py $(year) $(place) $(id)

calculation_accGDD: plot_min_max
	python $(r)calculationGDD.py


Different_T_base:
	python $(r)secondary3.py

clean:
	rm -rf $(p)
	rm -rf $(d)

init:   clean
	mkdir -p $(p)
	mkdir -p $(d)
test: 
	python $(r)test_GDD.py  && echo "CALCULATE_GDD... PASSED" || echo "CALCULATE_GDD... FAILED"
      
	
all:    accGDD 
