#!/usr/bin/env python3
#
# Script to download as much data from the DRIS+ API as possible
# and store it in the raw-data/ subdirectory.
#
import requests
import json
import shutil
import os
import time

url_base = "https://api.eurocris.org/dris"
output_dir = "data"
raw_output_dir = "raw-data"

if os.path.exists( raw_output_dir ):
    shutil.rmtree( raw_output_dir )
os.mkdir( raw_output_dir )

s = requests.Session()

url = url_base + "/entries"
while ( url is not None ):
    print( url )
    r = s.get( url, stream=True, headers = { "Accept": "application/json" } )
    print( "Request headers: " + str( r.request.headers ) )
    print( "Response headers: " + str( r.headers ) )
    r.raise_for_status()
    ct = r.headers["Content-Type"]
    fx = raw_output_dir + url[ len(url_base): ] + ( \
        ".json" if ct.startswith( "application/json" ) \
        else ".jsonld" if ct.startswith( "application/ld+json" ) \
        else ".html" if ct.startswith( "text/html" ) \
        else ".xxx" \
        )
    with open( fx, "wb" ) as f:
        for chunk in r.iter_content( chunk_size=4096 ):
            f.write( chunk )
    url = None
    if "next" in r.links:
        l = r.links["next"]
        if l is not None and l:
            url = l["url"]
            time.sleep( 1 )