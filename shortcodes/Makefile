ifndef IG_USER
$(error IG_USER is not set)
endif

all: dataset

dataset:
	source ../venv/bin/activate
	python get-shortcodes.py

clean:
	rm -rf \#100daysofpractice/
