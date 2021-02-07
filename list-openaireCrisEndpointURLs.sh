#!/bin/sh
#
# This script lists the lines containing the field "openaireCrisEndpointURL" from all downloaded JSON files
# and summarizes them by the field's value.
#
find data -name \*.json | \
xargs grep -h openaireCrisEndpointURL | \
sort | \
uniq -c
