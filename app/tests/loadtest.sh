#!/bin/bash

siege --verbose -p --log=./siege.log -c 10 -t2M -b -m "message" -f urls.txt