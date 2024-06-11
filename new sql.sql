/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - ngo
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`ngo` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `ngo`;

/*Table structure for table `donation` */

DROP TABLE IF EXISTS `donation`;

CREATE TABLE `donation` (
  `donation_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`donation_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `donation` */

insert  into `donation`(`donation_id`,`user_id`,`amount`,`date`) values 
(1,1,'1000','2022-06-23');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'ngo','ngo','ngo'),
(3,'re','re','retailer'),
(4,'user','user','user'),
(5,'sachin','s','pending'),
(7,'sa','12','retailer');

/*Table structure for table `ngo` */

DROP TABLE IF EXISTS `ngo`;

CREATE TABLE `ngo` (
  `ngo_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `ngo` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `file` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`ngo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `ngo` */

insert  into `ngo`(`ngo_id`,`login_id`,`ngo`,`place`,`phone`,`email`,`file`) values 
(1,2,'amans','kochis','8945345661','amans@gmail.com',NULL);

/*Table structure for table `proposal` */

DROP TABLE IF EXISTS `proposal`;

CREATE TABLE `proposal` (
  `proposal_id` int(11) NOT NULL AUTO_INCREMENT,
  `work_id` int(11) DEFAULT NULL,
  `retailer_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`proposal_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

/*Data for the table `proposal` */

insert  into `proposal`(`proposal_id`,`work_id`,`retailer_id`,`amount`,`date`,`status`) values 
(1,1,1,'500','2022-06-23','approve'),
(4,1,1,'10000','2023-05-13','cancel'),
(5,2,1,'100','2023-05-13','approve'),
(6,1,1,'100','2023-05-13','cancel'),
(7,1,1,'3000','2023-05-13','cancel'),
(8,3,1,'10000','2023-06-04','pending');

/*Table structure for table `retailer` */

DROP TABLE IF EXISTS `retailer`;

CREATE TABLE `retailer` (
  `retailer_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `file` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`retailer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `retailer` */

insert  into `retailer`(`retailer_id`,`login_id`,`name`,`place`,`phone`,`email`,`file`) values 
(1,3,'shahanas','kochis','9988776651','aleena22@gmail.com',NULL),
(2,7,'user qwerty','kerala','02345678907','student@gmail.com','static/retailer_id_proof88552a1b-411e-423e-bb73-7bec2f64f05fIMG_0156.JPEG');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`) values 
(1,4,'sherils','mariyas','kochis','9988776651','sherils@gmail.com');

/*Table structure for table `work` */

DROP TABLE IF EXISTS `work`;

CREATE TABLE `work` (
  `work_id` int(11) NOT NULL AUTO_INCREMENT,
  `ngo_id` int(11) DEFAULT NULL,
  `work` varchar(100) DEFAULT NULL,
  `detail` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `enddate` varchar(100) DEFAULT NULL,
  `file` varchar(1000) DEFAULT NULL,
  `amounts` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`work_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `work` */

insert  into `work`(`work_id`,`ngo_id`,`work`,`detail`,`date`,`status`,`enddate`,`file`,`amounts`) values 
(1,NULL,'work 1','ndgklblb','2022-06-23','proposal alloted',NULL,NULL,'100000'),
(2,1,'event','fss','2023-05-13','proposal alloted','2023-06-04','static/imaged7cedd8e-9484-4e84-b0c0-12a650a08355IMG_0156.JPEG','20000'),
(3,1,'event','fss','2023-05-14','approve','2023-06-04','static/image9804ff34-2d90-4ba5-9c6a-01a26e0b7eceIMG_0013.JPEG','0');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
