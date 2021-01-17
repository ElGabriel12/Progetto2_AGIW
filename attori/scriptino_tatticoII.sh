#!/bin/bash

while read p; do 
	sed -i 's+https://www.themoviedb.org/person+attori+g' attori.txt
done <attori.txt
