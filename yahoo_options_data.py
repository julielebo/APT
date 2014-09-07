from bs4 import BeautifulSoup
import urllib2
import json
import bs4.builder._lxml
import re
import locale
def contractAsJson(fileName):
   handler = open(fileName).read()
   locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
   soup = BeautifulSoup(handler, "xml")
   jsonElement = dict()
# optionQuotes
   jsonElement['optionQuotes'] = []
   templist = []
   contract = dict()
   contracts = soup.findAll('td', {'class':'yfnc_h'})
   x = 0
   while x < len(contracts)-7:
     date = re.split('[A-Z]*7?', contracts[x+1].string)
     symbol = re.findall('[A-Z]*7?',contracts[x+1].string)
     change_string = str(contracts[x+3])
     change = re.findall('\d+\.[\d+.]\d+',change_string)
     color = re.findall('#[a-z0-9]*', change_string)
     contract['Ask'] = contracts[x+5].string
     contract['Bid'] = contracts[x+4].string
     if( color[0] == '#008800'):
        contract['Change'] = "+"+change[0]
     if( color[0] == '#cc0000'):
        contract['Change'] = "-"+change[0]
     if( color[0] == '#000000'):
        contract['Change'] = " "+change[0]
     contract['Date'] = date[1]
     contract['Last'] = contracts[x+2].string
     contract['Open'] = contracts[x+7].string
     contract['Strike'] = contracts[x].string 
     contract['Symbol'] = symbol[0]
     contract['Type'] = symbol[7]
     contract['Vol'] = contracts[x+6].string
     templist.append(dict(contract))
     contract = dict()
     x = x+8
   
   contracts_data = soup.findAll('td', {'class':'yfnc_tabledata1'})
   x = 0
   while x < len(contracts_data)-7:
     date = re.split('[A-Z]*7?', contracts_data[x+1].string)
     symbol = re.findall('[A-Z]*7?',contracts_data[x+1].string)
     change_string = str(contracts_data[x+3])
     change = re.findall('\d+\.[\d+.]\d+',change_string)
     contract['Ask'] = contracts_data[x+5].string
     contract['Bid'] = contracts_data[x+4].string
     contract['Change'] = change[0]
     contract['Date'] = date[1]
     contract['Last'] = contracts_data[x+2].string
     contract['Open'] = contracts_data[x+7].string
     contract['Strike'] = contracts_data[x].string 
     contract['Symbol'] = symbol[0]
     contract['Type'] = symbol[7]
     contract['Vol'] = contracts_data[x+6].string
     templist.append(dict(contract))
     contract = dict()
     x = x+8
# sort list before adding to dictionary
   sortedlist = sorted(templist, key=lambda contract: locale.atoi(contract['Open']), reverse=True)
   jsonElement['optionQuotes'].append(sortedlist) 
# dateUrls
   table = soup.find('table', {'id':'yfncsumtab'})
   rows = table.findAll('tr')
   data = rows[2].findAll('td')
   urls = data[0].findAll('a')
   date_urls = []
   for eachurl in urls:
      tempurl = str(eachurl)
      result = re.findall('/.[A-Z]*.*m=\d*-\d*-*?\d+', tempurl)
      if len(result) != 0:
         date_urls.append("http://finance.yahoo.com" + result[0])
   jsonElement['dateUrls'] = date_urls
   
# Add current price to json
   current_price = soup.findAll('span',{'class':'time_rtq_ticker'})
   price = ""
   for x in current_price:
      price = x.string
   jsonElement['currPrice'] = float(price)

# Encode json object & return
   encoded_json = json.dumps(jsonElement, sort_keys=True, indent=4, separators=(',', ': '))
#   print encoded_json
   return encoded_json
