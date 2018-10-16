from bs4 import BeautifulSoup
import requests
import datetime
from _overlapped import NULL
import smtplib
import pymysql
from email.mime.text import MIMEText
def callmail(msg1,email):
    smtp_ssl_host = 'smtp.gmail.com'  
    smtp_ssl_port = 465
    username = 'reminderfromvaibhav'
    password = 'hiinnovacer'
    sender = "reminderfromvaibhav@gmail.com"
    targets = [email]
     
    msg = MIMEText(msg1)
    msg['Subject'] = 'Reminder'
    msg['From'] = sender
    msg['To'] = ', '.join(targets)
     
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(sender, targets, msg.as_string())

db = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='innovacer')
cursor=db.cursor()
cursor.execute("USE innovacer") # select the database
cursor.execute("SHOW TABLES")    # execute 'SHOW TABLES' (but data is not returned)
flag1=0
flag2=0
for (table_name,) in cursor:
    if (table_name=="userdata"):
        flag1=1
    if (table_name=="seriesdata"):
        flag2=1     
if(flag1 is 0):
    sql = """CREATE TABLE USERDATA (EMAIL  CHAR(50) NOT NULL,SERIES  CHAR(255) NOT NULL)"""
    cursor.execute(sql)
if(flag2 is 0):
    sql = """CREATE TABLE SERIESDATA (SERIES  CHAR(255) NOT NULL,DATE  CHAR(255) NOT NULL,DATEPRINT CHAR(255) NOT NULL)"""
    cursor.execute(sql)
def insertuserdata(email,series):
    sql = "INSERT INTO USERDATA(EMAIL, \
       SERIES) \
       VALUES ('%s', '%s')" % \
       (email, series)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
def findnext(seasonurl):
    if(1):
        html2 = requests.get(seasonurl)
        soup2 = BeautifulSoup(html2.text, 'html5lib')
        airdate = soup2.find_all('div', class_="airdate")
            
        episode=-1
        date=[]
        for d in airdate:
            episode=episode+1
            date.append(d.getText())
                        
        released=1  
        known=1
        year=0            
        for j in range(0,episode+1):
            date_str=date[j]
            date_final=[]
            for i in range(0, len(date_str)):
                if(date_str[i] is not NULL and date_str[i]!=' ' and date_str[i]!='\n'):
                    date_final.append(date_str[i])
            out_final="".join(str(x) for x in date_final) 
            l=len(out_final)
            flag=0
            if(l>7):
                c=date_final[1]
                if(c=='0' or c=='1' or c=='2' or c=='3' or c=='4' or c=='5' or c=='6' or c=='7' or c=='8' or c=='9'):
                    month=[]
                    for i in range(2,(len(out_final)-4)):
                        month.append(date_final[i])
                    month="".join(str(x) for x in month)    
                else:
                    flag=1   
                    month=[]
                    for i in range(1,(len(out_final)-4)):
                        month.append(date_final[i])
                    month="".join(str(x) for x in month) 
                if(month=="Jan."):   
                    mon="01"
                if(month=="Feb."):   
                    mon="02"    
                if(month=="Mar."):   
                    mon="03" 
                if(month=="Apr."):   
                    mon="04"    
                if(month=="May"):   
                    mon="05"    
                if(month=="Jun."):   
                    mon="06"    
                if(month=="Jul."):   
                    mon="07"    
                if(month=="Aug."):   
                    mon="08"    
                if(month=="Sep."):   
                    mon="09"    
                if(month=="Oct."):
                    mon="10"    
                if(month=="Nov."):   
                    mon="11"
                if(month=="Dec."):   
                    mon="12"      
                if(flag is 0):      
                    datestr=date_final[0]+date_final[1]
                else:
                    datestr="0"+date_final[0]
                yearstr=date_final[l-4]+date_final[l-3]+date_final[l-2]+date_final[l-1]
                date_now=str(datestr)+mon+str(yearstr)
                d=datetime.datetime.strptime(date_now, "%d%m%Y").date() 
                CurrentDate = datetime.datetime.now()
                if CurrentDate.date() < d:
                    released=0
                    break   
            else:
                if(l is 0):
                    known=0
                    break
                else:
                    year=1
                    break    
        if(j is 0):
            if(year is 1):
                z="New season of "+verify+"  will be live in "+out_final
            else:
                if(known is 1):
                    if(released is 0):
                        z="New season of "+verify+"  will be live on "+out_final
                        insertseriesdata(verify1,date_now,out_final)
                    else:
                        z=verify+" has stopped streaming and no other details are available"
                        insertseriesdata(verify1, "stopped",out_final)
                else:
                    z="New season of "+verify+" dates are not known"
        else:
            if(year is 1):
                z="Next episode of "+verify+" will be live in "+out_final
            else:
                if(known is 1):
                    if(released is 0):
                        z="Next episode of "+verify+" will be live on "+out_final
                        insertseriesdata(verify1,date_now,out_final)
                    else:
                        z=verify+" has stopped streaming and no further details are available"
                        insertseriesdata(verify1, "stopped",out_final)
                else:
                    z="Next episode dates of "+verify+" are not known"
    return z    
def insertseriesdata(name,date,dateprint):
    sql = "INSERT INTO SERIESDATA(SERIES, \
       DATE,DATEPRINT) \
       VALUES ('%s', '%s','%s')" % \
       (name, date,dateprint)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
