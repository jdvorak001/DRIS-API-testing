#!/usr/bin/env python3
#
# Script to process the downloaded data from the DRIS+ API as possible,
# stored in the raw-date/ subdirectory, and store the results in a data/ subdirectory tree.
#
import json
import shutil
import os
import json
import pathlib

url_base = "https://api.eurocris.org/dris"
output_dir = "data"
raw_input_dir = "raw-data"

n_files = 0
n_entries = 0
for fx in pathlib.Path( raw_input_dir ).rglob( "*.json" ):
    jx = json.load( open( fx ) )
    n_files += 1
    for x in jx["itemListElement"]:
        id = x["@id"]
        if ( id.startswith( url_base ) ):
            n_entries += 1
            fx = output_dir + id[ len(url_base): ] + ".json"
            os.makedirs( os.path.dirname( fx ), mode=0o755, exist_ok=True )
            with open( fx, "w" ) as f:
                json.dump( x, f, sort_keys=True, indent="\t" )
            for y in x["@included"]:
                id = y["@id"]
                if ( id.startswith( url_base ) ):
                    fy = output_dir + id[ len(url_base): ] + ".json"
                    os.makedirs( os.path.dirname( fy ), mode=0o755, exist_ok=True )
                    with open( fy, "w" ) as f:
                        json.dump( y, f, sort_keys=True, indent="\t" )
        else:
            raise Exception( f"id '{id}' doesn't start with url_base '{url_base}'" )

print( f"Processed {n_entries} entries from {n_files} files" )