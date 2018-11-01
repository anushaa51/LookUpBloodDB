drop table distance;
drop table blood_br;
drop table branch;
drop table organization;
drop table blood;
drop table donor;

create table donor (d_id varchar(5) primary key , name varchar(20), dob date, gender
varchar(6), b_group varchar(5), phone varchar(12), weight float);

create table blood (b_id varchar(5) primary key, hgb_level float, wbc float, rbc float, platelet float, date date, d_id varchar(5) unique,
foreign key (d_id) references donor(d_id) on delete cascade on update cascade);

create table organization( o_id varchar(5) primary key, org_name varchar(30), no_of_br int);

create table branch(o_id varchar(5), br_id varchar(5), address varchar(35), br_phone
varchar(12), foreign key (o_id) references organization(o_id) on delete cascade on update
cascade, primary key(br_id, o_id));

create table blood_br(b_id varchar(5) primary key, o_id varchar(5), br_id varchar(5), foreign
key (o_id) references organization (o_id) on delete cascade on update cascade, foreign key
(br_id) references branch(br_id) on delete cascade on update cascade,foreign key
(b_id) references blood(b_id) on delete cascade on update cascade);

create table distance(o_id varchar(5), br_id varchar(5), h_id varchar(5), dist float, foreign key
(o_id, br_id) references branch(o_id, br_id) on delete cascade on update cascade, primary
key(o_id, br_id, h_id));

-- create trigger datec after insert on blood when ( datediff(select convert(varchar,getdate(),23),new.date) > 46) 
-- mysql> create procedure heck(param varchar(5)) begin declare bid varchar(5); declare cur1 cursor for select b_id from blood; open cur1; loop fetch cur1 into bid; delete from blood where bid = param and b_id = bid; end loop; close cur1; end;//

-- mysql> create trigger datec after insert on blood for each row when ((select datediff(curdate(),new.date)) > 46) begin call heck(new.b_id); end; //



create trigger forDate after insert on dummy for each row begin call delDate(); end;//
create procedure delDate() begin delete from blood where (select datediff(curdate(),date)) > 46; end;//
