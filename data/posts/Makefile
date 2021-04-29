ifndef IG_USER
$(error IG_USER is not set)
endif

PYTHON=python
SRC=../../src
GET_POSTS_PY=$(SRC)/get-posts.py
POSTS_JSON=posts.json
OBJECTS = $(POSTS_JSON)

all: $(OBJECTS)

$(POSTS_JSON):
	$(PYTHON) $(GET_POSTS_PY)

clean:
	rm -rf $(OBJECTS)
