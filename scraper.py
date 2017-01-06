#!/usr/bin/python

import csv
import time
from lxml import html
import requests

def dicerequest(keyword, location): 

   requesturl="https://www.dice.com/jobs?q=%s&l=%s" % (keyword, location)

   timestr = time.strftime("%Y%m%d_%H%M%S")
   ofilename = "csv/diceresults_%s.csv" % timestr 
   ofile = open(ofilename, "wb")
   writer = csv.writer(ofile)
 
   page = requests.get(requesturl)
   tree = html.fromstring(page.content)

   #job_posting_header = tree.xpath('//div[child::input/@type = "checkbox" and child::input/@class = "fchk" and child::input/@chktyp = "djt"]/a/text()')

   job_title = tree.xpath('//div/h3/a[contains(@id, "position") and @class = "dice-btn-link"]/@title')
   job_link = tree.xpath('//div/h3/a[contains(@id, "position") and @class = "dice-btn-link" and boolean(@title)]/@href') 
   company = tree.xpath('//div/ul/li[@class="employer"]/a[contains(@id, "company") and @class = "dice-btn-link"]/text()')
   location = tree.xpath('//div/ul/li[@class="location"]/text()')
   posted = tree.xpath('//div/ul/li[@class="posted"]/text()')


   #job_title_clean = map(str.strip, job_title)
   
   print len(job_title)
   print len(job_link)
   print len(company)
   print len(location)
   print len(posted)

   for i in range(0, len(job_title)):
      print "%s|%s|%s|%s|%s|" % (job_title[i], job_link[i], company[i], location[i], posted[i])   
      writer.writerow([job_title[i], job_link[i], company[i], location[i], posted[i]])

   #print 'Job Title: ', job_title
   #print 'Job Link: ', job_link
   #print 'Company: ', company
   #print 'Location: ', location
   #print 'Posted: ', posted
   
   return

def main():
   
   dicerequest("data", "")
   return 0

if __name__ == "__main__":
    main()
