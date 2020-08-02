#!/bin/bash
source noisemaker/bin/activate

echo Enter in the source image

read -p 'Input Path: ' sourceImage

echo Enter in the output file path

read -p 'Output Path: ' outputImage

echo Enter any other options! Start each query with "--". Can also leave empty!
read -p 'Extra options: ' options

echo Ok, doing the stuff now!

counter=1
while [ $counter -le 3 ]
do
	artmangler --name $outputImage $options random $sourceImage
	sourceImage=$outputImage
	((counter++))
done