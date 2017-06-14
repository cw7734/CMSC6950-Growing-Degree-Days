# Source folder path from root directory
r = ./
p = ./Plot
d = ./DataFiles

# Provide list of cities, id and year here
place = -p 'st johns, halifax, toronto, vancouver'
id = -i '48871 50620 48549 888'
year = -y '2013 2017'

plot_min_max: autodownload
	python $(r)min_max.py

autodownload : init
	python $(r)autodownload.py $(year) $(place) $(id)

calculation_accGDD:
	python $(r)calculationGDD.py

AccGDD_plot_single:
	python $(r)AccGDD_plot_single.py

AccGDD_plot_all:
	python $(r)AccGDD_plot_all.py

Different_T_base:
	python $(r)secondary3.py

clean:
	rm -rf $(p)
	rm -rf $(d)

init:   clean
	mkdir -p $(p)
	mkdir -p $(d)

all: clean init autodownload plot_min_max calculation_accGDD AccGDD_plot_single AccGDD_plot_all Different_T_base
