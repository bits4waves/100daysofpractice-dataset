all: dataset

dataset:
	rm -rf \#100daysofpractice/
	instaloader --no-profile-pic --no-pictures --no-videos --no-captions "#100daysofpractice"
