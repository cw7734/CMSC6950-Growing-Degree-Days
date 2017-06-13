# Source folder path from root directory
r = ./


# Provide list of cities, id and year here
place = -p 'St.Johns,Halifax,Toronto,Vancouver'
id = -i '48871 50620 48549 888'
year = -y '2013 2017'

autodownload :
	python $(r)autodownload.py $(year) $(place) $(id)
plot_min_max:
	python $(r)min_max.py
calculationGDD:
	python $(r)calculationGDD.py
all: autodownload plot_min_max calculationGDD
