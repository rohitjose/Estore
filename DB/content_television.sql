-- phpMyAdmin SQL Dump
-- version 3.3.7deb5build0.10.10.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 29, 2011 at 07:32 PM
-- Server version: 5.1.49
-- PHP Version: 5.3.3-1ubuntu9.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `estore`
--

-- --------------------------------------------------------

--
-- Table structure for table `content_television`
--

CREATE TABLE IF NOT EXISTS `content_television` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `tv_type` varchar(50) NOT NULL,
  `company` varchar(150) NOT NULL,
  `size` varchar(150) NOT NULL,
  `resolution` varchar(150) NOT NULL,
  `power` varchar(150) NOT NULL,
  `price` decimal(8,2) NOT NULL,
  `launch_date` date DEFAULT NULL,
  `description` longtext NOT NULL,
  `rating` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `content_television`
--

INSERT INTO `content_television` (`id`, `title`, `tv_type`, `company`, `size`, `resolution`, `power`, `price`, `launch_date`, `description`, `rating`) VALUES
(1, '1080p', 'lcd', 'bush', '22in', '1920*1080', '48', '9020.00', '2010-12-01', 'This Bush 22 inch Full HD 1080p widescreen television is an LED TV which provides stunning pictures with colour and pin sharp detail.\r\n* LED backlighting technology.\r\n* Energy saving.', 3),
(2, 'ps42c450', 'plasma', 'samsung', '42in', '1024*728', '48', '9999.99', '2010-11-09', '* Digitally interactive.\r\n* Digital text.\r\n* Digital audio broadcasting (DAB).\r\n* Digital video broadcasting (DVB) subtitles available.', 3),
(3, 'ps50c6900', 'plasma', 'samsung', '50in', '1920*1080', '48', '50000.00', '2011-01-01', 'Sky 3D HDTV Ready\r\n* Wi-Fi Ready (Dongle Required)\r\n* Internet@TV / Samsung Apps Support\r\n* 4 HDMI (v1.4) Inputs', 3),
(4, 'lcd42f1080', 'lcd', 'wharfedale', '42in', '1920*1080', '48', '25000.00', '2010-09-01', 'Digitally interactive.\r\nDigital text.\r\nDigital Video Broadcasting (DVB) subtitles available.\r\nAuto setup.\r\nAuto scan for new channels. ', 2),
(5, 'ps3122', 'lcd', 'wharfedale', '22in', '1680*1050', '48', '12000.00', '2009-06-01', 'Digital text.\r\n\r\n* Digital Video broadcasting (DVB) subtitles available.\r\n\r\n* Auto setup.', 2),
(6, 'kdl-19bx200bu', 'lcd', 'sony', '19in', '1366*768', '110', '22000.00', '2010-09-09', 'HD Ready 720p picture quality.\r\nEasy connectivity with HDMI and USB ports.\r\nIdeal for the kitchen or bedroom.\r\nTelevision picture quality:', 4),
(7, '32av615d', 'lcd', 'toshiba', '32in', '1366*768', '48', '18000.00', '2010-01-01', '* Powerful in-built speakers\r\n* Contemporary black gloss finish, with narrow bezels\r\n', 4),
(8, 'tx-l3210', 'lcd', 'panasonic', '32in', '1366*768', '48', '14000.00', '2010-02-01', 'Suitable for wall mounting (brackets not included).\r\n\r\n* Standby power consumption 0.4 watts.\r\n', 3),
(9, '321d1380', 'lcd', 'hitachi', '32in', '1366*768', '48', '24000.00', '2009-08-01', '* Auto search tuner.\r\n\r\n* Auto search sorting.\r\n\r\n* Auto search labelling.\r\n', 1.5),
(10, '32kv500', 'lcd', 'toshiba', '32in', '1680*1050', '110', '23000.00', '2010-03-01', 'With an attractive glossy black design and a range of useful features, the Toshiba 32KV500B is the perfect HD-Ready addition to your living room.', 3);
