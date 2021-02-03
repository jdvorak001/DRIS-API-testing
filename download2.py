#!/usr/bin/env python3
#
# Script to attempt to re-download all data/entries/ files one-by-one from the DRIS+ API with ID-based accesses.
# It will store them in-place: a subsequent `git status` should not find any difference.
#
import requests
import os
import pathlib
import re
import json

url_base = "https://api.eurocris.org/dris"
input_output_dir = "data"
limit_dir = "/entries"

s = requests.Session()
n_files = 0
for x in sorted( pathlib.Path( input_output_dir + limit_dir ).rglob( "*.json" ), key=os.path.getmtime ):
    url = url_base + re.sub( '^' + input_output_dir, '', re.sub( r'\.json$', '', x.as_posix() ) )
    print( url )
    r = s.get( url, stream=True, headers = { "Accept": "application/json" } )
    r.raise_for_status()
    ct = r.headers["Content-Type"]
    with open( x, "w" ) as f:
        json.dump( r.json(), f, sort_keys=True, indent="\t" )
    n_files += 1

print( f"Processed {n_files} files. After this, `git status` should not list any files from the {input_output_dir}/ subdirectory" )

