#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
import xml.etree.ElementTree as etree
import yaml

def ziskejHlasy(senator):
    url = "http://senat.cz/senatori/hlasovani_xml.php?pid="

    file = urllib2.urlopen(url + str(senator))
    data = file.read()
    file.close()

    hlasovani = etree.fromstring(data)

    print "Senator: " + hlasovani.attrib['jmenoSenatora'].encode('utf-8')

    for hlas in hlasovani:
      print "Volebni obdobi "+hlas.find('volebniObdobi').text
      print "Schuze "+hlas.find('cisloSchuze').text
      print hlas.find('popisHlasovani').text.encode('utf-8')+" "+hlas.find('oCemHlasovano').text.encode('utf-8')+" - "+hlas.find('textHlasu').text.encode('utf-8')+" ("+hlas.find('textVysledku').text.encode('utf-8')+")"
      print hlas.find('urlHlasu').text
      print "---"

if __name__ == "__main__":
    ziskejHlasy(278)
