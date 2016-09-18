# -*- coding: utf-8 -*-
from numpy import *
import operator
from os import listdir
import random
import sys

def output(line_num):
	text1 = "Average_线路"+str(line_num)+"_老人卡.txt"
	text2 = "Average_线路"+str(line_num)+"_普通卡.txt"
	text3 = "Average_线路"+str(line_num)+"_学生卡.txt"
	f1 = open(text1)
	f2 = open(text2)
	f3 = open(text3)

	text = ['星期日','星期一','星期二','星期三','星期四','星期五','星期六']

	n = 2
	m = 24  
	people_num = []
	for i in range(n):
		people_num.append([])
	for i in range(n):
		for j in range(m):
			people_num[i].append([])
	for line in f1:
		if ( line.split(',')[1] == "休息日" ):
			people_num[0][ int( line.split(',')[2]) ] = int( line.split(',')[3] )
		else:
			people_num[1][ int( line.split(',')[2]) ] = int( line.split(',')[3] )

	for line in f2:
		if ( line.split(',')[1] == "休息日" ):
			people_num[0][ int( line.split(',')[2]) ] += int( line.split(',')[3] )
		else:
			people_num[1][ int( line.split(',')[2]) ] += int( line.split(',')[3] )

	for line in f3:
		if ( line.split(',')[1] == "休息日" ):
			people_num[0][ int( line.split(',')[2]) ] += int( line.split(',')[3] )
		else:
			people_num[1][ int( line.split(',')[2]) ] += int( line.split(',')[3] )

	if(line_num==10):
		f2 = open("new_final_line10.txt",'w')
	if(line_num==15):
		f2 = open("new_final_line15.txt",'w')

	for i in range(7):
		for j in range(6,22):
			if(j >= 0 and j <= 9):
				Time = '0'+str(j) + ','
			else:
				Time = str(j) + ','
			if ( i < 3 ) :
				f2.write("线路" + str(line_num) + ',2015010' + str(i+1) + ',' + Time + str( people_num[0][j]) + '\n' )
			else :
				f2.write("线路" + str(line_num) + ',2015010' + str(i+1) + ',' + Time + str( people_num[1][j]) + '\n' )


def insert_label(filenameIn,line_name,Card_type):
	lineName = ['线路10','线路15']
	CardType = ['普通卡','老人卡','学生卡']
	f1 = open(filenameIn)

	text_name = "Insert_lable"+'_'+lineName[line_name]+'_'+CardType[Card_type]+".txt"
	f2 = open(text_name,'w')
	f3 = open("gd_weather_report.txt")


	weather_flag = [0]*2
	week = 4
	text = ['日','一','二','三','四','五','六']
	text1=['休息日','工作日']
	weather = ['晴','雨']

	filter_num = [0]*25
	for i in range(24):
		filter_num[i] = -1
	for i in range(11,17):
		filter_num[i] = 200
	for i in range(17,22):
		filter_num[i] = 350
	filter_num[6] = 150
	filter_num[7] = 600
	filter_num[8] = 1000
	filter_num[9] = 1000
	filter_num[10] = 800
	filter_num[22] = 200
	for line in f1:

		listFromLine = line.split(',')
		# if ( lineName[line_name] == '线路15' ):
		# 	if ( int(line.split(',')[3]) > filter_num[ int( line.split(',')[2][-2:])] ):
		if(listFromLine[2]=='00'):
			week +=1

		if(listFromLine[1][4:]=='1011'):
			result = 1
		elif((week%7==0) or (week%7==6)):
			result=0
		elif(listFromLine[1][4:]>='1001'and listFromLine[1][4:]<='1007'):
			result = 0
		else:
			result = 1

		if(listFromLine[2]=='00'):
			weatherline = f3.readline()
			if '雨' in (weatherline.split(',')[1].split('/')[0]):
				weather_flag[0] = 1
			else:
				weather_flag[0] = 0
			if '雨' in (weatherline.split(',')[1].split('/')[1]):
				weather_flag[1] = 1
			else:
				weather_flag[1] = 0

		if(int(listFromLine[2]) >= 6 and int(listFromLine[2]) <= 18):
			weather_text = weather[weather_flag[0]]
		else:
			weather_text = weather[weather_flag[1]]

		if(listFromLine[1][4:]<'0810' or listFromLine[1][4:]>'0820'):
			f2.write(line[:-1]+','+'星期'+text[week%7]+','+text1[result]+','+weather_text+'\n')

	return text_name

