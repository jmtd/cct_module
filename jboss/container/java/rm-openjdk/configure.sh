#!/bin/sh
set -u
set -e

for pkg in java-1.8.0-openjdk-devel \
       java-1.8.0-openjdk-headless \
       java-1.8.0-openjdk; do
    if rpm -q "$pkg"; then
        rpm -e --nodeps "$pkg"
    fi
done

# clean up some directories left by the RPMs
for d in /usr/lib/jvm-1.8.0*; do
	if [ -d "$d" ]; then
		find "$d" -type d \
			| awk '{ print length, $0 }' \
			| sort -nsrk1 \
			| cut -d" " -f2- \
			| xargs rmdir
	fi
done
