from bs4 import BeautifulSoup
from urllib import urlopen
html = urlopen('http://www.rottentomatoes.com/').read()
soup = BeautifulSoup(html)
print "\n"

print "--------Top Grossing Films--------"

print "\n"
rank = 1

for section in soup.findAll('div',{"id":"homepage-top-box-office"}):
    for sec in section.findAll('td'):
        for sec2 in sec.findAll('a'):
            print "--%d-- %s"%(rank, sec2.text)
            rank = rank + 1


print "\n"
