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
-- Table structure for table `content_book`
--

CREATE TABLE IF NOT EXISTS `content_book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `section` varchar(50) NOT NULL,
  `authors` varchar(150) NOT NULL,
  `subject` varchar(50) NOT NULL,
  `publisher` varchar(50) NOT NULL,
  `publication_date` date DEFAULT NULL,
  `price` decimal(8,2) NOT NULL,
  `description` longtext NOT NULL,
  `rating` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `content_book`
--

INSERT INTO `content_book` (`id`, `title`, `section`, `authors`, `subject`, `publisher`, `publication_date`, `price`, `description`, `rating`) VALUES
(1, 'modern operating systems', 'computer science', 'andrew s. tanenbaum', 'operating systems', 'prentice-hall india', '2005-05-01', '545.00', 'The widely anticipated revision of this worldwide best-seller incorporates the latest developments in operating systems technologies.  The Third Edition includes up-to-date materials on relevant operating systems such as Linux, Windows, and embedded real-time and multimedia systems. Includes new and updated coverage of multimedia operating systems, multiprocessors, virtual machines, and antivirus software. Covers internal workings of Windows Vista (Ch. 11); unique even for current publications. Provides information on current research based Tanenbaum’s experiences as an operating systems researcher. A useful reference for programmers.', 0),
(2, 'computer networks', 'computer science', 'andrew s.tanenbaum', 'computer networks', 'pearson education asia', '2008-06-02', '425.00', 'Computer Networks, Fourth Edition is the ideal introduction to computer networks. Renowned author, educator, and researcher Andrew S. Tanenbaum has updated his classic best seller to reflect the newest technologies, including 802.11, broadband wireless, ADSL, Bluetooth, gigabit Ethernet, the Web, the wireless Web, streaming audio, IPsec, AES, quantum cryptography, and more. Using real-world examples, Tanenbaum explains how networks work on the inside, from underlying physical layer hardware up through today''s most popular network applications.', 1),
(3, 'an introduction to compute', 'computer science', 'kenneth c.mansfield', 'computer networks', 'prentice-hall india', '2000-09-09', '324.00', 'For freshman-level courses in Technology, Computer Science, Computer Technology, Engineering, CIS, and Business. This text provides a detailed, yet straightforward approach to computer networking-with an emphasis on real-world network environments such as Windows. It features a strong pedagogy that enables students to apply numerous concepts to real-world computer situations.', 3),
(4, 'data and computer communication', 'computer science', 'william stallings', 'data communication', 'pearson education india', '2000-05-05', '450.00', 'Data and Computer Communications, 9e, is a two-time winner of the best Computer Science and Engineering textbook of the year award from the Textbook and Academic Authors Association. It is ideal for one/two-semester courses in Computer Networks, Data Communications, and Communications Networks in CS, CIS, and Electrical Engineering departments.\r\n\r\n ', 1),
(5, 'cryptography and network security: principles and practice', 'computer science', 'william stallings', 'security in computing', 'prentice-hall india', '2005-05-01', '510.00', 'William Stallings'' Cryptography and Network Security: Principles and Practice, 5e is a practical survey of cryptography and network security with unmatched support for instructors and students.', 2),
(6, 'computer graphics priciples and practice', 'computer science', 'james d.foley', 'computer graphics', 'addison wesley', '2002-03-01', '280.00', 'The long-awaited second edition of this book has been completely rewritten to provide the most comprehensive authoritative and up-to-date coverage of the field---making it the standard computer graphics reference work for the 1990s. The authors provide a unique combination of current concepts and practical applications. The important algorithms in 2D and 3D graphics are detailed for easy implementation.', 3),
(7, 'java 2 complete reference', 'computer science', 'herbert schidt', 'java,computer graphics', 'tata mcgraw hill', '1999-02-02', '245.00', 'This book is the most complete and up-to-date resource on Java from programming guru, Herb Schildt -- a must-have desk reference for every Java programmer.', 4),
(8, 'the java programming language', 'computer science', 'arnold,gosling,holmes', 'java', 'pearson education asia', '2005-04-01', '350.00', 'Direct from the creators of the Java™ programming language, the completely revised fourth edition of The Java™ Programming Language is an indispensable resource for novice and advanced programmers alike. ', 4),
(9, 'data structures algorithms and applications', 'computer science', 'sartaj sahni', 'data structures', 'tata mcgraw hill', '2004-08-31', '600.00', 'This text provides students with an introduction to data structures and algorithms. It emphasizes algorithm analysis and the development of efficient code, and includes important background material. Divided into three parts, the text features Data Structure Application sections at the end of each chapter in part two, Algorithm Application sections in each design method chapter in part three, and a gradual development of C++ features not found in C to help students with either a background in C or C++ to comprehend topics in the book.', 5),
(10, 'introduction to algorithm', 'computer science', 'thomas coreman,charles,ronald rivest', 'data structures', 'the mit press', '2009-09-30', '700.00', 'Some books on algorithms are rigorous but incomplete; others cover masses of material but lack rigor. Introduction to Algorithms uniquely combines rigor and comprehensiveness. The book covers a broad range of algorithms in depth, yet makes their design and analysis accessible to all levels of readers. Each chapter is relatively self-contained and can be used as a unit of study. The algorithms are described in English and in a pseudocode designed to be readable by anyone who has done a little programming. The explanations have been kept elementary without sacrificing depth of coverage or mathematical rigor.', 4);
