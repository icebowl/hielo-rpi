#!/bin/bash
for IP in  216 218 219 220 221 222 223 224 226 230
do
	echo $IP
	python3 sphere_surface_cla.py 192.168.7.$IP

done





python3 sphere_surface_cla.py 192.168.7.205
python3 sphere_surface_cla.py 192.168.7.206
python3 sphere_surface_cla.py 192.168.7.207
python3 sphere_surface_cla.py 192.168.7.209
python3 sphere_surface_cla.py 192.168.7.212
python3 sphere_surface_cla.py 192.168.7.215
python3 sphere_surface_cla.py 192.168.7.216
python3 sphere_surface_cla.py 192.168.7.217
python3 sphere_surface_cla.py 192.168.7.218
python3 sphere_surface_cla.py 192.168.7.219
python3 sphere_surface_cla.py 192.168.7.220
python3 sphere_surface_cla.py 192.168.7.226

