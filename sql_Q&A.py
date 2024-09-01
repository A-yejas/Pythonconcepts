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
select count(distinct customerd id) from table name join table name on tabname.id =tablename.id.
------------------------------------

-- Select count(*) from candidate_application_custom where date(applied_on)=current_date-1
 
-- Select count(distinct candidate_id) from candidate_application_custom where date(applied_on)=current_date-1
 
 
-- Select count(*) from candidate_application_custom where date(applied_on)=current_date-1 and iwo_status in ('rejected', 'Reject')
 
-- Select count(*) from candidate_application_custom where date(applied_on)=current_date-1 and iwo_status='proposed'
--  
-- select count(*) from job where demand_status='approved' and visibility is true
-- 
-- select count(distinct job_id) from candidate_application_custom where date(Applied_On)='April 04,2024'
 
----------------------------------
-- select C.candidate_id,C.first_name,C.last_name,
-- A.job_id, A.star_rating, A.interviewer_code, A.interviewer_name, A.interview_discussion_date,A.additional_comment,G.application_status,
-- A.iwo_status as IWO_status,A.action_taken_by, date(A.applied_on) as candidate_applied_date,A.reason,E.l2_code,E.l3_code,
-- F.name as employees_primary_skill,b.primary_skills as job_primary_skill, E.dfr_flag, E.deployment_status, E.zbillstat,
-- b.visibility
-- from candidate_application_custom as A left join job as B
-- on A.job_id=B.job_id
-- left join candidate as C
-- on A.candidate_id=C.candidate_id
-- left join job_custom as D
-- on A.job_id=D.job_id
-- left join candidate_custom as E on E.candidate_id=A.candidate_id
-- left join skill as F on a.candidate_id=F.candidate_id
-- left join applications as G on A.job_id=G.job_id and A.candidate_id=G.candidate_id
-- where A.applied_on>='June 21, 2023' and A.applied_on<current_date and b.visibility is true and F.skill_type ='primary'  
------------------------------
-- select name,count(*) from skill group by name order by count(*) desc limit 30
----------------------------------------------------
-- select A.job_id, A.demand_status, A.start_date, A.end_date,A.posted_date,B.city,C.project_id,D.account_id,D.account_name,
-- cast(G.resource_manager_ids as char(459)),E.grade_code, G.l0_code, G.l1_code, G.l2_code, G.l3_code, a.visibility
-- from job as A left join Location as B on A.location_id=B.id
-- left join project_job as C on A.project_id=C.id
-- left join Account as D on A.account_id=D.id
-- left join grade as E on A.grade_id=E.id
-- left join practice as F on A.practice_id=F.id
-- left join job_custom as G on A.job_id=G.job_id
-- where a.visibility is true
 
------------
select a.email,a.candidate_id,a.first_name,a.last_name,C.country,b.deployment_status, b.l0_code,
case
when b.deployment_status in ('AAFD', 'AFD', 'AFD-Regular', 'AAFD Released by PM', 'AFD Regular') then 'Bench' else 'Non-Bench' end as BenchNonBench,
case
when b.l0_code in ('52600401','54914523','55802103','55421734','52600403','55322984','52600404','55049740','55821011') then 'DBS'
when b.l0_code in ('55377824', '50302786','55837977','54746267','55552759','55552753','55318251','55316388') then 'ERS'
when b.l0_code in ('56005075','56006083') then 'APME'
else 'N/A'
end as LOB
from candidate as A left join
candidate_custom as B on a.candidate_id=B.candidate_id left join location as C on a.location_id=C.id
----
 
-- select A.email,A.candidate_id,A.first_name,A.last_name,C.country,b.deployment_status,B.dfr_flag, B.zbillstat,B.l0_code from candidate as A left join
-- candidate_custom as B on a.candidate_id=B.candidate_id left join location as C on a.location_id=C.id where c.country !='Germany' and  deployment_status in ('AFD-Regular','AAFD') or B.dfr_flag in('yes','Yes') or zbillstat in ('N')
 
----------------------------------------------------
 
-- select C.candidate_id,C.first_name,C.last_name,
-- A.job_id, A.star_rating, A.interviewer_code, A.interviewer_name, A.interview_discussion_date,A.additional_comment,G.application_status,
-- A.iwo_status as IWO_status,A.action_taken_by, date(A.applied_on) as candidate_applied_date,A.reason,E.l2_code,E.l3_code,
-- F.name as employees_primary_skill,b.primary_skills as job_primary_skill, E.dfr_flag, E.deployment_status, E.zbillstat,
-- b.visibility
-- from candidate_application_custom as A left join job as B
-- on A.job_id=B.job_id
-- left join candidate as C
-- on A.candidate_id=C.candidate_id
-- left join job_custom as D
-- on A.job_id=D.job_id
-- left join candidate_custom as E on E.candidate_id=A.candidate_id
-- left join skill as F on a.candidate_id=F.candidate_id
-- left join applications as G on A.job_id=G.job_id and A.candidate_id=G.candidate_id
-- where A.applied_on>='January 1, 2024' and A.applied_on<current_date and b.visibility is true and F.skill_type ='primary'
-- UNION ALL
-- select C.candidate_id,C.first_name,C.last_name,
-- A.job_id, A.star_rating, A.interviewer_code, A.interviewer_name, A.interview_discussion_date,A.additional_comment,G.application_status,
-- A.iwo_status as IWO_status,A.action_taken_by, date(A.applied_on) as candidate_applied_date,A.reason,E.l2_code,E.l3_code,
-- F.name as employees_primary_skill,b.primary_skills as job_primary_skill, E.dfr_flag, E.deployment_status, E.zbillstat,
-- b.visibility
-- from candidate_application_custom as A left join job as B
-- on A.job_id=B.job_id
-- left join candidate as C
-- on A.candidate_id=C.candidate_id
-- left join job_custom as D
-- on A.job_id=D.job_id
-- left join candidate_custom as E on E.candidate_id=A.candidate_id
-- left join skill as F on a.candidate_id=F.candidate_id
-- left join applications as G on A.job_id=G.job_id and A.candidate_id=G.candidate_id
-- where A.applied_on>='June 21, 2023' and A.applied_on<'January 1, 2024' and b.visibility is true and F.skill_type ='primary' and
-- A.iwo_status in('Auto released as final selected in other SR','Block in Other SR','Customer Blocked','Final Select','Pending with Initiator',
-- 'Pending with WPC','proposed','Select','Shortlisted by initiator','Shortlisted in Other SR','Shortlist')
------------------------------------------------------------
# for pic the email ids and job id
select jc.job_id,can.email from job_custom jc, candidate can where 1=1 
AND jc.tpg_manager_ids=can.candidate_id 
AND jc.job_id in ('ISD-/ISD-/2023/2194769',
'DRYI/DRYI/2023/2088607') 

'''

# If you inheritance more than one parent class that is called multi inheritance

