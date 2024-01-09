-- phpMyAdmin SQL Dump
-- version 4.1.6
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Aug 09, 2023 at 05:35 PM
-- Server version: 5.6.16
-- PHP Version: 5.5.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `crops`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=49 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add crop_table', 7, 'add_crop_table'),
(26, 'Can change crop_table', 7, 'change_crop_table'),
(27, 'Can delete crop_table', 7, 'delete_crop_table'),
(28, 'Can view crop_table', 7, 'view_crop_table'),
(29, 'Can add ftlzr_table', 8, 'add_ftlzr_table'),
(30, 'Can change ftlzr_table', 8, 'change_ftlzr_table'),
(31, 'Can delete ftlzr_table', 8, 'delete_ftlzr_table'),
(32, 'Can view ftlzr_table', 8, 'view_ftlzr_table'),
(33, 'Can add plant_disease', 9, 'add_plant_disease'),
(34, 'Can change plant_disease', 9, 'change_plant_disease'),
(35, 'Can delete plant_disease', 9, 'delete_plant_disease'),
(36, 'Can view plant_disease', 9, 'view_plant_disease'),
(37, 'Can add product', 10, 'add_product'),
(38, 'Can change product', 10, 'change_product'),
(39, 'Can delete product', 10, 'delete_product'),
(40, 'Can view product', 10, 'view_product'),
(41, 'Can add purchase', 11, 'add_purchase'),
(42, 'Can change purchase', 11, 'change_purchase'),
(43, 'Can delete purchase', 11, 'delete_purchase'),
(44, 'Can view purchase', 11, 'view_purchase'),
(45, 'Can add reg_user', 12, 'add_reg_user'),
(46, 'Can change reg_user', 12, 'change_reg_user'),
(47, 'Can delete reg_user', 12, 'delete_reg_user'),
(48, 'Can view reg_user', 12, 'view_reg_user');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `crop_prediction_crop_table`
--

CREATE TABLE IF NOT EXISTS `crop_prediction_crop_table` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `u_id` varchar(150) NOT NULL,
  `N` varchar(200) NOT NULL,
  `P` varchar(150) NOT NULL,
  `K` varchar(150) NOT NULL,
  `temperature` varchar(150) NOT NULL,
  `humidity` varchar(150) NOT NULL,
  `ph` varchar(150) NOT NULL,
  `rainfall` varchar(150) NOT NULL,
  `result` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `crop_prediction_ftlzr_table`
--

CREATE TABLE IF NOT EXISTS `crop_prediction_ftlzr_table` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `u_id` varchar(150) NOT NULL,
  `N` varchar(200) NOT NULL,
  `P` varchar(150) NOT NULL,
  `K` varchar(150) NOT NULL,
  `crop_type` varchar(150) NOT NULL,
  `result` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `crop_prediction_plant_disease`
--

CREATE TABLE IF NOT EXISTS `crop_prediction_plant_disease` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `u_id` varchar(150) NOT NULL,
  `file` varchar(200) NOT NULL,
  `label` varchar(250) NOT NULL,
  `remedies` varchar(1000) NOT NULL,
  `pesticides` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `crop_prediction_product`
--

CREATE TABLE IF NOT EXISTS `crop_prediction_product` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(100) NOT NULL,
  `crop_type` varchar(100) NOT NULL,
  `price` varchar(100) NOT NULL,
  `quantity` varchar(100) NOT NULL,
  `image` varchar(500) NOT NULL,
  `product_type` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=30 ;

--
-- Dumping data for table `crop_prediction_product`
--

