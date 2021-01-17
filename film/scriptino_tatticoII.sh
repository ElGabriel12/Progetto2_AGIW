#!/bin/bash

while read p; do 
	sed -i 's+https://www.themoviedb.org/movie+film+g' film.txt
done <film.txt
