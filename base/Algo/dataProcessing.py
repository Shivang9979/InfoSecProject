import os
def Segment(data):
	# f=open(os.path.join(os.getcwd()+"\\base\Algo","Original.txt"),"r")
	# con=f.read()
	# f.close()
	con =data
	print(con)
	count=0
	for char in con:
		count+=1
	k=0
	limit=int(count/5)
	for i in range(0,5):
		name=str(i)+".txt"
		path=os.path.join(os.getcwd()+"\\base\Algo\Segments",name)
		f=open(path,'w')
		ctr=0
		for j in range(k,count):
			k+=1
			f.write(con[j])
			ctr+=1
			if(ctr==limit and i!=4):
				f.close()
				break
		f.close()
	
	#os.remove('Original.txt')

def gatherInfo():
	path1=os.getcwd()
	path1=path1+"/base/Algo/Infos/Log.txt"
	path2=os.getcwd()
	path2=path2+"/base/Algo/Segments/"
	mainFile=open(path1,'w')
	lisDir=os.listdir(os.getcwd()+"/base\Algo\Segments\\")
	for i in lisDir:
		f=open(path2+i,'r')
		content=f.read()
		mainFile.write(str(len(content)))
		mainFile.write('::::')
		f.close()
	mainFile.close()	

def trim():
	path1=os.getcwd()
	path1=path1+"//base/Algo/Infos/Log.txt"
	mainFile=open(path1,'r')
	content=mainFile.read()
	mainFile.close()
	content=content.split('::::')
	path2=os.getcwd()
	path2=path2+"//base/Algo/Segments"
	lisDir=os.listdir(path2)
	tData=""
	c=0
	i=0
	for j in lisDir:
		path3=path2+"/"+j
		f=open(path3,'r')
		data=f.read()
		f.close()
		n=int(content[i])
		tData=data[:n]
		i+=1
		open(path3,'w').close()
		f=open(path3,'w')
		f.write(tData)
		f.close()
		tData=""
			


def Merge():
	path=os.path.join(os.getcwd()+"\\base\Algo","Output.txt")
	mainFile=open(path,"w")
	for i in range(0,5):
		name=os.path.join(os.getcwd()+"\\base\Algo\Segments",str(i)+".txt")
		f=open(name,"r")
		cont=f.read()
		print(cont)
		mainFile.write(cont)
		f.close()
		os.remove(name)
	mainFile.close()