INSERT INTO `crop_prediction_product` (`id`, `product_name`, `crop_type`, `price`, `quantity`, `image`, `product_type`) VALUES
(1, 'urea', 'rice', '60', '29', 'urea.jpg', 'fertilizer'),
(2, 'superphosphate', 'maize', '25', '50', 'Super-Phosphate.jpg', 'fertilizer'),
(3, 'nitrogen', 'chickpea', '30', '50', 'nitrogreen_600x600.jpg', 'fertilizer'),
(4, '10-10-10', 'kidneybeans', '55', '40', '10-10-10.jpg', 'fertilizer'),
(7, '20-40-20', 'blackgram', '155', '50', '20_40_20.jpg', 'fertilizer'),
(8, 'Rhizobium', 'lentil', '100', '50', 'RHIZOBIUM.jpeg', 'fertilizer'),
(9, '8-8-8', 'pomegranate', '45', '50', '8-8-8.jpeg', 'fertilizer'),
(10, '5-10-10', 'banana', '143', '50', '5-10-10.jpeg', 'fertilizer'),
(11, '10-20-20', 'mango', '60', '50', '10-20-20.jpg', 'fertilizer'),
(12, 'Hydrated Lime', 'grapes', '72', '50', 'hydratedLime_.jpg', 'fertilizer'),
(13, '5-5-5', 'watermelon', '30', '50', '5-5-5.jpg', 'fertilizer'),
(14, '19-19-19', 'muskmelon', '245', '48', '19-19-19.jpg', 'fertilizer'),
(15, 'FYM', 'apple', '100', '50', 'fymm.jpeg', 'fertilizer'),
(16, 'P2O5', 'orange', '155', '50', 'p205.jpg', 'fertilizer'),
(17, '14-14-14', 'papaya,pigeonpeas', '55', '50', '14_14_14.jpeg', 'fertilizer'),
(18, 'ERP', 'coconut', '48', '50', 'ERP.jpeg', 'fertilizer'),
(19, '20-10-10', 'cotton', '22', '50', '20-10-10-fertilizer.jpg', 'fertilizer'),
(20, '40-20-20', 'jute', '34', '50', '40-20-20.jpg', 'fertilizer'),
(21, 'lime', 'coffee', '155', '50', 'lime.jpg', 'fertilizer'),
(22, 'CHLOROTHALONIL', 'Potato early blight', '360', '50', 'CHLOROTHALONIL.jpg', 'pesticide'),
(23, 'METALAXYL', 'Potato late blight', '480', '50', 'METALAXYL.jpeg', 'pesticide'),
(24, 'STREPTOMYCIN SULPHATE', 'Rice bacterial leaf blight', '54', '50', 'STREPTOMYCIN SULPHATE.jpg', 'pesticide'),
(25, 'GRISEPFULVIN', 'Rice brown spot', '220', '50', 'GRISEPFULVIN.jpeg', 'pesticide'),
(26, 'COPPER OXYCHLORIDE', 'Rice leaf smut', '500', '50', 'COPPER HYDROXIDE.jpg', 'pesticide'),
(27, 'AZOXYSTROBIN', 'Tomato bacterial spot', '360', '50', 'AZOXYSTROBIN.jpg', 'pesticide'),
(28, 'COPPER HYDROXIDE', 'Tomato early blight', '1170 Rs', '1 Kg', 'COPPER OXYCHLORIDE.jpg', 'pesticide'),
(29, 'PROPINEB', 'Tomato late blight', '393 Rs', '1 Kg', 'PROPINEB.jpeg', 'pesticide');

-- --------------------------------------------------------

--
-- Table structure for table `crop_prediction_purchase`
--

CREATE TABLE IF NOT EXISTS `crop_prediction_purchase` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `pr_id` varchar(100) NOT NULL,
  `product_name` varchar(100) NOT NULL,
  `rate` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `cardtype` varchar(100) NOT NULL,
  `cardname` varchar(100) NOT NULL,
  `cardnumber` varchar(100) NOT NULL,
  `cvv` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `uid` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `quantity` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `crop_prediction_purchase`
--

