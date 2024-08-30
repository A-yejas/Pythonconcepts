'''
1.What is SQL?
1.Relational Data base,
CRUD:- Create ,Read, Update & Delete
2.Sql Data Types:Signed, Unsigned
DDl:- DATA Defination language:- Create , alter, rname,Truncate, & drop



'''
'''
create table  (tablename)( column varachar(255), column name bigint);

create table tab name (
    id bigint NOT null Auto_Increment,
    Name varchar(255) Not null,
    Prive int,
    Primary key(id)
select Distinct column name from table name  -- Given answers unique one only.
Insert into 'table name'(column names) values (); -- Insert data into tables
Insert into 'table name '(colums names) values('pd',null);
Order by:- user to sort the column based by assending and des order
select * from table name order by column name ASC;
select * from table name order by column name DESC;
Not null:-
select * from table name where 'coulmn name' is NOT NULL;
select * from table name where 'coulmn name' is  NULL;
#Update:-
Update 'table name' set 'column name'='value' where id=2;
Delete:-
Delete from 'table name' where id=6
LIMIT:-
SELECT * FROM Customers LIMIT 10 ;
SELECT * FROM Customers Order By (Column name) asc LIMIT 10;
SELECT max(salary) FROM Customers 
SELECT avg(salary) FROM Customers 
SELECT max(salary) FROM Customers limit 1
Count:-
Select count(*) from table name
Select * from table name where name like 'A%' -->>> Starts from A
Select * from table name where name like '%A'  --->>> End from A.
Select * from table name where name like 'P_%'  -->> Start P match any charcter
IN:-
select * from table name where col name in (city names any thing)
select * from table name where col name NOT in (city names any thing)
Between:-
select * from tablename where colname between 400 AND 500;
Group by:-
select * from table name Group by column name
select (id,address) table name Group by column name
select count(id), address from table name Group by column name(ex:- Gremany)
select count(id), address from table name Group by column name(ex:- Gremany) Having count(id) > 7;
ex:- select count(CustomerID), Country from Customers Group by Country Having count(CustomerID) > 5
After group by we are not using 'where', there we use 'Having' user where we cannot use 'where' keyword;
Drop:-
drop table table name;  -- delete the data
Truncate table tablename -- Clear the data only not delete the entire columns.delete the values only.
Alter:-
ALTER TABLE table name RENAME column columnname to columnname
ALTER TABLE table name MOdify column columnname varchar(64)
ALTER TABLE table name ADD column (columnname text(100) NOT NULL)
ALTER TABLE table name DROP column columnname identity
Join:-
select * from table name join table name on tabname.id =tablename.id
select count(*) from table name join table name on tabname.id =tablename.id
select count(distinct customerd id) from table name join table name on tabname.id =tablename.id









 

'''

# If you inheritance more than one parent class that is called multi inheritance
class Mat_Oper():
    name = 'sriram'
    def add(self, a, b):
        print('sum is', a + b)

    def sub(self, a, b):
        print('sub is', a - b)

class Number_Oper():
    def in_ope(self, a, b):
        if a in b : print('exit')

    def not_in_ope(self, a, b):
        if a not in b: print('Not exit')

class Python_Operators(Number_Oper,Mat_Oper):
    def and_oper(self, a, b):
        if a or b: print('and oper')

ins = Python_Operators()
((ins.not_in_ope()))
