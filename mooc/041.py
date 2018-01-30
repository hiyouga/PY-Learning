#mutifiles.py
ftele1 = open('041.1.in', 'rb')
ftele2 = open('041.2.in', 'rb')

ftele1.readline()
ftele2.readline()
lines1 = ftele1.readlines()
lines2 = ftele2.readlines()

list1_name = []
list1_tele = []
list2_name = []
list2_email = []
lines = []

for line in lines1:
	elements = line.split()
	list1_name.append(str(elements[0].decode('utf-8')))
	list1_tele.append(str(elements[1].decode('utf-8')))

for line in lines2:
	elements = line.split()
	list2_name.append(str(elements[0].decode('utf-8')))
	list2_email.append(str(elements[1].decode('utf-8')))

for i in range(len(list1_name)):
	s = ''
	if list1_name[i] in list2_name:
		j = list2_name.index(list1_name[i])
		s = ' \t'.join([list1_name[i], list1_tele[i], list2_email[j]])
		s += '\n'
	else:
		s = ' \t'.join([list1_name[i], list1_tele[i], str('   -----   ')])
		s += '\n'
	lines.append(s)
for i in range(len(list2_name)):
	s = ''
	if list2_name[i] not in list1_name:
		s = ' \t'.join([list2_name[i], str('   -----   '), list2_email[i]])
		s += '\n'
	lines.append(s)

ftele3 = open('041.out', 'w')
ftele3.writelines(lines)

ftele3.close()
ftele1.close()
ftele2.close()

print("The addressBooks are merged!")