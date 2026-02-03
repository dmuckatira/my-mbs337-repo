import json
import xmltodict

#load and store json data
with open("hw3.json", "r") as f:
    prot_data = json.load(f)

#xml is kind of like a big dict with values and keys
#this put json into one root element so it's ready for stuff to be added
root = {}
root["data"] = prot_data

#converts root dictionary into the xml file
with open("proteins.xml", "w") as o:
    o.write(xmltodict.unparse(root, pretty=True))