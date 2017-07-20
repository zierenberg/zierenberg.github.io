#!/usr/bin/python
import numpy
import re


publications="./data/publications.dat"
data = numpy.genfromtxt(publications, dtype='str', delimiter=";")
FILE=open("./data/auto_publications.html", "w")

for entry in data:
    year=entry[0]
    authors=entry[1]
    title=entry[2]
    journal=entry[3]
    volume=entry[4]
    pages=entry[5]
    link=entry[6]
    entry_formatted="<li>"
    #modify author list:
    author_names=authors.split("and")
    for i in range(len(author_names)):
        first=author_names[i].split()[:-1]
        last=author_names[i].split()[-1]
        tmp=""
        for name in first:
            tmp+="%s."%name[0]
        tmp+=" %s"%last
        author_names[i]=tmp
    authors=""
    for index,author in enumerate(author_names):
        if index==len(author_names)-2:
            authors+= "%s and "%author 
        elif index==len(author_names)-1:
            authors+= "%s"%author 
        else:
            authors+="%s, "%author
    entry_formatted+="%s,\n"%authors
    #title:
    if title:
        entry_formatted+="<pubtitle><a href=\"%s\">%s,</a></pubtitle>\n"%(link,title)
    #journal:
    if journal:
        entry_formatted+="<journal>%s</journal>"%journal
    if re.search('\d',volume):
        entry_formatted+=" %s"%volume
    if re.search('\d',pages):
        entry_formatted+=", %s"%pages
    if year:
        entry_formatted+=" (%s)."%year
    entry_formatted+="\n</li>\n"
    FILE.write(entry_formatted)
FILE.close()
