#!/bin/bash

while read p; do 
	sed -i 's+https://www.musicstore.sm+musica+g' musica.txt
done <musica.txt
