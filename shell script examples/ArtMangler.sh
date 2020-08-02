#!/bin/bash
source noisemaker/bin/activate

echo Enter in the source image

read -p 'Input Path: ' sourceImage

echo Enter in the output file path

read -p 'Output Path: ' outputImage

echo Enter in any effects! Start each effect with "--". Can also leave blank!
read -p 'Effects: ' effects

echo Ok, doing the stuff now!

artmangler --name $outputImage $effects random $sourceImage