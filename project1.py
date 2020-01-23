# 딕셔너리 만들기

f=open("students.txt", "r")
stu_dic={}
stu_list=[]
name_list=[]

for i in f:
    a,b,c,d = i.split('\t')
    d=d[:-1]
    stu_list.append(a)
    name_list.append(b)
    stu_dic[a]=[a,b,c,d]
        
def averaging(mid, fin):
    avg=0.0 # 이거 꼭 있어야 하나?
    avg=(mid+fin)/2     
        # 소수점 이하 첫째자리까지만 나오게 추가    
    return avg

def grading(avg):
    if avg>=90:
        grade='A'
    elif avg>=80:
        grade='B'
    elif avg>=70:
        grade='C'
    elif avg>=60:
        grade='D'
    else:
        grade='F'
    return grade

# attach average and grade
for key in stu_dic:
    stu_dic[key][2]=int(stu_dic[key][2])
    stu_dic[key][3]=int(stu_dic[key][3])
    avg=averaging(stu_dic[key][2], stu_dic[key][3])
    grd=grading(avg)
    stu_dic[key].append(avg)
    stu_dic[key].append(grd)

def tostring(ls):
    for i in range(len(ls)):
        ls[i]=str(ls[i])
    return(ls)

def toint(ls):
    for i in range(2,5):
        ls[i]=int(ls[i])
    return(ls)

def show():
    varname='Student'+'\t'+'\t'+'Name'+'\t'+'\t'+'Midterm'+'\t'+'Final'+'\t'+'Average'+'\t'+'Grade'
    cutline="---------------------------------------------------------------"
    print(varname)
    print(cutline)
    # sort by average    
    sorted_dic=sorted(stu_dic.items(), key=lambda a: -a[1][3])
    for i in range(len(sorted_dic)):
        score=sorted_dic[i][1]
        score=tostring(score)
        line='\t'.join(score)
        print(line)

def partshow(stuid):
    stuid=str(stuid)
    varname='Student'+'\t'+'\t'+'Name'+'\t'+'\t'+'Midterm'+'\t'+'Final'+'\t'+'Average'+'\t'+'Grade'
    cutline="---------------------------------------------------------------"
    print(varname)
    print(cutline)
    score=stu_dic[stuid]
    line='\t'.join(score)
    print(line)
    
    
    
def search():
    stuid=input("Student ID: ")
    if stuid not in stu_dic.keys():
        print("NO SUCH PERSON.")
    else:                                  
        varname='Student'+'\t'+'\t'+'Name'+'\t'+'\t'+'Midterm'+'\t'+'Final'+'\t'+'Average'+'\t'+'Grade'
        cutline="---------------------------------------------------------------"
        print(varname)
        print(cutline)
        line=stu_dic[stuid]
        line=tostring(line)
        sline='\t'.join(line)
        print(sline)

def changescore():
    
    stuid=input("Student ID: ")
    
    if stuid not in stu_dic.keys():
        print("NO SUCH PERSON.")
        stuid=input("Student ID: ")   # while문으로 수정?
        
    else:
        mf=input("Mid/Final? ")
    
        if mf!='mid' and mf!='final':
            mf=input("Mid/Final? ")      # while 문으로 수정?
        
        else: 
            if mf=='mid':
                nscore=int(input("Input new score: "))
                if nscore>=0 and nscore<=100:
                    # 여기서 학번을 받을 수 있는 show를 실행하면 좋을텐데...클래스 같은!
                    # 기존 점수 프린트
                    partshow(stuid)
                    print("Score changed.")
                    # 새 점수 프린트
                    stu_dic[stuid][2]=nscore
                    print(type(stu_dic[stuid][3]))
                    stu_dic[stuid][3]=int(stu_dic[stuid][3])
                    stu_dic[stuid][4]=averaging(stu_dic[stuid][2], stu_dic[stuid][3])
                    stu_dic[stuid][5]=grading(stu_dic[stuid][4])
                    partshow(stuid)
                else:
                     nscore=int(input("Input new score: "))
            if mf=='final':
                nscore=int(input("Input new score: "))
                if nscore>=0 and nscore<=100:
                    # 여기서 학번을 받을 수 있는 show를 실행하면 좋을텐데...클래스 같은!
                    # 기존 점수 프린트
                    partshow(stuid)
                    print("Score changed.")
                    # 새 점수 프린트
                    stu_dic[stuid][3]=nscore
                    stu_dic[stuid][4]=averaging(stu_dic[stuid][2], stu_dic[stuid][3])
                    stu_dic[stuid][5]=grading(stu_dic[stuid][4])
                    line=stu_dic[stuid]
                    partshow(stuid)
                else:
                     nscore=int(input("Input new score: "))
  
show()

command=input("#")
lcommand=command.lower()
command_list=['show', 'search', 'changescore', 'add', 'searchgrade', 'remove', 'quit']
while lcommand not in command_list:
    input("#") 

if lcommand=='show':
    show()
if lcommand=='search':
    search()
if lcommand=='changescore':
    changescore()
if lcommand=='add':
    changescore()
if lcommand=='searchgrade':
    changescore()
if lcommand=='remove':
    remove()
if lcommand=='quit':
    quit()
    
    
f.close()