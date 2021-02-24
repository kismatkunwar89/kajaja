-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 04, 2020 at 10:29 AM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.2.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `payment`
--

-- --------------------------------------------------------

--
-- Table structure for table `payouts`
--

CREATE TABLE `payouts` (
  `Idno` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `contact` varchar(150) NOT NULL,
  `department` varchar(100) NOT NULL,
  `payment` varchar(150) NOT NULL,
  `amount` varchar(150) NOT NULL,
  `overtime` varchar(100) NOT NULL,
  `total` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `payouts`
--

INSERT INTO `payouts` (`Idno`, `name`, `contact`, `department`, `payment`, `amount`, `overtime`, `total`) VALUES
(1, 'Shashwat Dhakal', '9841868088', 'Information Technology', 'Cash', '9999999', '50%', 14999999),
(2, 'Raman Dahal', '123456789', 'Information Technology', 'E-Sewa', '15000', '10%', 16500);

-- --------------------------------------------------------

--
-- Table structure for table `workers`
--

CREATE TABLE `workers` (
  `Idno` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(150) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `contact` varchar(150) NOT NULL,
  `dob` varchar(150) NOT NULL,
  `address` varchar(200) NOT NULL,
  `department` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `payment` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `workers`
--

INSERT INTO `workers` (`Idno`, `name`, `email`, `gender`, `contact`, `dob`, `address`, `department`, `status`, `payment`) VALUES
(1, 'Shashwat Dhakal', 'findshashwat11@gmail.com', 'Male', '9841868088', '12/12/2000', 'Balkot, Bhaktapur\n', 'Information Technology', 'Present', 'Cash'),
(2, 'Raman Dahal', 'rddahal8@gmail.com', 'Male', '123456789', '01/01/2001', 'Tikathali\n', 'Information Technology', 'Present', 'E-Sewa'),
(3, 'Abhishek Bhattarai', 'ab@gmail.com', 'Male', '987654321', '01/01/2000', 'Earth\n', 'Information Technology', 'Free', 'Bank'),
(4, 'Abhishek Lama', 'al@gmail.com', 'Male', '456789123', '02/03/2000', 'gg\n', 'Information Technology', 'Busy', 'Cheque'),
(5, 'Bipin Adhikari', 'ba@gmail.com', 'Male', '789123456', '05/05/2001', 'ez\n', 'Information Technology', 'Busy', 'Master Card');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `payouts`
--
ALTER TABLE `payouts`
  ADD PRIMARY KEY (`Idno`);

--
-- Indexes for table `workers`
--
ALTER TABLE `workers`
  ADD PRIMARY KEY (`Idno`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
