DEV=/Volumes/CIRCUITPY

if test -d "$DEV"; then
	echo "Copying BMP to volume..."
	cp -R bmps $DEV
	echo "Copying secrets to volume..."
	cp secrets.py $DEV
	echo "Copying fonts to volume..."
	cp -R fonts $DEV
else 
	echo "$DEV does not exist."
fi