def aver(filenameIn,line_name,Card_type):

	lineName = ['线路10','线路15']
	CardType = ['普通卡','老人卡','学生卡']
	f1 = open(filenameIn)

	text_name = "Average"+'_'+lineName[line_name]+'_'+CardType[Card_type]+".txt"
	f2 = open(text_name,'w')

	n = 2
	m = 24
	matrix = []
	text = ['休息日','工作日']
	for i in range(n):
		matrix.append([])
	for i in range(n):
		for j in range(m):
			matrix[i].append([])
			matrix[i][j] = 0
	for line in f1:
		listFromLine = line.split(',')

		if(listFromLine[5]=='休息日'):
			matrix[0][int(listFromLine[2])] += int(listFromLine[3])
			if(matrix[0][int(listFromLine[2])] != int(listFromLine[3])):
				matrix[0][int(listFromLine[2])] /= 2
		elif(listFromLine[5]=='工作日'):
 			matrix[1][int(listFromLine[2])] += int(listFromLine[3])
 			if(matrix[1][int(listFromLine[2])] != int(listFromLine[3])):
 				matrix[1][int(listFromLine[2])] /= 2
 	for i in range(n):
 		for j in range(m):
 			f2.write(lineName[line_name]+','+text[i]+","+str(j)+','+str(matrix[i][j])+'\n')

def DealtimeStatistic(filenameIn,line_name,Card_type):
	lineName = ['线路10','线路15']
	CardType = ['普通卡','老人卡','学生卡']
	f1 = open(filenameIn)

	text_name = "Statistic"+'_'+lineName[line_name]+'_'+CardType[Card_type]+".txt"
	f2 = open(text_name,'w')

	newLine = []
	n = 5  
	m = 32  
	k = 24
	l = 2  
	matrix = []
	for i in range(n):
		matrix.append([])
	for i in range(n):
		for j in range(m):
			matrix[i].append([])
	for i in range(n):
		for j in range(m):
			for s in range(k):
				matrix[i][j].append([])
	for i in range(n):
		for j in range(m):
			for s in range(k):
				for q in range(l):
					matrix[i][j][s].append([])
					matrix[i][j][s][q]=0

	

	for line in f1:
		listFromLine = line.split(',')
		month = int(listFromLine[5][4:6])-8
		day = int(listFromLine[5][6:8])
		time = int(listFromLine[5][8:])
		if ( listFromLine[1] == "线路10"):
			bus_line = 0
		else:
			bus_line = 1
		
		if(listFromLine[-1][0:9] == CardType[Card_type]):
			matrix[month][day][time][bus_line] += 1



	for i in range(n):
		for j in range(m):
			for s in range(k):
				for q in range(l):
					statisticNum = matrix[i][j][s][q]
					if(q==0):
						bus_line = "线路10"	
					else:
						bus_line = "线路15"
					if((i+8) >= 8 and (i+8) <= 9):
						Month = '0'+str(i+8)
					else:
						Month = str(i+8)
					if(j >= 0 and j <= 9):
						Day = '0'+str(j)
					else:
						Day = str(j)
					if(s >= 0 and s <= 9):
						Time = '0'+str(s)
					else:
						Time = str(s)

					if(Day == '00' or (Month == '09'and Day == '31') or (Month == '11'and Day == '31')):
						whatever = 0
					else:
						if(bus_line == lineName[line_name]):
							f2.write(bus_line+","+"2014"+Month+Day+','+Time+','+str(statisticNum)+'\n')
    
	return  text_name
def sequence(filenameIn):

	print(" Start!")

	for i in range(2):
		for j in range(3):
			
			f_out = DealtimeStatistic(filenameIn,i,j)
			print("Statistic Complete!")
			f_out_1 = insert_label(f_out,i,j)
			print("insert_label Complete!")
			aver(f_out_1,i,j)
			print("Average Complete!")













