def findseriesdata(name):
    sql = "SELECT * FROM SERIESDATA"
    try:
        cursor.execute(sql)
        for row in cursor:
            name=str(name)
            namedata=str(row[0])
            if(namedata==name): 
                z=row[1]
                if(z == "stopped"):
                    return 1
                else:
                    d=datetime.datetime.strptime(z, "%d%m%Y").date() 
                    CurrentDate = datetime.datetime.now()
                    if CurrentDate.date() < d:
                        return row[2]
                    deleteold(series)
                    return 0      
    except Exception as e:
        print("Exeception occured:{}".format(e))
        db.rollback()
def deleteold(series):
    sql="DELETE FROM SERIESDATA WHERE SERIES='"+series+"'";
    try:
        cursor.execute(sql)
    except Exception as e:
        print("Exeception occured:{}".format(e))
        db.rollback() 
            
print("Enter Email-ID:")
email=input()
atcheck = email.find('@')
dotcheck= email.find('.',atcheck+1)
length=len(email)
while((atcheck <= 0) or (dotcheck is -1) or (length is (dotcheck+1))):
    print("Enter valid email id:")
    email=input()
    atcheck = email.find('@')
    dotcheck= email.find('.',atcheck+1)
    length=len(email)
print("Enter series:")       
series=input()
insertuserdata(email, series)
count=[]
for i in range(0,len(series)):
    if(series[i] is ','):
        count.append(i)
    
count.append(len(series))    
for q in range(0,len(count)):
    inp=[]
    if(q==0):
        for j in range(0,count[q]):
            inp.append(series[j])
    else:
        if(q!=len(count)):
            for j in range(count[q-1]+1,count[q]):
                inp.append(series[j])   
        else:
            for j in range(count[q-1]+1,len(series)):
                inp.append(series[j])
    inp="".join(str(x) for x in inp)
    name=[ ]
    for i in range(0, len(inp)):
        if(inp[i] is ' '):
            name.append('%')
            name.append('2')
            name.append('0')
        else:
            name.append(inp[i])
    name="".join(str(x) for x in name)  
    searchurl="https://www.imdb.com/find?q="+name+"&s=tt&ttype=tv&ref_=fn_tv"
    
    ################################################################
    html = requests.get(searchurl)
    soup = BeautifulSoup(html.text, 'html5lib')
    
    
    s=[]
    celeb_name = []
    serieslink = soup.find_all(class_='result_text')
    sl=str(serieslink)
    if(sl =="[]"):
        z="No "+inp+" series exist"
        if(q == 0):
            mail=z
        else:
            mail=mail+'\n'+z
    else:
        s1=serieslink[0]
        
        verify=s1.text
        verify1=[ ]
        for i in range(0, len(verify)):
            if(verify[i+1] is '('):
                break
            else:
                verify1.append(verify[i+1])
        verify1.pop()        
        verify1="".join(str(x) for x in verify1)
        flag=0
        if(list(inp.lower()) == list(verify1.lower())):
            flag=1  
        if(flag is 0):
            print("Do You mean: "+verify+" instead of "+inp)
            print("Type yes or no")
            temp=input()
            if(temp=="no"):
                z="No "+inp+" series exist"
                if(q == 0):
                    mail=z
                    continue
                else:
                    mail=mail+'\n'+z
                    continue
        verify1=[]
        for i in range(0, len(verify)):
            if(verify[i+1] is '('):
                break
            else:
                verify1.append(verify[i+1])
        verify1.pop()        
        verify1="".join(str(x) for x in verify1)
        dt=findseriesdata(verify1)
        if(dt is not 0 and dt!=None):
            if(dt is 1):
                z=verify+" has stopped streaming and no more information is available"
            else:
                z="Next episode of "+verify+" will be live on "+ dt
            if(q == 0):
                mail=z
                continue
            else:
                mail=mail+'\n'+z
                continue
        else:            
            s  = []
            anchor=s1.a
            s2 = str(anchor)
            for i in s2:
                s.append(i)
            
            outseries= []
            for i in range(0, len(s)):
                if(s[i] is 'f'):
                    j=i+3
                    while(s[j] != '"'):
                        outseries.append(s[j])
                        j=j+1
                    break    
            
            titleurl="".join(str(x) for x in outseries)
            titleurl="https://www.imdb.com"+titleurl
            
            
            
            ##########################################
            html1 = requests.get(titleurl)
            soup1 = BeautifulSoup(html1.text, 'html5lib')
            seasonlink = soup1.find_all('div', class_="seasons-and-year-nav")
            sl=str(seasonlink)
            if(sl =="[]"):
                z="No "+inp+" series exist"
                print(z)
                if(q == 0):
                    mail=z
                else:
                    mail=mail+'\n'+z
            else:    
                lastseason=seasonlink[0]
                lastseason=str(lastseason.a)
                season  = []
                for i in lastseason:
                    season.append(i)
                outseason= []
                for i in range(0, len(season)):
                    if(season[i] is '<' and season[i+1] is 'a' ):
                        j=i+9
                        while(season[j] != '"'):
                            outseason.append(season[j])
                            j=j+1
                        break 
                seasonurl="".join(str(x) for x in outseason)   
                seasonurl="https://www.imdb.com"+seasonurl
                z=findnext(seasonurl)
            if(q == 0):
                mail=z
            else:
                mail=mail+'\n'+z   
print("Thanks for visiting,please check your mail")
print(mail)
callmail(mail,email)             
