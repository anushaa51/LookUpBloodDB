drop table distance;
drop table blood_br;
drop table branch;
drop table organization;
drop table blood;
drop table donor;
drop table dummy;

create table donor (d_id varchar(5) primary key , name varchar(20), dob date, gender
varchar(6), b_group varchar(5), phone varchar(12), weight float);

create table blood (b_id varchar(5) primary key, hgb_level float, wbc float, rbc float, platelet float, date date, d_id varchar(5) unique,
foreign key (d_id) references donor(d_id) on delete cascade on update cascade);

create table organization( o_id varchar(5) primary key, org_name varchar(30), no_of_br int);

create table branch(o_id varchar(5), br_id varchar(5), address varchar(35), br_phone
varchar(12), foreign key (o_id) references organization(o_id) on delete cascade on update
cascade, primary key(br_id, o_id));

create table blood_br(b_id varchar(5) primary key, o_id varchar(5), br_id varchar(5), foreign
key (o_id,br_id) references branch (o_id,br_id) on delete cascade on update cascade,foreign key
(b_id) references blood(b_id) on delete cascade on update cascade);

create table distance(o_id varchar(5), br_id varchar(5), h_id varchar(5), dist float, foreign key
(o_id, br_id) references branch(o_id, br_id) on delete cascade on update cascade, primary
key(o_id, br_id, h_id));

create table dummy (name varchar(10));




create trigger forDate after insert on dummy for each row begin call delDate(); end;//
create procedure delDate() begin delete from blood where (select datediff(curdate(),date)) > 46; end;//

