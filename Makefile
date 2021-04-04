all: dataset

dataset:
	instaloader --login ${IG_USER} --no-profile-pic --no-pictures --no-videos --no-captions "#100daysofpractice"

clean:
	rm -rf \#100daysofpractice/
