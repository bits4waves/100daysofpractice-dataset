ifndef IG_USER
$(error IG_USER is not set)
endif

PYTHON=python
SRC=../src
GET_SHORTCODES_PY=$(SRC)/get-shortcodes.py
SHORTCODES_ORIG=shortcodes-orig.txt
SHORTCODES_TEST=shortcodes-test.txt
SHORTCODES_SORT=shortcodes-sort.txt
SHORTCODES_UNIQ=shortcodes-uniq.txt

all: shortcodes-orig shortcodes-test shortcodes-sort shortcodes-uniq

shortcodes-orig:
	$(PYTHON) $(GET_SHORTCODES_PY)

shortcodes-test: $(SHORTCODES_ORIG)
	head --lines=10 $(SHORTCODES_ORIG) > $(SHORTCODES_TEST)

shortcodes-sort: $(SHORTCODES_ORIG)
	sort $(SHORTCODES_ORIG) > $(SHORTCODES_SORT)

shortcodes-uniq: $(SHORTCODES_SORT)
	uniq $(SHORTCODES_SORT) > $(SHORTCODES_UNIQ)

clean:
	rm -rf $(SHORTCODES_ORIG) $(SHORTCODES_TEST) $(SHORTCODES_SORT) $(SHORTCODES_UNIQ)
