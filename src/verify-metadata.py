import walktree
from xml.etree.ElementTree import Element
import os,sys
from argparse import ArgumentParser
import xml.etree.ElementTree as ET
import datetime

def walkXML(root,rootpath):
	for child in root:
           #print child.tag, child.attrib
           child_path=os.path.join(rootpath,child.attrib['name'])
           modification_time=os.stat(child_path).st_mtime
           #not take into account fractions of seconds
           times1=str(modification_time).split('.')
           times=child.attrib['modtime'].split('.')
           if abs(int(times1[0])-int(times[0])) > 1:
                print '%s has changed' % child_path
                print 'modification time %s' % datetime.datetime.fromtimestamp(int(times1[0])).strftime('%Y-%m-%d %H:%M:%S')
                #print 'modtime in metadat.xml %s' % times[0]
           else:
                if child.tag == 'dir':
                        walkXML(child,child_path)


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
        walkXML(root,options.local)
