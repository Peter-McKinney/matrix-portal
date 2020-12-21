LIB=/Volumes/CIRCUITPY/lib

if test -d "$LIB"; then
	echo "Copying lib to volume..."
	cp -R lib/* $LIB
else 
	echo "$LIB does not exist."
fi
