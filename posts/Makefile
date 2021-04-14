ifndef IG_USER
$(error IG_USER is not set)
endif

PYTHON=python -i
SRC=../src
GET_POSTS_PY=$(SRC)/get-posts.py
POSTS_ORIG=posts-orig.txt
OBJECTS = $(POSTS_ORIG)

all: $(OBJECTS)

$(POSTS_ORIG):
	$(PYTHON) $(GET_POSTS_PY)

clean:
	rm -rf $(OBJECTS)
