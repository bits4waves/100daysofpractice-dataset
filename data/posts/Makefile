ifndef IG_USER
$(error IG_USER is not set)
endif

PYTHON=python
SRC=../../src
GET_POSTS_PY=$(SRC)/get-posts.py
GET_POSTS_CSV_PY=$(SRC)/get-posts-csv.py
POSTS_JSON=posts.json
POSTS_CSV=posts.csv
METADATA_TXT=metadata.txt
POSTS_ZIP=posts.zip
FILES_TO_ZIP= $(POSTS_CSV) $(METADATA_TXT)
ZIP_FLAGS=-s 50m
HASHTAGS_CSV=hashtags.csv
OBJECTS = $(POSTS_JSON) $(POSTS_CSV) $(POSTS_ZIP)

all: $(OBJECTS)

$(POSTS_JSON):
	$(PYTHON) $(GET_POSTS_PY)

$(POSTS_CSV): $(POSTS_JSON)
	$(PYTHON) $(GET_POSTS_CSV_PY)
	echo "‘posts.csv’0 generation details" > $(METADATA_TXT)
	echo "Date: "`date` >> $(METADATA_TXT)
	echo "commit: "`git rev-parse HEAD` >> $(METADATA_TXT)

$(POSTS_ZIP): $(POSTS_CSV) $(METADATA_TXT)
	zip $(ZIP_FLAGS) $(POSTS_ZIP) $(FILES_TO_ZIP)

$(HASHTAGS_CSV): $(POSTS_CSV)
	tail -n +2 $(POSTS_CSV) |\
	cut -d ',' -f11 |\
	tr '[:upper:]' '[:lower:]' |\
	tr --delete '"' |\
	tr --delete '' |\
	tr ' ' '\n' |\
	sort |\
	uniq -c |\
	tr --delete '^[:blank:]*' |\
	tr '#' ' ' |\
	tail -n +2 |\
	sort --human-numeric-sort --reverse |\
	tr ' ' ',' \
	> $(HASHTAGS_CSV)

clean:
	rm -rf $(OBJECTS)
