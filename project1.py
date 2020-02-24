import sys

# 데이터 입력
f=open("students.txt", "r")
stu_dic={}

# 입력받은 데이터를 딕셔너리에 입력
for i in f:
    a,b,c,d = i.split('\t')
    d=d[:-1] # 줄바꿈 삭제
    stu_dic[a]=[a,b,c,d]

# 데이터를 출력할 때 쓰이는 변수명과 절취선 스트링 변수    
varname='Student'+'\t'+'\t'+'Name'+'\t'+'\t'+'Midterm'+'\t'+'Final'+'\t'+'Average'+'\t'+'Grade'
cutline="---------------------------------------------------------------"            
                            
# 평균 산출 함수    
def averaging(mid, fin):
    avg='%.1f'
    avg=(mid+fin)/2     
    return avg

# 등급 산출 함수
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


# 리스트의 모든 요소들을 스트링 타입으로 변환해주는 함수
def tostring(ls):
    for i in range(len(ls)):
        ls[i]=str(ls[i])
    return(ls)

#show 함수
def show():
    print(varname)
    print(cutline)
    # sort by average
    for key in stu_dic:
        stu_dic[key][4]=round(float(stu_dic[key][4]),1)    # 소수점 한 자리 표시
    sorted_dic=sorted(stu_dic.items(), key=lambda a: -a[1][4])
    for i in range(len(sorted_dic)):
        score=sorted_dic[i][1]
        score=tostring(score)
        line='\t'.join(score)
        print(line)

# 일치하는 학번을 가진 학생의 성적만을 보여주는 partshow 함수
def partshow(stuid):
    stuid=str(stuid)
    score=stu_dic[stuid]
    score=tostring(score)
    line='\t'.join(score)
    print(line)

#search 함수
def search():
    stuid=input("Student ID: ")
    if stuid not in stu_dic.keys():
        print("NO SUCH PERSON.")
    else:                                  
        line=stu_dic[stuid]
        line=tostring(line)
        sline='\t'.join(line)
        print(varname)
        print(cutline)
        print(sline)
        
#changescore 함수        
def changescore():
    stuid=input("Student ID: ")
    
    if stuid not in stu_dic.keys():
        print("NO SUCH PERSON.")
        
    else:
        mf=input("Mid/Final? ").lower()
 
        if mf=='mid':
            nscore=int(input("Input new score: "))
            if nscore>=0 and nscore<=100:
               # 기존 점수 프린트
                print(varname)
                print(cutline)
                partshow(stuid)
                print("Score changed.")
                # 새 점수 프린트
                stu_dic[stuid][2]=nscore
                stu_dic[stuid][3]=int(stu_dic[stuid][3])
                stu_dic[stuid][4]=averaging(stu_dic[stuid][2], stu_dic[stuid][3])
                stu_dic[stuid][5]=grading(stu_dic[stuid][4])
                partshow(stuid)
                
        if mf=='final':
            nscore=int(input("Input new score: "))
            if nscore>=0 and nscore<=100:
            # 기존 점수 프린트
                print(varname)
                print(cutline)
                partshow(stuid)
                print("Score changed.")
                # 새 점수 프린트
                stu_dic[stuid][3]=nscore
                stu_dic[stuid][2]=int(stu_dic[stuid][2])
                stu_dic[stuid][4]=averaging(stu_dic[stuid][2], stu_dic[stuid][3])
                stu_dic[stuid][5]=grading(stu_dic[stuid][4])
                line=stu_dic[stuid]
                partshow(stuid)
               

#add 함수                        
def add():
    stuid=input("Student ID: ")
    if stuid in stu_dic.keys():
        print("ALREADY EXISTS")
    else:
        stuname=input("Name: ")
        mscore=int(input("Midterm Score: "))
        fscore=int(input("Final Score: "))
        print("Student added.")
        avg=averaging(mscore, fscore)
        grd=grading(avg)
        stu_dic[stuid]=[stuid, stuname, mscore, fscore, avg, grd]

#searchgrade 함수
def searchgrade():
    grd=input("Grade to search: ").upper()
    temp=0
    if grd in ['A', 'B', 'C', 'D', 'F']:
        ls=[varname, cutline]
        for key in stu_dic.keys():
            if grd==stu_dic[key][5]:
                score=stu_dic[key] # 해당 키의 값을 score에 할당
                score=tostring(score)
                line='\t'.join(score)
                ls.append(line)
            else:
                temp+=1
                if temp==len(stu_dic):
                    ls[:]=[]
                    print("NO RESULTS.")
        for var in ls:
            print(var)

#remove 함수            
def remove():
    if len(stu_dic.values())==0:
        print("List is empty.")
    else:
        rm=input("Student ID: ")  
        if rm not in stu_dic.keys():
            print("NO SUCH PERSON.")
        else:
            del stu_dic[rm]
            print("Student removed.")

#quit 함수        
def quit():
    save=input("Save data?[yes/no] ")
    if save=='yes':
        fname=input("File name: ")
        fnew=open(fname, "w")
        data=sorted(stu_dic.items(), key=lambda a: a[1][4])
        for var in data:
            a='\t'.join(var[1])
            a+='\n'
            fnew.write(a)
        fnew.close()
    else:
        f.close()            
            
                     
# 평균 산출 함수와 등급 산출 함수로 산출한 평균과 등급을 데이터에 추가
for key in stu_dic:
    stu_dic[key][2]=int(stu_dic[key][2])
    stu_dic[key][3]=int(stu_dic[key][3])
    avg=averaging(stu_dic[key][2], stu_dic[key][3])
    grd=grading(avg)
    stu_dic[key].append(avg)
    stu_dic[key].append(grd)

    

show()

while True: 
    command=input("#")
    command=command.lower() 

    if command=='show':
        show()
    if command=='search':
        search()
    if command=='changescore':
        changescore()
    if command=='add':
        add()
    if command=='searchgrade':
        searchgrade()
    if command=='remove':
        remove()
    if command=='quit':
        quit()
        break
