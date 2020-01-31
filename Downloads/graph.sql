-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jan 28, 2020 at 03:22 PM
-- Server version: 10.3.17-MariaDB-0+deb10u1
-- PHP Version: 7.3.11-1~deb10u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sensor`
--

-- --------------------------------------------------------

--
-- Table structure for table `graph`
--

CREATE TABLE `graph` (
  `pm25` float NOT NULL,
  `pm10` float NOT NULL,
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `graph`
--

INSERT INTO `graph` (`pm25`, `pm10`, `updated_at`) VALUES
(10, 66, '2020-01-25 20:35:00'),
(34, 88, '2020-01-25 23:35:05'),
(20.2, 27, '2020-01-26 06:30:02'),
(20.4, 25.2, '2020-01-26 07:30:02'),
(20.1, 33.8, '2020-01-26 09:30:02'),
(20.9, 32.1, '2020-01-26 10:30:02'),
(28.3, 37, '2020-01-26 15:30:03'),
(21.9, 28.2, '2020-01-26 16:30:02'),
(19.7, 25, '2020-01-26 17:30:03'),
(16.1, 23.8, '2020-01-27 07:30:03'),
(19.1, 24.6, '2020-01-27 08:30:02'),
(26.2, 35.1, '2020-01-27 10:30:03'),
(23.6, 39.9, '2020-01-28 07:30:03'),
(2611.3, 5009.1, '2020-01-28 08:30:03'),
(17, 29.7, '2020-01-28 09:30:02');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `graph`
--
ALTER TABLE `graph`
  ADD PRIMARY KEY (`updated_at`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
