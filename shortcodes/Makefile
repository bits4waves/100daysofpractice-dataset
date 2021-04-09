ifndef IG_USER
$(error IG_USER is not set)
endif

PYTHON=python
SRC=../src
SHORTCODES_ORIG=shortcodes-orig.txt
SHORTCODES_TEST=shortcodes-test.txt

all: shortcodes-orig

shortcodes-orig:
	$(PYTHON) $(SRC)/get-shortcodes.py

shortcodes-test: $(SHORTCODES_ORIG)
	head --lines=10 $(SHORTCODES_ORIG) > $(SHORTCODES_TEST)

clean:
	rm -rf \#100daysofpractice/
