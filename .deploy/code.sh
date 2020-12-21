#/bin/bash
CODE=/Volumes/CIRCUITPY

if test -d "$CODE"; then
	echo "Copying code to volume..."
	cp code.py $CODE
else 
	echo "$CODE does not exist."
fi