INSERT INTO `crop_prediction_purchase` (`id`, `pr_id`, `product_name`, `rate`, `date`, `cardtype`, `cardname`, `cardnumber`, `cvv`, `phone`, `uid`, `status`, `quantity`, `name`) VALUES
(1, '1', 'urea', '120.00', '2023-08-07', 'credit', 'Akhil', '1234567890123456', '123', '7736417404', '1', 'delivered', '2', 'Akhil Vinayak P'),
(2, '1', 'urea', '60.00', '2023-08-09', 'credit', 'ghhjas', '7410852963852741', '123', '7736417404', '1', 'delivered', '1', 'Akhil Vinayak P');

-- --------------------------------------------------------

--
-- Table structure for table `crop_prediction_reg_user`
--

CREATE TABLE IF NOT EXISTS `crop_prediction_reg_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `email` varchar(200) NOT NULL,
  `phone` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  `address` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `crop_prediction_reg_user`
--

INSERT INTO `crop_prediction_reg_user` (`id`, `name`, `email`, `phone`, `password`, `address`) VALUES
(1, 'Akhil Vinayak P', 'vinayakakhil030@gmail.com', '7736417404', 'Akhil@97', 'Naduvilaveedu Neerkunnam Vandanam P O');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'crop_prediction', 'crop_table'),
(8, 'crop_prediction', 'ftlzr_table'),
(9, 'crop_prediction', 'plant_disease'),
(10, 'crop_prediction', 'product'),
(11, 'crop_prediction', 'purchase'),
(12, 'crop_prediction', 'reg_user'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=25 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-07-13 15:39:10.143733'),
(2, 'auth', '0001_initial', '2023-07-13 15:39:11.762680'),
(3, 'admin', '0001_initial', '2023-07-13 15:39:12.072070'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-07-13 15:39:12.074808'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-07-13 15:39:12.089924'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-07-13 15:39:12.242579'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-07-13 15:39:12.312186'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-07-13 15:39:12.381218'),
(9, 'auth', '0004_alter_user_username_opts', '2023-07-13 15:39:12.388733'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-07-13 15:39:12.452465'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-07-13 15:39:12.452465'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-07-13 15:39:12.463512'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-07-13 15:39:12.531752'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-07-13 15:39:12.611315'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-07-13 15:39:12.721402'),
(16, 'auth', '0011_update_proxy_permissions', '2023-07-13 15:39:12.735599'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-07-13 15:39:12.805090'),
(18, 'crop_prediction', '0001_initial', '2023-07-13 15:39:13.101057'),
(19, 'sessions', '0001_initial', '2023-07-13 15:39:13.306623'),
(20, 'crop_prediction', '0002_plant_disease_pesticides', '2023-07-14 05:43:59.049624'),
(21, 'crop_prediction', '0003_product_product_type', '2023-07-14 06:19:01.873265'),
(22, 'crop_prediction', '0004_purchase_status', '2023-08-02 08:37:59.567722'),
(23, 'crop_prediction', '0005_auto_20230803_1252', '2023-08-03 07:24:33.098594'),
(24, 'crop_prediction', '0006_purchase_name', '2023-08-09 10:30:42.969612');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('frsv0s25wdtbt4m1g722wdfa9hsaygqm', 'eyJhZG1pbiI6ImFkbWluIn0:1qTgi0:gVGyLmvNle6Z_2lw6WXwTkCfix-vb_zSwBfwlFIbuSw', '2023-08-23 10:46:32.868002'),
('ma224fcuzugnpqbvp3q15jw2fa8umpp4', 'e30:1qRTdp:_pb9kqlDZnAOvFdZ6u5e7ISEa7f-xhCWwykJXRHUb2M', '2023-08-17 08:25:05.068471'),
('owqqe1tlrd2mwjm6dh9n2smr4aa9orha', 'e30:1qKI4i:PrVBtRkzBY_ty96N13D9NgPRkvlaG9vwV475cgXuXeQ', '2023-07-28 12:39:08.548240');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
