-- MySQL dump 10.13  Distrib 5.1.54, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: myseun
-- ------------------------------------------------------
-- Server version	5.1.54-1ubuntu4

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `blog_entries`
--

DROP TABLE IF EXISTS `blog_entries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_entries` (
  `entry_ID` int(9) unsigned NOT NULL AUTO_INCREMENT,
  `posted` int(11) unsigned NOT NULL,
  `categoryID` tinyint(2) unsigned NOT NULL,
  `title` char(255) NOT NULL,
  `entry` text NOT NULL,
  PRIMARY KEY (`entry_ID`),
  KEY `posted` (`posted`),
  KEY `categoryID` (`categoryID`),
  FULLTEXT KEY `title` (`title`,`entry`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_entries`
--

LOCK TABLES `blog_entries` WRITE;
/*!40000 ALTER TABLE `blog_entries` DISABLE KEYS */;
INSERT INTO `blog_entries` VALUES (1,1050942000,1,'About miester','I was born in michigan in 1980 in a small town called Adrian. \n         My mother is named Sue, while my father is named Mike. \n         They currently live in a small town called East Jordan. On April \n         27th, 2003 I will graduate from Eastern Michigan University with a \n         degree in Computer Information Systems.');
/*!40000 ALTER TABLE `blog_entries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `branches`
--

DROP TABLE IF EXISTS `branches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `branches` (
  `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
  `street_address` char(150) NOT NULL,
  `city_name` char(40) NOT NULL,
  `state_name` char(40) NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `company_id` tinyint(4) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `branches`
--

LOCK TABLES `branches` WRITE;
/*!40000 ALTER TABLE `branches` DISABLE KEYS */;
INSERT INTO `branches` VALUES (1,'House on the rock','Google','Rivers','2011-09-19 22:24:24',2),(2,'House on the rock','Google','Rivers','2011-09-19 22:24:24',2),(3,'House on the rock','Google','Rivers','2011-09-19 22:24:24',2),(4,'House on the rock','Google','Rivers','2011-09-19 22:24:24',2),(5,'House on the rock','Google','Rivers','2011-09-19 22:24:24',2),(6,'House on the rock','Google','Rivers','2011-09-19 22:24:24',2),(7,'House on the rock','Google','Rivers','2011-09-19 22:24:24',2),(8,'House on the rock','Google','Rivers','2011-09-19 22:24:24',2),(9,'House on the rock','Google','Rivers','2011-09-19 22:24:24',2),(10,'House on the rock','Google','Rivers','2011-09-19 22:24:24',2),(11,'House on the rock','Google','Rivers','2011-09-19 22:24:24',2),(12,'House on the rock','Google','Rivers','2011-09-19 22:24:24',1),(13,'House on the rock','Google','Rivers','2011-09-19 22:24:24',1);
/*!40000 ALTER TABLE `branches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `user_id` tinyint(4) NOT NULL,
  `review_id` tinyint(4) NOT NULL,
  `message` varchar(500) NOT NULL,
  PRIMARY KEY (`id`),
  FULLTEXT KEY `message` (`message`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (1,'2011-09-25 20:11:47','2011-09-19 22:24:24',1,1,'This is my home'),(2,'2011-09-19 22:24:24','2011-09-19 22:24:24',1,1,'branches that would lead use to the ciyrt'),(3,'2011-09-19 22:24:24','2011-09-19 22:24:24',1,1,'branches that would lead use to the ciyrt'),(4,'2011-09-19 22:24:24','2011-09-19 22:24:24',1,1,' that would lead use to the ciyrt');
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `companies`
--

DROP TABLE IF EXISTS `companies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `companies` (
  `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `sector_id` tinyint(4) NOT NULL,
  `name` char(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companies`
--

LOCK TABLES `companies` WRITE;
/*!40000 ALTER TABLE `companies` DISABLE KEYS */;
INSERT INTO `companies` VALUES (1,'2011-09-19 22:24:24',1,'bank'),(2,'2011-09-19 22:24:24',1,'bank'),(3,'2011-09-19 22:24:24',2,'bank'),(4,'2011-09-19 22:24:24',2,'bank');
/*!40000 ALTER TABLE `companies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reviews` (
  `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
  `entry` text NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` tinyint(3) unsigned NOT NULL,
  `branch_id` tinyint(3) unsigned NOT NULL,
  `title` char(255) DEFAULT NULL,
  `url` char(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  FULLTEXT KEY `title` (`title`,`entry`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (1,'branches that would lead use to the city','2011-09-19 22:24:24',1,1,'oogletivers','oogletivers'),(2,'Another journey into space which I am into','2011-11-05 05:55:22',1,1,'The real thing','the_real_thing'),(3,'Another journey into space which I am into','2011-11-05 05:55:59',1,1,'The real thing','the_real_thing'),(4,'Another journey into space which I am into','2011-11-05 06:03:05',1,1,'The real thing','the_real_thing'),(5,'None is like yours','2011-11-10 05:20:16',1,4,'This house is mine','Doodlefoo'),(6,'None is like yours','2011-11-10 05:21:36',1,4,'This house is mine','Doodlefoo'),(7,'None is like yours','2011-11-10 05:24:02',1,4,'This house is mine','Doodlefoo'),(8,'None is like yours','2011-11-10 05:24:40',1,4,'This house is mine','Doodlefoo'),(9,'None is like yours','2011-11-10 05:25:51',1,4,'This house is mine','Doodlefoo'),(10,'None is like yours','2011-11-10 05:27:58',1,4,'This house is mine','Doodlefoo'),(11,'None is like yours','2011-11-10 05:29:31',1,4,'This house is mine','Doodlefoo'),(12,'None is like yours','2011-11-10 05:30:48',1,4,'This house is mine','Doodlefoo'),(13,'None is like yours','2011-11-10 05:36:17',1,4,'This house is mine','Doodlefoo');
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sectors`
--

DROP TABLE IF EXISTS `sectors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sectors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `name` char(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sectors`
--

LOCK TABLES `sectors` WRITE;
/*!40000 ALTER TABLE `sectors` DISABLE KEYS */;
INSERT INTO `sectors` VALUES (1,'2011-09-19 22:24:24','bank'),(2,'2011-09-19 22:24:24','bank'),(3,'2011-09-19 22:24:24','bank');
/*!40000 ALTER TABLE `sectors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
  `username` char(40) NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `flag` int(2) unsigned NOT NULL DEFAULT '0',
  `email` varchar(100) NOT NULL,
  `salt` varchar(9) NOT NULL,
  `activation_code` varchar(80) NOT NULL,
  `password` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'kobdaabbxys','2011-11-10 04:24:59','2011-11-10 04:24:59',0,'haacvvccop@cmail.com','ZeA<D^K=',' kÍÉ‰p± ÑÈÙ;@Ç“^s-os3Hˆpîv','9ˆu8¿ÊõhÏlû­žUÎÙÚ–âg0bƒŠLšme\r'),(2,'kobdaabbxygssgs','2011-11-05 03:20:51','2011-11-05 03:20:51',0,'havvvassscvvccop@cmail.com','Ich0ZLq','r½	„3—™	LÑƒ$žôD½·9²‘•g<µý nsœ','QN]<˜Hs›Åa—™@ƒ¨mÐÊ(4~EŽ=!y'),(8,'jdklhkda','2011-11-10 22:53:37','2011-11-10 22:53:37',0,'emekamicro@gmail.com','N?A_g^H<','ÁûâšË‚`Lêí\nçå88?Ÿ±~xaC/*L','õ\ZßTäÇÇ1ÇUù)Þ—é„mò!/(öc;Ÿ');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `votes`
--

DROP TABLE IF EXISTS `votes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `votes` (
  `ID1` int(9) unsigned NOT NULL,
  `ID2` int(9) unsigned NOT NULL,
  `review_id` int(9) unsigned NOT NULL,
  `counted_votes` int(9) unsigned NOT NULL DEFAULT '1',
  PRIMARY KEY (`ID2`,`review_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `votes`
--

LOCK TABLES `votes` WRITE;
/*!40000 ALTER TABLE `votes` DISABLE KEYS */;
/*!40000 ALTER TABLE `votes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-11-11  1:57:50
