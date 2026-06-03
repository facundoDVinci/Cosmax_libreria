-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 03, 2026 at 06:28 PM
-- Server version: 8.4.3
-- PHP Version: 8.3.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cosmax_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 3, 'add_permission'),
(6, 'Can change permission', 3, 'change_permission'),
(7, 'Can delete permission', 3, 'delete_permission'),
(8, 'Can view permission', 3, 'view_permission'),
(9, 'Can add group', 2, 'add_group'),
(10, 'Can change group', 2, 'change_group'),
(11, 'Can delete group', 2, 'delete_group'),
(12, 'Can view group', 2, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add cliente', 6, 'add_cliente'),
(22, 'Can change cliente', 6, 'change_cliente'),
(23, 'Can delete cliente', 6, 'delete_cliente'),
(24, 'Can view cliente', 6, 'view_cliente'),
(25, 'Can add libro', 8, 'add_libro'),
(26, 'Can change libro', 8, 'change_libro'),
(27, 'Can delete libro', 8, 'delete_libro'),
(28, 'Can view libro', 8, 'view_libro'),
(29, 'Can add user', 9, 'add_usuario'),
(30, 'Can change user', 9, 'change_usuario'),
(31, 'Can delete user', 9, 'delete_usuario'),
(32, 'Can view user', 9, 'view_usuario'),
(33, 'Can add venta', 10, 'add_venta'),
(34, 'Can change venta', 10, 'change_venta'),
(35, 'Can delete venta', 10, 'delete_venta'),
(36, 'Can view venta', 10, 'view_venta'),
(37, 'Can add detalle venta', 7, 'add_detalleventa'),
(38, 'Can change detalle venta', 7, 'change_detalleventa'),
(39, 'Can delete detalle venta', 7, 'delete_detalleventa'),
(40, 'Can view detalle venta', 7, 'view_detalleventa');

-- --------------------------------------------------------

--
-- Table structure for table `cosmax_cliente`
--

CREATE TABLE `cosmax_cliente` (
  `id` bigint NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `telefono` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `cosmax_cliente`
--

INSERT INTO `cosmax_cliente` (`id`, `nombre`, `apellido`, `email`, `telefono`) VALUES
(1, 'Cliente', 'Apellido', 'Cliente@gmail.com', '23435645');

-- --------------------------------------------------------

--
-- Table structure for table `cosmax_detalleventa`
--

CREATE TABLE `cosmax_detalleventa` (
  `id` bigint NOT NULL,
  `cantidad` int UNSIGNED NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `libro_id` bigint NOT NULL,
  `venta_id` bigint NOT NULL
) ;

-- --------------------------------------------------------

--
-- Table structure for table `cosmax_libro`
--

CREATE TABLE `cosmax_libro` (
  `id` bigint NOT NULL,
  `titulo` varchar(200) NOT NULL,
  `autor` varchar(100) NOT NULL,
  `precio` decimal(5,2) NOT NULL,
  `stock` int UNSIGNED NOT NULL
) ;

-- --------------------------------------------------------

--
-- Table structure for table `cosmax_usuario`
--

CREATE TABLE `cosmax_usuario` (
  `id` bigint NOT NULL,
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
  `rol` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `cosmax_usuario`
--

INSERT INTO `cosmax_usuario` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `rol`) VALUES
(1, 'pbkdf2_sha256$1200000$AKvCEOGDkjzaYnkpwGlz1X$VYutCcQIouK9XDJg/EEXYKkGCLlfb+4FGkG6j1DVBOI=', '2026-06-03 17:22:39.372251', 1, 'leonardo', '', '', 'leo@gmail.com', 1, 1, '2026-06-03 17:22:18.266661', 'empleado');

-- --------------------------------------------------------

--
-- Table structure for table `cosmax_usuario_groups`
--

CREATE TABLE `cosmax_usuario_groups` (
  `id` bigint NOT NULL,
  `usuario_id` bigint NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `cosmax_usuario_user_permissions`
--

CREATE TABLE `cosmax_usuario_user_permissions` (
  `id` bigint NOT NULL,
  `usuario_id` bigint NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `cosmax_venta`
--

CREATE TABLE `cosmax_venta` (
  `id` bigint NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `metodo_pago` varchar(20) NOT NULL,
  `cliente_id` bigint DEFAULT NULL,
  `empleado_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'group'),
(3, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(6, 'cosmax', 'cliente'),
(7, 'cosmax', 'detalleventa'),
(8, 'cosmax', 'libro'),
(9, 'cosmax', 'usuario'),
(10, 'cosmax', 'venta'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2026-06-03 17:21:30.006833'),
(2, 'contenttypes', '0002_remove_content_type_name', '2026-06-03 17:21:30.216543'),
(3, 'auth', '0001_initial', '2026-06-03 17:21:30.540507'),
(4, 'auth', '0002_alter_permission_name_max_length', '2026-06-03 17:21:30.618894'),
(5, 'auth', '0003_alter_user_email_max_length', '2026-06-03 17:21:30.628462'),
(6, 'auth', '0004_alter_user_username_opts', '2026-06-03 17:21:30.638545'),
(7, 'auth', '0005_alter_user_last_login_null', '2026-06-03 17:21:30.646220'),
(8, 'auth', '0006_require_contenttypes_0002', '2026-06-03 17:21:30.650994'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2026-06-03 17:21:30.660161'),
(10, 'auth', '0008_alter_user_username_max_length', '2026-06-03 17:21:30.669546'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2026-06-03 17:21:30.680326'),
(12, 'auth', '0010_alter_group_name_max_length', '2026-06-03 17:21:30.705567'),
(13, 'auth', '0011_update_proxy_permissions', '2026-06-03 17:21:30.713536'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2026-06-03 17:21:30.721523'),
(15, 'cosmax', '0001_initial', '2026-06-03 17:21:31.503584'),
(16, 'admin', '0001_initial', '2026-06-03 17:21:31.689526'),
(17, 'admin', '0002_logentry_remove_auto_add', '2026-06-03 17:21:31.701606'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2026-06-03 17:21:31.712924'),
(19, 'sessions', '0001_initial', '2026-06-03 17:21:31.761848');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('pcvwnqf1r63sjveumu0w03lsrphut4oh', '.eJxVjLsOwjAMAP_FM4rqJmnSjux8Q2THDimgVupjQvw7qtQB1rvTvSHRvtW0r7qkUWAAhMsvY8pPnQ4hD5rus8nztC0jmyMxp13NbRZ9Xc_2b1BprTCASlRynZKKD-yaGF2rXbZCTStSLHsJ2DMSMgdsvA0YsGDpHWbno8LnCwUqOCc:1wUpId:DrS9htKVEdLYfy38sxF7CFfYN1t-AN-3M0W8_GkkxOE', '2026-06-17 17:22:39.383035');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `cosmax_cliente`
--
ALTER TABLE `cosmax_cliente`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cosmax_detalleventa`
--
ALTER TABLE `cosmax_detalleventa`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cosmax_detalleventa_libro_id_7f75d38f_fk_cosmax_libro_id` (`libro_id`),
  ADD KEY `cosmax_detalleventa_venta_id_884179fe_fk_cosmax_venta_id` (`venta_id`);

--
-- Indexes for table `cosmax_libro`
--
ALTER TABLE `cosmax_libro`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cosmax_usuario`
--
ALTER TABLE `cosmax_usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `cosmax_usuario_groups`
--
ALTER TABLE `cosmax_usuario_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `cosmax_usuario_groups_usuario_id_group_id_8bfa0a97_uniq` (`usuario_id`,`group_id`),
  ADD KEY `cosmax_usuario_groups_group_id_84b28e8c_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `cosmax_usuario_user_permissions`
--
ALTER TABLE `cosmax_usuario_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `cosmax_usuario_user_perm_usuario_id_permission_id_65673564_uniq` (`usuario_id`,`permission_id`),
  ADD KEY `cosmax_usuario_user__permission_id_996db64f_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `cosmax_venta`
--
ALTER TABLE `cosmax_venta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cosmax_venta_cliente_id_137a356c_fk_cosmax_cliente_id` (`cliente_id`),
  ADD KEY `cosmax_venta_empleado_id_183fc9ea_fk_cosmax_usuario_id` (`empleado_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_cosmax_usuario_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `cosmax_cliente`
--
ALTER TABLE `cosmax_cliente`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `cosmax_detalleventa`
--
ALTER TABLE `cosmax_detalleventa`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cosmax_libro`
--
ALTER TABLE `cosmax_libro`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cosmax_usuario`
--
ALTER TABLE `cosmax_usuario`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `cosmax_usuario_groups`
--
ALTER TABLE `cosmax_usuario_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cosmax_usuario_user_permissions`
--
ALTER TABLE `cosmax_usuario_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cosmax_venta`
--
ALTER TABLE `cosmax_venta`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `cosmax_detalleventa`
--
ALTER TABLE `cosmax_detalleventa`
  ADD CONSTRAINT `cosmax_detalleventa_libro_id_7f75d38f_fk_cosmax_libro_id` FOREIGN KEY (`libro_id`) REFERENCES `cosmax_libro` (`id`),
  ADD CONSTRAINT `cosmax_detalleventa_venta_id_884179fe_fk_cosmax_venta_id` FOREIGN KEY (`venta_id`) REFERENCES `cosmax_venta` (`id`);

--
-- Constraints for table `cosmax_usuario_groups`
--
ALTER TABLE `cosmax_usuario_groups`
  ADD CONSTRAINT `cosmax_usuario_groups_group_id_84b28e8c_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `cosmax_usuario_groups_usuario_id_9502c7aa_fk_cosmax_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `cosmax_usuario` (`id`);

--
-- Constraints for table `cosmax_usuario_user_permissions`
--
ALTER TABLE `cosmax_usuario_user_permissions`
  ADD CONSTRAINT `cosmax_usuario_user__permission_id_996db64f_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `cosmax_usuario_user__usuario_id_65730c9e_fk_cosmax_us` FOREIGN KEY (`usuario_id`) REFERENCES `cosmax_usuario` (`id`);

--
-- Constraints for table `cosmax_venta`
--
ALTER TABLE `cosmax_venta`
  ADD CONSTRAINT `cosmax_venta_cliente_id_137a356c_fk_cosmax_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `cosmax_cliente` (`id`),
  ADD CONSTRAINT `cosmax_venta_empleado_id_183fc9ea_fk_cosmax_usuario_id` FOREIGN KEY (`empleado_id`) REFERENCES `cosmax_usuario` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_cosmax_usuario_id` FOREIGN KEY (`user_id`) REFERENCES `cosmax_usuario` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
