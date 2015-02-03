drop table if exists task;
create table task (
	id integer primary key autoincrement,
	category text not null,
	priority integer not null,
	description text not null
);