def Srt2Word(inputfile,outputfile):
	f1 = open(inputfile)
	f2 = open(outputfile,'w')
	for line in f1:
		if ((line[0]>='A') and (line[0]<='Z'))or((line[0]>='a') and (line[0]<='z')):
			if(line[-3]!='.'):
				l=line[0:-3]
				f2.write(l)
				f2.write(' ')
			else:
				f2.write(line)
				f2.write('\n')

def sort_at_colume(filename,colume):
	f1 = open(filename)
	if(colume == 3):
		f2 = open("sort_at_time.txt",'w')
	elif(colume == 1):
		f2 = open("sort_at_Busline.txt",'w')

	temp = []
	count = 0
	flag = 0
	id = ''

	for line in f1:

		listFromLine = line.split(',')

		if(id == ''):
			if(listFromLine[2]):
				id = listFromLine[2]
			else:
				id = ''
	
		if(id == listFromLine[2]):
			count+=1
		else:
			if(flag == 1):
				flag = 0
				fileoutput(f2,temp,colume)
				f2.write(' '+(str)(count)+'\n')
			else:
				f2.write('deleted'+'\n')

			id = listFromLine[2]
			count=1
			del temp[0:]

		temp.append(line)
		if(line.split(',')[3][-2:] >= '01' and line.split(',')[3][-2:] <= '07'):
			flag = 1

	fileoutput(f2,temp,colume)
	f2.write(' '+(str)(count)+'\n')

global people_num
people_num = 0

def fileoutput(file,Stringlist,colume):
	global people_num
	Matric_temp = Stringlist2Matric(Stringlist)
	quick_sort(Matric_temp,0,len(Matric_temp)-1,colume)

	if(Matric_temp[-1][3][4:6]<='11'):
		return
	

	for l in Matric_temp:
		l[2] = str(people_num)
	people_num+=1

	sorted_temp = Matric2Stringlist(Matric_temp)
	for l in sorted_temp:
		file.write(l)	

def filter(filename):
	f1 = open(filename)
	f2 = open("filted.txt",'w')

	temp = []
	count = 0
	flag = 0
	id = ''

	for line in f1:

		listFromLine = line.split(',')

		if(id == ''):
			id = listFromLine[2]
	
		if(id == listFromLine[2]):
			count+=1
		else:
			if(flag == 1):
				flag = 0
				for l in temp:
					f2.write(l)
				f2.write(' '+(str)(count)+'\n')
			else:
				f2.write('deleted'+'\n')

			id = listFromLine[2]
			count=1
			del temp[0:]

		temp.append(line)
		if(line.split(',')[3][-2:] >= '00' and line.split(',')[3][-2:] <= '08'):
			flag = 1

	for l in temp:
		f2.write(l)	
	f2.write(' '+(str)(count)+'\n')

	
def Stringlist2Matric(Stringlist):
	outputMatric = []
	index = 0
	for line in Stringlist:
		listFromLine = line.split(',')
		outputMatric.insert(index,listFromLine)
		index += 1
	return outputMatric
def Matric2Stringlist(Matric):
	outputStringlist = []
	index = 0
	for line in Matric:
		oneStringline = ','.join(line)
		outputStringlist.insert(index,oneStringline)
		index += 1

	return outputStringlist
def DealtimeStatistic_pro(filenameIn):
	f1 = open(filenameIn)
	f2 = open("DealtimeStatistic_pro.txt",'w')

	newLine = []
	firstline = f1.readline().split(',')
	firstline.append(0)
	newLine.append(firstline)
	print(newLine[0])
	for line in f1:
		listFromLine = line.split(',')
		for l in newLine:
			if(listFromLine[5] == l[5] and listFromLine[1] == l[1]):#time and line equal
				l[-1]+=1
			else:
				Createline = listFromLine
				Createline.append(0)
				newLine.append(Createline)

	for line in newLine:
		out_line = []
		out_line.append(line[1])#line_name
		out_line.append(line[5][:8])#Deal_time_day
		out_line.append(line[5][8:])#Deal_time_hour
		out_line.append(line[-1])#Deal_time_hour
		out = ','.join(out_line)
		f2.write(out)









