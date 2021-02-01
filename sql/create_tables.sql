CREATE TABLE `Employee` (
	`id` varchar(256) NOT NULL,
	`name` varchar(256),
	`manager_id` varchar(256) NOT NULL,
	`team_id` varchar(256) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Experiment` (
	`irp_barcode` varchar(256) NOT NULL,
	`from_farm_id` varchar(256) NOT NULL,
	`sample_crop` varchar(256) NOT NULL,
	`sample_treatment` varchar(256) NOT NULL,
	`sample_seed_variety` varchar(256) NOT NULL,
	PRIMARY KEY (`irp_barcode`)
);

CREATE TABLE `Sample` (
	`irp_barcode` varchar(256) NOT NULL,
	`date_received` DATE NOT NULL,
	`received_by_employee_id` varchar(256) NOT NULL,
	`date_treated` DATE NOT NULL,
	`date_planted` DATE NOT NULL,
	`days_between_treated_and_planted` INT NOT NULL,
  `date_sample_taken` DATE,
	`is_qa_needed` BOOLEAN NOT NULL,
	PRIMARY KEY (`irp_barcode`,`date_received`)
);

CREATE TABLE `Test` (
	`irp_barcode` varchar(256) NOT NULL,
	`date_received` DATE NOT NULL,
	`tested_by_employee_id` varchar(256) NOT NULL,
	`date_plated_on` DATE NOT NULL,
	`chemical_treatment_visible` varchar(1024) NOT NULL,
	`plating_code` varchar(256) NOT NULL,
	`seeds_per_gram` DECIMAL(10) NOT NULL,
	`mass_seed_extracted` DECIMAL(10) NOT NULL,
	`plated_volume` DECIMAL(10) NOT NULL,
	`cfu_per_1_seed` DECIMAL(10) NOT NULL,
	`cfu_per_10_seed` DECIMAL(10) NOT NULL,
	`cfu_per_100_seed` DECIMAL(10) NOT NULL,
	`cfu_per_1000_seed` DECIMAL(10) NOT NULL,
	`average_cfu_per_seed` DECIMAL(10) NOT NULL,
	`comment` varchar(1024) NOT NULL
);
/*
ALTER TABLE `Employee` ADD CONSTRAINT `Employee_fk0` FOREIGN KEY (`manager_id`) REFERENCES `Employee`(`id`);

ALTER TABLE `Employee` ADD CONSTRAINT `Employee_fk1` FOREIGN KEY (`team_id`) REFERENCES `Team`(`id`);

ALTER TABLE `Experiment` ADD CONSTRAINT `Experiment_fk0` FOREIGN KEY (`from_farm_id`) REFERENCES `Farm`(`ID`);

ALTER TABLE `Sample` ADD CONSTRAINT `Sample_fk0` FOREIGN KEY (`irp_barcode`) REFERENCES `Experiment`(`irp_barcode`);

ALTER TABLE `Sample` ADD CONSTRAINT `Sample_fk1` FOREIGN KEY (`received_by_employee_id`) REFERENCES `Employee`(`id`);

ALTER TABLE `Test` ADD CONSTRAINT `Test_fk0` FOREIGN KEY (`irp_barcode`) REFERENCES `Experiment`(`irp_barcode`);

ALTER TABLE `Test` ADD CONSTRAINT `Test_fk1` FOREIGN KEY (`date_received`) REFERENCES `Sample`(`date_received`);

ALTER TABLE `Test` ADD CONSTRAINT `Test_fk2` FOREIGN KEY (`tested_by_employee_id`) REFERENCES `Employee`(`id`);
*/
