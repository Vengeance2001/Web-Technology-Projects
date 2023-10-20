from django.shortcuts import render
fam = 0

def enterMarks(request):

	return render(request, 'EnterMarks.html')


def get_Grade(marks):

	marks = int(marks)
	if(marks >= 90):
		return "A"
	elif(marks >= 80 and marks < 90):
		return "B"
	elif(marks >= 60 and marks < 80):
		return "C"
	elif(marks >= 40 and marks < 60):
		return "D"
	else:
		return "E"

supple = []

def get_Remark(marks):

	global fam
	global supple

	marks = int(marks)
	if(marks >= 90):
		fam += 1
		return "Pass"
	elif(marks >= 80 and marks < 90):
		fam += 1
		return "Pass"
	elif(marks >= 60 and marks < 80):
		fam += 1
		return "Pass"
	elif(marks >= 40 and marks < 60):
		fam += 1
		return "Pass"
	else:
		supple.append(fam)
		fam += 1
		return "Fail"


def get_Subject(x):
	
	if(x == 0):
		return "WT"
	elif(x == 1):
		return "DAA"
	elif(x == 2):
		return "SMD"
	elif(x == 3):
		return "CN"
	else:
		return "EDI"


def getMarks(request):

	physics = []
	chemistry = []
	maths = []
	english = []
	computer = []

	name = request.GET['sname']
	roll = request.GET['roll']
	phy = request.GET['phy']
	chem = request.GET['chem']
	math = request.GET['math']
	eng = request.GET['eng']
	comp = request.GET['comp']
	n1 = request.GET['n1']
	n2 = request.GET['n2']
	n3 = request.GET['n3']
	n4 = request.GET['n4']
	n5 = request.GET['n5']

	physics.append("1")
	chemistry.append("2")
	maths.append("3")
	english.append("4")
	computer.append("5")

	physics.append(str(n1))
	chemistry.append(str(n2))
	maths.append(str(n3))
	english.append(str(n4))
	computer.append(str(n5))

	physics.append("100")
	chemistry.append("100")
	maths.append("100")
	english.append("100")
	computer.append("100")
	
	physics.append(phy)
	chemistry.append(chem)
	maths.append(math)
	english.append(eng)
	computer.append(comp)

	physics.append(get_Grade(physics[3]))
	chemistry.append(get_Grade(chemistry[3]))
	maths.append(get_Grade(maths[3]))
	english.append(get_Grade(english[3]))
	computer.append(get_Grade(computer[3]))

	physics.append(get_Remark(physics[3]))
	chemistry.append(get_Remark(chemistry[3]))
	maths.append(get_Remark(maths[3]))
	english.append(get_Remark(english[3]))
	computer.append(get_Remark(computer[3]))

	supple_sub = []
	result = ""

	for x in supple:
		supple_sub.append(get_Subject(x))

	if(len(supple_sub) == 0):
		result = "Pass"

	elif(len(supple_sub) == 1):
		result = "Supplementary in"

	elif(len(supple_sub) == 2):
		supple_sub[0] +=" and"
		result = "Supplementary in"

	else:
		supple_sub.clear()
		result = "Fail"


	return render(request, 'MarkSheet.html', {'physics':physics, 'chemistry':chemistry, 'maths':maths, 'english':english, 'computer':computer, 'name':name, 'rollno':roll, 'supple':supple_sub, 'result':result})