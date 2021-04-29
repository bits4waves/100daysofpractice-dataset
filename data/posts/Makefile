ifndef IG_USER
$(error IG_USER is not set)
endif

PYTHON=python
SRC=../../src
GET_POSTS_PY=$(SRC)/get-posts.py
GET_POSTS_CSV_PY=$(SRC)/get-posts-csv.py
POSTS_JSON=posts.json
POSTS_CSV=posts.csv
OBJECTS = $(POSTS_JSON)

all: $(OBJECTS)

$(POSTS_JSON):
	$(PYTHON) $(GET_POSTS_PY)

$(POSTS_CSV): $(POSTS_JSON)
	$(PYTHON) $(GET_POSTS_CSV_PY)

clean:
	rm -rf $(OBJECTS)
