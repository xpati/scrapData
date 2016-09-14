
import urllib
import re


urls = ["http://www.dges.mctes.pt/coloc/2013/col1det.asp?BIC=14787482","http://www.dges.mctes.pt/coloc/2013/col1det.asp?BIC=14511244","http://www.dges.mctes.pt/coloc/2013/col1det.asp?BIC=14666652"]

regex = ['<td width="590">(.+?)</td>','td width="110">(.+?)</td>','<td width="650">(.+?)</td>','<td width="70" align="center" style="border-right-color: #4682B4; border-right-style: solid; border-right-width: 1px; border-bottom-color: #4682B4; border-bottom-style: solid; border-bottom-width: 1px;">(.+?)</td>','<td width="70" align="center" style="border-right-color: #4682B4; border-right-style: solid; border-right-width: 1px;">(.+?)</td>']

ids=['Name','B.I.','Opcion','University','Course', 'CandidateClassificasion','nOrder','Grade','PI','12','GeneralClassification']

print "DETAILS:"
i=0
q=0
while i < len(urls):
	j=0
	htmlfile = urllib.urlopen(urls[i])
	htmltext = htmlfile.read()
	i+=1
	print
	while j<len(regex):
		pattern=re.compile(regex[j])
		words = re.findall(pattern,htmltext)
		print j
		if j>1 and j<3: #'Opcion','University','Course'
			k=0
			number=1
			for word in words:        # Second Example				
				xpto = word.decode('iso-8859-1').encode('utf8')
				my_string = re.sub("<.*?>"," ", xpto)
	 			my_string = re.sub("&nbsp;"," ", my_string)
				if k==0:
					print "%s %d" %(ids[q],number) 				
					print "%s => %s" %(ids[q+1],my_string)
					number+=1
					q+=2
					k+=1
				else:
					print "%s => %s" %(ids[q],my_string)
					q=q-2
					k=0
		elif j==0 or j==1: #'Name','B.I.'
			xpto = words[0].decode('iso-8859-1').encode('utf8')
			my_string = re.sub("<.*?>"," ", xpto)
	 		my_string = re.sub("&nbsp;"," ", my_string)
			print "%s => %s" %(ids[q],my_string)
			q+=1	
		else:#'CandidateClassificasion','nOrder','Grade','PI','12']
			if j==3:
				r=5
			else:
				r=10
			q=6
			for word in words:        # Second Example
				if "<strong>" not in word: 
					xpto = word.decode('iso-8859-1').encode('utf8')
					my_string = re.sub("<.*?>"," ", xpto)
		 			my_string = re.sub("&nbsp;"," ", my_string)
					print "%s - %s => %s" %(ids[r],ids[q],my_string)
					q+=1
					if q==10: 
						print
						q=6
			q=0
		j+=1
		print



