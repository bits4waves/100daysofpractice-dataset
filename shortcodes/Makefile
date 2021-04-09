ifndef IG_USER
$(error IG_USER is not set)
endif

PYTHON=python
SRC=../src

all: shortcodes

shortcodes:
	$(PYTHON) $(SRC)/get-shortcodes.py

clean:
	rm -rf \#100daysofpractice/
