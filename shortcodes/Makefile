ifndef IG_USER
$(error IG_USER is not set)
endif

PYTHON=../venv/bin/python
SRC=../src

all: dataset

dataset:
	$(PYTHON) $(SRC)/get-shortcodes.py

clean:
	rm -rf \#100daysofpractice/
