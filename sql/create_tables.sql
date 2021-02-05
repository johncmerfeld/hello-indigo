CREATE TABLE `Employee` (
	`id` varchar(256) NOT NULL,
	`name` varchar(256),
	`manager_id` varchar(256),
	`team_id` varchar(256),
	PRIMARY KEY (`id`)
);

CREATE TABLE `Experiment` (
	`irp_barcode` varchar(256) NOT NULL,
	`from_farm_id` varchar(256),
	`sample_crop` varchar(256),
	`sample_treatment` varchar(256),
	`sample_seed_variety` varchar(256),
	PRIMARY KEY (`irp_barcode`)
);

CREATE TABLE `Sample` (
	`irp_barcode` varchar(256) NOT NULL,
	`date_received` DATE NOT NULL,
	`received_by_employee_id` varchar(256),
	`date_treated` DATE,
	`date_planted` DATE,
	`days_between_treated_and_planted` INT,
  `date_sample_taken` DATE,
	`is_qa_needed` BOOLEAN,
	PRIMARY KEY (`irp_barcode`,`date_received`)
);

CREATE TABLE `Test` (
	`irp_barcode` varchar(256) NOT NULL,
	`date_received` DATE NOT NULL,
	`tested_by_employee_id` varchar(256),
	`date_plated_on` DATE,
	`chemical_treatment_visible` varchar(1024),
	`plating_code` varchar(256),
	`seeds_per_gram` DECIMAL(10),
	`mass_seed_extracted` DECIMAL(10),
	`plated_volume` DECIMAL(10),
	`cfu_per_1_seed` DECIMAL(10),
	`cfu_per_10_seed` DECIMAL(10),
	`cfu_per_100_seed` DECIMAL(10),
	`cfu_per_1000_seed` DECIMAL(10),
	`average_cfu_per_seed` DECIMAL(10),
	`comment` VARCHAR(1024)
);

CREATE TABLE `CfuCode` (
	`code` INTEGER NOT NULL,
	`description` VARCHAR(1024) NOT NULL
);



ALTER TABLE `Employee` ADD CONSTRAINT `Employee_fk0` FOREIGN KEY (`manager_id`) REFERENCES `Employee`(`id`);

ALTER TABLE `Sample` ADD CONSTRAINT `Sample_fk0` FOREIGN KEY (`irp_barcode`) REFERENCES `Experiment`(`irp_barcode`);

ALTER TABLE `Sample` ADD CONSTRAINT `Sample_fk1` FOREIGN KEY (`received_by_employee_id`) REFERENCES `Employee`(`id`);

ALTER TABLE `Test` ADD CONSTRAINT `Test_fk0` FOREIGN KEY (`date_received`, `irp_barcode`) REFERENCES `Sample`(`date_received`, `irp_barcode`);

ALTER TABLE `Test` ADD CONSTRAINT `Test_fk1` FOREIGN KEY (`tested_by_employee_id`) REFERENCES `Employee`(`id`);
