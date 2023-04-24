CREATE SCHEMA IF NOT EXISTS `easy_health`;

SET SQL_MODE = `NO_AUTO_VALUE_ON_ZERO`;
START TRANSACTION;
SET time_zone = `+00:00`;

CREATE TABLE IF NOT EXISTS `client` (
	`health_plan`	VARCHAR(30) NOT NULL,
	`id`	INTEGER NOT NULL,
	`active`	BOOLEAN NOT NULL,
	`name`	VARCHAR(50) NOT NULL,
	`email`	VARCHAR(30) NOT NULL,
	`password`	VARCHAR(24) NOT NULL,
	`phone_number`	INTEGER NOT NULL,
	PRIMARY KEY(`id`)
);
CREATE TABLE IF NOT EXISTS `health_plan` (
	`name`	VARCHAR(30) NOT NULL,
	PRIMARY KEY(`name`)
);
CREATE TABLE IF NOT EXISTS `professional` (
	`provides_home_service`	BOOLEAN NOT NULL,
	`specialty`	VARCHAR(20) NOT NULL,
	`council_registration`	INTEGER NOT NULL,
	`twitter`	VARCHAR(20),
	`insta`	VARCHAR(20),
	`linkedin`	VARCHAR(20),
	`bio`	VARCHAR(50),
	`id`	INTEGER NOT NULL,
	`active`	BOOLEAN NOT NULL,
	`name`	VARCHAR(50) NOT NULL,
	`email`	VARCHAR(30) NOT NULL,
	`password`	VARCHAR(24) NOT NULL,
	`phone_number`	INTEGER NOT NULL,
	PRIMARY KEY(`id`)
);
CREATE TABLE IF NOT EXISTS `subspecialty` (
	`name`	VARCHAR(20) NOT NULL,
	PRIMARY KEY(`name`)
);
CREATE TABLE IF NOT EXISTS `client_address` (
	`client_id`	INTEGER NOT NULL,
	`id`	INTEGER NOT NULL,
	`state`	VARCHAR(2) NOT NULL,
	`city`	VARCHAR(20) NOT NULL,
	`street`	VARCHAR(100) NOT NULL,
	`complement`	VARCHAR(100),
	UNIQUE(`client_id`),
	FOREIGN KEY(`client_id`) REFERENCES `client`(`id`),
	PRIMARY KEY(`id`)
);
CREATE TABLE IF NOT EXISTS `health_plan_professional` (
	`health_plan_id`	VARCHAR(10),
	`professional_id`	INTEGER,
	FOREIGN KEY(`professional_id`) REFERENCES `professional`(`id`),
	FOREIGN KEY(`health_plan_id`) REFERENCES `health_plan`(`name`)
);
CREATE TABLE IF NOT EXISTS `professional_address` (
	`professional_id`	INTEGER NOT NULL,
	`id`	INTEGER NOT NULL,
	`state`	VARCHAR(2) NOT NULL,
	`city`	VARCHAR(20) NOT NULL,
	`street`	VARCHAR(100) NOT NULL,
	`complement`	VARCHAR(100),
	FOREIGN KEY(`professional_id`) REFERENCES `professional`(`id`),
	PRIMARY KEY(`id`)
);
CREATE TABLE IF NOT EXISTS `subspecilaty_professional` (
	`subspecialty_id`	VARCHAR(10),
	`professional_id`	INTEGER,
	FOREIGN KEY(`subspecialty_id`) REFERENCES `subspecialty`(`name`),
	FOREIGN KEY(`professional_id`) REFERENCES `professional`(`id`)
);