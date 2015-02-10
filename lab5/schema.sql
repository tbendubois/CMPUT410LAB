drop table IF exists task;
create table task (
	id integer primary key not null,
	category text not null,
	priority integer not null,
	description text not null
);

