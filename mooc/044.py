#mutifiles2.py
ftele1 = open('041.1.in', 'rb')
ftele2 = open('041.2.in', 'rb')

ftele1.readline()
ftele2.readline()
lines1 = ftele1.readlines()
lines2 = ftele2.readlines()

dic1 = {}
dic2 = {}

for line in lines1:
	elements = line.split()
	dic1[elements[0]] = str(elements[1].decode('gbk'))

for line in lines2:
	elements = line.split()
	dic2[elements[0]] = str(elements[1].decode('gbk'))

lines = []
lines.append('姓名 \t电话 \t邮箱\n')


for key in dic1:
	s = ''
	if key in dic2.keys():
		s = ' \t'.join([str(key.decode('utf-8')), dic1[key], dic2[key]])
		s += '\n'
	else:
		s = ' \t'.join([str(key.decode('utf-8')), dic1[key], str('   -----    ')])
		s += '\n'
	lines.append(s)


for key in dic2:
	s = ''
	if key not in dic1.keys():
		s = ' \t'.join([str(key.decode('utf-8')), str('   -----   '), dic2[key]])
		s += '\n'
	lines.append(s)

ftele3 = open('044.out', 'w')
ftele3.writelines(lines)

ftele3.close()
ftele1.close()
ftele2.close()