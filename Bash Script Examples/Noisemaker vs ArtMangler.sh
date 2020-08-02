#!/bin/bash

source noisemaker/bin/activate

echo Input file output path, please!

read -p 'Output Path: ' outputPath

echo Input an effect please! Start each effect with a "--" and provide a float if needed. Also can leave empty for plain noise!

read -p 'Effects: ' effects

echo Ok, doing stuff now!

noisemaker --name $outputPath $effects

read -p "Do you want to mangle it further? [y/n] " -n 1 -r
echo    # (optional) move to a new line
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    exit 1
fi

counter=1
while [ $counter -le 3 ]
do
	artmangler --name $outputPath random $outputPath
	((counter++))
done

echo Done! <3