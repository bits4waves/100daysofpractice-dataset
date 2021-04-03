all: dataset

dataset:
	instaloader --no-profile-pic --no-pictures --no-videos --no-captions --count 1000 "#100daysofpractice"

clean: FORCE
	rm -rf \#100daysofpractice/

FORCE:
