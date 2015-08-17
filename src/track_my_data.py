#!/usr/bin/env python

import walktree
from xml.etree.ElementTree import Element
import os,sys
from argparse import ArgumentParser

if __name__ == '__main__':

    arg_parser = ArgumentParser(description="Track your staged data for changes in comparison with original data. You will need to first stage your data using: 'rsync -a <sourcefolder> <destinationfolder>'") 
    arg_parser.add_argument('--origin', help='original directory') 
    arg_parser.add_argument('--destination', help='destination directory') 
    options, rest = arg_parser.parse_known_args() 
    
    #open(options.origin, 'r') as origin
    metadata = Element('root')
    walktree.walktree(options.origin, metadata)
    metadatadir=os.path.join(options.destination, ".metadata")
    os.mkdir(metadatadir)
    f = open(os.path.join(metadatadir, "metadata.xml"), 'w')
    f.write(walktree.prettify(metadata))
