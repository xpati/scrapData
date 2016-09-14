
import urllib
import re


urls = ["http://www.dges.mctes.pt/coloc/2013/col1res.asp?BI=14787482","http://www.dges.mctes.pt/coloc/2013/col1res.asp?BI=14511244","http://www.dges.mctes.pt/coloc/2013/col1res.asp?BI=14666652"]

regex = ['<td width="590">(.+?)</td>','td width="110">(.+?)</td>','<td width="660">(.+?)</td>','<td width="660" style="border-top-color: #4682B4; border-top-style: solid; border-top-width: 1px;">(.+?)</td>']

print "ACCEPTED:"
i=0
while i < len(urls):
	j=0
	htmlfile = urllib.urlopen(urls[i])
	htmltext = htmlfile.read()
	i+=1
	print
	while j<len(regex):
		pattern=re.compile(regex[j])
		words = re.findall(pattern,htmltext)
		xpto = words[0].decode('iso-8859-1').encode('utf8')
		my_string = re.sub("<.*?>"," ", xpto)
		my_string = re.sub("&nbsp;"," ", my_string)
		print my_string
		j+=1
				
    
   



