import walktree
from xml.etree.ElementTree import Element
import os,sys
from argparse import ArgumentParser

if __name__ == '__main__':

    arg_parser = ArgumentParser(description='Stage in directory to destination directory') 
    arg_parser.add_argument('--origin', help='original directory to stage in') 
    arg_parser.add_argument('--destination', help='destination where to stage in') 
    options, rest = arg_parser.parse_known_args() 
    
    #open(options.origin, 'r') as origin
    metadata = Element('root')
    walktree.walktree(options.origin, metadata)
    metadatadir=os.path.join(options.destination, ".metadata")
    os.mkdir(metadatadir)
    f = open(os.path.join(metadatadir, "metadata.xml"), 'w')
    f.write(walktree.prettify(metadata))
