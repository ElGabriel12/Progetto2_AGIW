#!/bin/bash

while read p; do 
	sed -i 's+https://www.hoepli.it/libro/++g' libri.txt
done <libri.txt
