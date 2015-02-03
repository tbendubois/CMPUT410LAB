create table task (
	id primary key autoincrement,
	category text not null,
	priority integer not null,
	description text not null
);

