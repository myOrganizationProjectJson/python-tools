import MySQLdb  
  
try:  
#db='dbname'
    conn = MySQLdb.connect(host='localhost',user='root',passwd='test',port=3306)  
    conn.select_db('test')  
	 
	cur = conn.cursor()  
  
    #cur.execute('create database if not exists PythonDB')  
   
    cur.execute('select * from a limit 1')  
    row=cur.fetchone()
#fetchall()
    print row
    
    #value = [1,'ACdreamer','student']  
    #cur.execute('insert into Test values(%s,%s,%s)',value)  
  
   # values = []  
    #for i in range(20):  
     #   values.append((i,'Hello World!','My number is '+str(i)))  
  
    #cur.executemany('insert into Test values(%s,%s,%s)',values)  
   # cur.execute('update Test set name="ACdreamer" where id=3')  
  
    conn.commit()  
    cur.close()  
    conn.close()  
except MySQLdb.Error,msg:  
    print "MySQL Error %d: %s" %(msg.args[0],msg.args[1])  