import requests
import os
import zipfile
import csv
import json
import io
# Downloading the zip file
page = "https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2019.json.zip"
result = requests.get(page)
# extracting the zipfile
zipout = zipfile.ZipFile(io.BytesIO(result.content))
zipout.extractall()
# opening JSON file
nvdjson = open("nvdcve-1.1-2019.json")
nvddict = json.load(nvdjson)
# WORK in progress you have to iterate here for CVE items
nvddict['CVE_Items'][0]





