#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
import xml.etree.ElementTree as etree
import yaml
import sys

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

def nactiKonfiguraci(soubor):
    cfile = open(soubor)
    root = yaml.safe_load(cfile)
    senatori = []
    for senator in root['senatori']:
       senatori.append(senator)
    cfile.close()
    return senatori

def hlasyDleKonf(soubor):
    for senator in nactiKonfiguraci(soubor):
        ziskejHlasy(senator)

def main():
    hlasyDleKonf(sys.argv[1])

if __name__ == "__main__":
    main()
