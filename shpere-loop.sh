#!/bin/bash
for IP in  201 203 205 206 209 210 211 212 214 215 216 220 222 224 226
do
	echo $IP
	#python3 sphere_surface_cla.py 192.168.7.$IP
	python3 imageparse.py 192.168.7.$IP 
done
