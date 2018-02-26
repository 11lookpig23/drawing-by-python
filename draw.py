import fileinput
import re
import math
def read():
	#make such [[x,1,2],[y,1,3]]
	string = ''
	for line in fileinput.input():
	#sys.stdout.write(x)
		string = string+line
	#print(string)
	y = '\n'
	#print(string.find(y))
	sub = re.compile(r'\r|\t|' '')
	x = sub.sub('',string)
	x = x.replace('\n',' ')
	#print(x)
	cmd_list = re.findall('\((.*?)\)', x)
	#print(cmd_list)
	
	x_li = []
	print('%!PS-Adobe-3.1')
	for cmd in cmd_list:
		
		cmd = cmd.strip()
		ele = re.split(r'\s+', cmd)
		#print(ele[0])
		
		if ele[0]=='color' :
			print(color(ele))		
		elif ele[0]=='line' :
			#print('s')		
			x_li.append(ele)
			#print(x_li)	
			Parser(x_li)
			x_li = []
		elif ele[0]== 'rect':
			#print('s')		
			x_li.append(ele)
			#print(x_li)	
			Parser(x_li)
			x_li = []
		elif ele[0]=='translate' :
			#print('d')
			x_li.append(ele)
		elif ele[0]=='rotate':
			#print('d')
			x_li.append(ele)
		elif ele[0]=='linewidth':
			#print('sdf')
			print(linewi(ele))
		else:
			pass
	print('showpage')
	#return command
	#return all_cmd = [1_line,2_line,,,,]

def Executor(mid_res):
	#for each_line in read():
	#	Parser(each_line)
	for i in range(len(mid_res)):
		string =''
		string = string+str(mid_res[i][0])+' '+str(mid_res[i][1])+' '+mid_res[i][2]
		print(string)
	print('stroke')
def Parser(cmd):
	#cmd = [['translate', '50', '50'], ['rect', '-10', '-10', '20', '20']]
	#for i in cmd[::-1]:
	lon = len(cmd)
	if cmd[lon-1][0]=='rect':
		rect_list = rect(cmd[lon-1])
		try:
			for j in range(lon-1):
				i = lon-2-j
				if cmd[i][0]=='translate':
					rect_list = translate(rect_list,cmd[i])
				elif cmd[i][0]=='rotate':
					rect_list = rotate(rect_list,cmd[i])
		except IndexError:	
			pass
		return Executor(rect_list)

	elif cmd[lon-1][0]=='line':
		line_list = line(cmd[lon-1])
		try:
			for j in range(lon-1):
				i = lon-2-j
				if cmd[i][0]=='translate':
					line_list = translate(line_list,cmd[i])
				elif cmd[i][0]=='rotate':
					line_list = rotate(line_list,cmd[i])
		except IndexError:	
			pass
		return Executor(line_list)
	
#x = ['line', '-10', '0', '10', '0']
def color(x):
	string = ''
	for i in range(1,len(x)):
		string = string+x[i]+' '
	string = string+'setrgbcolor'
	return string

def linewi(x):
	string = ''
	for i in range(1,len(x)):
		string = string+x[i]+' '
	string = string+'setlinewidth'
	return string

def rect(x):
	#trans to list
	y = []
	res = [0,0,0,0,0]
	for i in range(1,len(x)):
		y.append(eval(x[i]))
	res[0] = [y[0],y[1],'moveto']
	res[1] = [y[0]+y[2],y[1],'lineto']
	res[2] = [y[0]+y[2],y[1]+y[3],'lineto']
	res[3] = [y[0],y[1]+y[3],'lineto']
	res[4] = [y[0],y[1],'lineto']
	return res
	#return like this:[[-50, 0, 'moveto'], [10, 0, 'lineto']]
def line(x):
	y = []
	res = [0,0]
	for i in range(1,len(x)):
		y.append(eval(x[i]))
	res[0] = [y[0],y[1],'moveto']
	res[1] = [y[2],y[3],'lineto']
	return res
trans = ['translate', '60', '60']
rec = ['rect', '-10', '-10', '20', '20']
roat = ['rotate','5']
lin = ['line','-50','0','10','0']
pic = line(lin)
#print(pic)
def translate(pic,trans):
	#pic=[[-50, 0, 'moveto'], [10, 0, 'lineto']],trans is ['translate', '70', '70']
	x = eval(trans[1])
	y = eval(trans[2])
	for i in range(len(pic)):
		pic[i][0]=pic[i][0]+x
		pic[i][1]=pic[i][1]+y	
	return pic

def rotate(pic,roat):
	#change into radian
	pi = 3.141592653589397238
	theta = eval(roat[1])*pi/180
	#print(theta)
	#matrix caculate
	for i in range(len(pic)):
		x =math.cos(theta)*(pic[i][0])-math.sin(theta)*(pic[i][1])
		y =math.sin(theta)*(pic[i][0])+math.cos(theta)*(pic[i][1])
		pic[i][0] = x
		pic[i][1] = y
	return pic
#print(rotate(pic,roat))
#(translate 50 50) (translate 300 300) (line -10 0 10 0)

read()
#xy = [[-50, 0, 'moveto'], [10, 0, 'lineto']]
#print(Executor(xy))

#(
# rotate

#268.88110198960874 ) ( line -397.445802458825  -452.9687040830686 -901.4926756465527  -352)