def divideAndSort(filenameIn):
	f1 = open(filenameIn)
	fo_8 = open("divided_8.txt",'w')
	fo_9 = open("divided_9.txt",'w')
	fo_10 = open("divided_10.txt",'w')
	fo_11 = open("divided_11.txt",'w')
	fo_12 = open("divided_12.txt",'w')

	newLine = []
	for line in f1:
		listFromLine = line.split(',')
		temp = []
		temp.append(listFromLine[1])#0:Use_city 1:line_name 2:Terminal_id 3:Card_id 4: Create_city 5:Deal_time 6:Card_type
		temp.append(listFromLine[5])
		temp.append(listFromLine[6])
		out = ','.join(temp)
		if(listFromLine[5][4:6]=="08"):
			fo_8.write(out)
		elif(listFromLine[5][4:6]=="09"):
			fo_9.write(out)
		elif(listFromLine[5][4:6]=="10"):
			fo_10.write(out)
		elif(listFromLine[5][4:6]=="11"):
			fo_11.write(out)
		elif(listFromLine[5][4:6]=="12"):
			fo_12.write(out)

	print("divide Complete!")
	SortAndCombine("divided_8.txt")
	SortAndCombine("divided_9.txt")
	SortAndCombine("divided_10.txt")
	SortAndCombine("divided_11.txt")
	SortAndCombine("divided_12.txt")

def SortAndCombine(fileIn):
	sys.setrecursionlimit(10000000)

	f1 = open(fileIn)
	f2 = open("Combined.txt",'w')
	index = 0
	newLine = []
	for line in f1:
		listFromLine = line.split(',')
		newLine.insert(index,listFromLine)
		index+=1

	print("SortAndCombine prepare Complete!")
	quickSort(newLine,0,len(newLine)-1,1)
	print("SortAndCombine sort Complete!")
	for line in newLine:
		out = ','.join(line)
		f2.write(out)


def file2Matric(filenameIn):
	f1 = open(filenameIn)
	f2 = open("outputfile.txt",'w')
	index = 0
	newLine = []
	for line in f1:
		listFromLine = line.split(',')
		temp = listFromLine[0:2]
		temp.append(listFromLine[3])
		temp.append(listFromLine[6])
		newLine.insert(index,temp)
		index += 1
	print("prepare Complete!")
	quick_sort(newLine,0,len(newLine)-1,2)
	print("sort Complete!")
	for line in newLine:
		out = ','.join(line)
		f2.write(out)
	#quick sort
def quickSort(L, low, high,colume):
	i = low 
	j = high
	if i >= j:
		return
	mid = (i+j)/2
	key = L[mid][colume]
	while i < j:
		while i < mid and L[i][colume] >= key:
			i = i + 1                                                            
		#L[i], L[j] = L[j], L[i]
		while mid < j and L[j][colume] <= key:    
			j = j - 1
		L[j], L[i] = L[i], L[j]
	#L[mid][colume] = key 
	quickSort(L, low, i-1,colume)
	quickSort(L, j+1, high,colume)

def randomized_partition(A,p,r,colume):
	i = random.randint(p,r)
	A[r], A[i] = A[i], A[r]
	return partion(A,p,r,colume)


def partion(array, p, r,colume):
	x = array[r][colume]
	i = p - 1
	for j in range(p, r):
		if (array[j][colume] < x):
			i+=1
			array[j], array[i] = array[i], array[j]

	i+=1
	array[i], array[r] = array[r], array[i]
	return i

def quick_sort(array, p, r,colume):
	if p < r:
		q = randomized_partition(array, p, r,colume)
		quick_sort(array, p, q - 1,colume)	
		quick_sort(array, q + 1, r,colume)

def select_sort(a):  
	a_len=len(a)  
	for i in range(a_len):  
		min_index = i
		for j in range(i+1, a_len):  
			if(a[j]<a[min_index]):  
				min_index=j  
		if min_index != i: 
			a[i],a[min_index] = a[min_index],a[i]  
def shell_sort(a,colume):  

	a_len=len(a)  
	gap=a_len/2  
	while gap>0:  
		for i in range(a_len): 
			m=i  
			j=i+1  
			while j<a_len:  
				if a[j][colume]<a[m][colume]:  
					m=j  
				j+=gap
			if m!=i:  
				a[m],a[i]=a[i],a[m]  
		gap/=2 

    