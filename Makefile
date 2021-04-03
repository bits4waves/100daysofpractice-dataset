all: dataset

dataset:
	instaloader --no-profile-pic --no-pictures --no-videos --no-captions "#100daysofpractice"

clean: FORCE
	rm -rf \#100daysofpractice/

FORCE:
