-- phpMyAdmin SQL Dump
-- version 3.3.7deb5build0.10.10.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 29, 2011 at 07:31 PM
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
-- Table structure for table `content_camera`
--

CREATE TABLE IF NOT EXISTS `content_camera` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `company` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  `optical_zoom` varchar(100) NOT NULL,
  `battery` varchar(100) NOT NULL,
  `digital_camera_type` varchar(100) NOT NULL,
  `price` decimal(8,2) NOT NULL,
  `memory_card_format` varchar(100) NOT NULL,
  `display_size` varchar(100) NOT NULL,
  `accessories` longtext NOT NULL,
  `launch_date` date DEFAULT NULL,
  `description` longtext NOT NULL,
  `rating` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `content_camera`
--

INSERT INTO `content_camera` (`id`, `title`, `company`, `model`, `optical_zoom`, `battery`, `digital_camera_type`, `price`, `memory_card_format`, `display_size`, `accessories`, `launch_date`, `description`, `rating`) VALUES
(1, '14.2mp camera', 'Nikon', 'D3100', '3x 18-55mm Zoom', 'EN-EL14 Rechargeable Li-ion Battery', 'Digital SLR Camera', '15000.00', 'SD/SDHC/SDXC memory cards', '3in', '4.2-megapixel DX-format CMOS image sensor; 3-inch monitor with One-Touch Live View shooting and movie capture\r\nIncludes 3x 18-55mm Zoom-NIKKOR VR Image Stabilization lens\r\nFull 1080p HD Cinematic Video with full-time autofocus and sound\r\nEasy-To-Use Nikon Guide Mode with intuitive controls and on-board assistance\r\nCapture images to SD/SDHC/SDXC memory cards (not included)', '2011-01-01', 'ikon has unveiled the D3100, its latest entry-level offering and its first DSLR that can record full 1080p HD videos. Successor to the popular D3000, it is built around a 14.2 CMOS sensor and a 3 inch LCD. As well as movies it gains Live View shooting, a wider ISO range ( 100-3200 expandable to 12800) and a host of small revisions. We''ve been given access to a pre-production version of the camera which we''ve used to prepare a hands-on preview, looking at the changes Nikon has made to its best-selling DSLR. ', 2),
(2, '16.2mp camera', 'Nikon', 'Nikon D7000', '1.5x', 'EN-EL15', 'CMOS Digital SLR', '10000.00', 'Twin SD card slots', '3in', 'High Resolution 16.2 MP DX-format CMOS sensor\r\nBody only; lenses sold separately\r\nHigh Speed 6 frames per second continuous shooting up to 100 shots\r\nBreathtaking Full 1080p HD Movies with Full Time Autofocus\r\ndynamic ISO range from 100 to 6400\r\n', '2010-04-06', 'Nikon has released the D7000 mid-level digital SLR. Housed in a magnesium alloy body, the feature-rich camera incorporates a 16.2Mp CMOS sensor, faster ''Expeed 2''-branded processor, 921k dot 3.0" LCD and can record 1080p full HD movies. It features the company''s latest 39-point AF system with 3D tracking and 2,016 pixel RGB metering sensor. It will start shipping with the 18-105mm VR kit lens from October 2010 at a retail price of $1499.95. We''ve had a pre-production D7000 in the office for long enough for us to prepare an full hands-on preview looking at the camera, its features and where it''ll sit in the range. ', 2),
(3, '10.2mp camera', 'sony', 'Cyber-shot DSC-HX5V', '10x', 'Lithium-ion battery', 'CMOS Digital Camera', '11000.00', '45MB internal Flash Memory', '3in', '"Exmor R" CMOS sensor for stunning low-light performance\r\niSweep Panorama Mode captures stunning panoramic images\r\nFast capture with 10fps at full 10.2-megapixel resolution\r\n10x optical zoom Sony G-Lens with 25mm wide angle; 1080i AVCHD Movie records high-quality HD movies\r\nRecording Media : 45MB internal Flash Memory, optional Memory Stick Duo Media, optional Memory Stick PRO Duo Media, optional Memory Stick PRO Duo (High Speed), optional Memory Stick PRO HG-Duo, optional SD/SDHC media\r\n', '2009-07-15', 'Capture stunning low-light images and sweeping panoramic views with the DSC-HX5V featuring an "Exmor R" CMOS Sensor. Plus catch fast action shots with up to 10 frames per seconds shooting. Full HD Movie Mode records amazingly detailed video and a 25mm equivalent wide angle 10x high-zoom G Lens allows you to take captivating images.\r\n', 2),
(4, '12.2mp camera', 'sony', 'TX Series DSC-TX9/H', '4x', 'Lithium-ion battery', 'Digital Still Camera', '16000.00', 'SD/SDHC/SDXC', '3.5in', 'Supplied Accessories - Rechargeable Battery (NP-BN1), Battery Charger, A/V Cable, wrist Strap, Paint Pen, CD-ROM, Multi Output StandFeatures\r\n12.2MP Exmor R CMOS sensor for stunning low-light performance\r\n3.5 Touch screen for easy focus selection and photo viewing\r\nCarl Zeiss Vario-Tessar 4x (25mm) optical zoom lens\r\n1080i AVCHD Movie records high-quality HD movies\r\n', '2009-09-01', 'Photographic brilliance meets pure, elegant style in the Cyber-shot DSC-TX9 digital camera. Capture impressive landscapes with iSweep Panorama and enjoy 3D shots as well. Sony''s "Exmor R" CMOS sensor delivers impressive clarity and crisp detail in low light, and the Superior Auto mode takes the guesswork out of choosing the right settings. There''s also an innovative Background Defocus feature and Full HD 1080/60i AVCHD movie recording that looks great on your compatible HDTV. Enjoy it all on an easy to view 3.5-inch (diagonal) touch screen.\r\n', 3);
