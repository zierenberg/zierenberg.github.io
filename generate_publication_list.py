#!/usr/bin/python
import numpy
import re
import fileinput

publications="./data/publications.dat"
data = numpy.genfromtxt(publications, dtype='str', delimiter=";")
FILE=open("./data/auto_publications.html", "w")

list_publications=""
for entry in data:
    year=entry[0]
    journal=entry[1]
    volume=entry[2]
    pages=entry[3]
    authors=entry[4]
    title=entry[5]
    link=entry[6]
    comments=entry[7]
    entry_formatted="\n<li>"
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
    if len(comments)>2:
        entry_formatted+="\n%s"%comments
    entry_formatted+="\n</li>\n"
    FILE.write(entry_formatted)
    list_publications+="%s"%entry_formatted
FILE.close()

#now insert auto_publications into _pages/03_publications.md at the correct place
filestring=open("auto_pages/publications.md.mask").read()
mark='<!-- List of journal publications start -->'
start, end = filestring.split(mark,1)
filestring=start+mark+list_publications+end
FILE=open("_pages/03_publications.md", "w")
FILE.write(filestring)
FILE.close()
