# Source folder path from root directory
r = ./


# Provide list of cities, id and year here
cityName = -p 'St.Johns,Halifax,Toronto,Vancouver'
stationId = -i '48871 50620 48549 888'
year = -y '2013 2013'

autodownload :
	python $(r)autodownload.py $(year) $(place) $(id)
plot_min_max:
	python $(r)min_max.py
calculation_accGDD:
	python $(r)calculationGDD.py
AccGDD_plot:
	python $(r)AccGDD_plot.py

all: autodownload plot_min_max calculation_accGDD AccGDD_plot
