import walktree
from xml.etree.ElementTree import Element
import os,sys
from argparse import ArgumentParser
import xml.etree.ElementTree as ET

if __name__ == '__main__':

    arg_parser = ArgumentParser(description='Verify the differences in metadata from original directory with local directory') 
    arg_parser.add_argument('--origin', help='original directory') 
    arg_parser.add_argument('--local', help='local') 
    options, rest = arg_parser.parse_known_args() 
    
    #open(options.origin, 'r') as origin
    metadata = Element('root')
    walktree.walktree(options.origin, metadata)
    metadatadir=os.path.join(options.local, ".metadata")
    f = open(os.path.join(metadatadir, "metadata.xml"), 'r')
    if f.read() != walktree.prettify(metadata):
	print 'WARNING ORIGINAL DATA HAS CHANGED\n'
    else:
	tree = ET.parse(os.path.join(metadatadir, "metadata.xml"))
	root = tree.getroot()
	for child in root:
	   print child.tag, child.attrib

       	
