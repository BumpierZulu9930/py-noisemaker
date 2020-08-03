#!/bin/bash

source noisemaker/bin/activate

echo Input file output path, please!

read -p 'Output Path: ' outputPath

echo Input an effect please! Start each effect with a "--" and provide a float if needed. Also can leave empty for plain noise!

read -p 'Effects: ' effects

echo Ok, doing stuff now!

noisemaker --name $outputPath $effects

echo "Done! <3"
