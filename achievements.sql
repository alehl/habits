CREATE TABLE user (
	user_id SERIAL PRIMARY KEY,
	user_name VARCHAR(30) NOT NULL,
	password VARCHAR(30) DEFAULT password NOT NULL,
	);

CREATE TABLE created_achievements (
	achievement_id SERIAL PRIMARY KEY,
	user_id
		REFERENCES user
	);

CREATE TABLE inspirations (
	inspiration_id SERIAL PRIMARY KEY,
	user_id
		REFERENCES user_id
	);