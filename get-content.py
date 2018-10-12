from bs4 import BeautifulSoup as soup


# Get the html saved in the txt file
with open('html.txt', 'r') as f:

	text = f.read()


# Make soup	widit
soup = soup(text, 'html.parser')
#<div class="entry-content">


# Find desired content by tag
tags = soup.find_all('h3')


list = []


# Get the text. The tag may have child tags, which make a list, so iterate lists
# Some objects in the lists are text and others bs4 objects
# There may be a broader, more universal method to do this
for i in tags:

	line = ''
	
	for j in i:
	
		# For bs4 objects
		try:
		
			#print j.text
			line += j.text
			
		except AttributeError:
		
			# For just text
			try:
			
				#print j
				line += j
		
			except:
			
				print 'Some error happened for %s. Type is %s' % (j, type(j))
		
	print line
	list.append(line)


	
	
pause = raw_input('done')
