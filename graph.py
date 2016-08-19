import matplotlib.pyplot as plt
import arstCliLib
from arstCliLib import *
import sys

if len(sys.argv) != 2 :
	print("You have to enter dut name as argument to this script")
	print("exiting script ..... ")
	exit()
else:
	DutName=sys.argv[1]
	openSshOnDut(DutName, sshUsername='admin', sshPassword='', cliTimeout=30)
	CmdList=["show int eth 1 counter rate"]
	Result=sendCmd (DutName, CmdList, accessMethod='ssh', prompt='base')
	closeSshOnDut(DutName)
   	for list1 in Result:
      		for list2 in list1:
         		listS2=[]
         		for list3 in list2:
            			listS2.append(str(list3))

      	 		l=len(listS2)
         		i=0
         		while i < l:
            			#i=i+1
            			print(listS2[i]),
            			i=i+1
         		print("")
      #print(listS2)
	#print(Result)
	for list1 in Result:
		for list2 in list1:
			listS2=[]

			for list3 in list2:
                                listS2.append(str(list3))
			l=len(listS2)
                        i=0
                        if list2[i]=="Et1":
				input=listS2[3].rstrip("%")
				output=listS2[6].rstrip("%")
				print(input)
				print(output)	
				"""while i < l:
                                	#i=i+1
					print(listS2[i]),
                                	i=i+1"""
                        print("")
	import numpy as np
	import matplotlib.pyplot as plt
 
	objects = ('Input', 'Output')
	y_pos = np.arange(len(objects))
	intput=float(input)
	output=float(output)
	performance = [input,output]
 
	plt.bar(y_pos, performance, align='center', alpha=0.5)
	plt.xticks(y_pos, objects)
	plt.ylabel('Usage')
	plt.title('Interface Eth1 usage')
 
plt.show()
