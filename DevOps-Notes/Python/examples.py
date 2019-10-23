files_list=['file1.txt','file2.txt']
#output_file= 'file-final.txt'
#out= open('output_file.txt','w+')
'''appending two file and keeping extral file'''
#Method-1
# with open('output_file.txt','w') as outline_file:
# 	for file in files_list:
# 		with open(file) as inline_file:
# 			for line in inline_file:
# 				print line
# 				outline_file.write(line)
# Method-2
f1= open('file1.txt','r')
f1_line= f1.read()
f2= open('file2.txt','r')
f2_line= f2.read()

f3= open('file3.txt','w+')
f3.write(f1_line)
if f2_line not in f3:
	f3.write(f2_line)
f1.close()
f2.close()
f3.close()

'''Reading CSV file '''
# import csv 
# with open('test.csv','r') as csv_file:
# 	red_csv= csv.reader(csv_file)
# 	header= red_csv.next()
# 	job_index = header.index("job")
# 	statu_Index = header.index("statu")
# 	date_indeck= header.index("date")
# 	#red_csv.readrow(('job', 'statu')
# 	coordList=[]
# 	for row in red_csv:
# 		if row[statu_Index] =='down':
# 			#status = row[statu_Index]
# 			job_name = row[job_index]
# 			date_fail = row[date_indeck]
# 			coordList.append([job_name,date_fail])
# 	print coordList