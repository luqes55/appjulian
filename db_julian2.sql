-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-11-2024 a las 20:44:39
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db_julian2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `idCliente` bigint(20) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `apellidos` varchar(45) NOT NULL,
  `nit` bigint(20) NOT NULL,
  `correo` varchar(65) NOT NULL,
  `direccion` varchar(65) NOT NULL,
  `telefono` int(20) NOT NULL,
  `fechaIngreso` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`idCliente`, `nombre`, `apellidos`, `nit`, `correo`, `direccion`, `telefono`, `fechaIngreso`) VALUES
(14, 'maria', 'maria', 1131213, 'mari@gmail.com', 'casn', 321332, '2024-11-18'),
(15, 'mariano', 'luques', 1222121, 'mari@gmail.com', 'santa fe', 314236535, '2024-11-18'),
(16, 'mariano', 'luques', 1222121, 'mari@gmail.com', 'santa fe', 314236535, '2024-11-18'),
(17, 'mariano', 'luques', 1222121, 'mari@gmail.com', 'santa fe', 314236535, '2024-11-18'),
(18, 'mariano', 'luques', 1222121, 'mari@gmail.com', 'santa fe', 314236535, '2024-11-18'),
(19, 'mariana', 'lopez', 1111111, 'octa@gmail.com', 'santa', 322232221, '0000-00-00'),
(20, 'mariana', 'lopez', 1111111, 'octa@gmail.com', 'santa', 322232221, '0000-00-00'),
(21, 'mariana', 'lopez', 1111111, 'octa@gmail.com', 'santa', 322232221, '2024-11-19'),
(22, 'santiago', 'londoño', 1193553973, 'octag@gmail.com', 'sanjeronimo', 324561272, '2024-11-19'),
(23, 'juliana', 'lopez', 11211212323, 'juli@gmail.com', 'santa fe', 314562738, '2024-11-20'),
(24, 'juliana', 'lopez', 11211212323, 'juli@gmail.com', 'santa fe', 314562738, '2024-11-20'),
(25, 'juliana', 'lopez', 11211212323, 'juli@gmail.com', 'santa fe', 314562738, '2024-11-20'),
(26, 'juliana', 'lopez', 11211212323, 'juli@gmail.com', 'santa fe', 314562738, '2024-11-20'),
(27, 'juliana', 'lopez', 11211212323, 'juli@gmail.com', 'santa fe', 314562738, '2024-11-20'),
(28, 'juliana', 'lopez', 11211212323, 'juli@gmail.com', 'santa fe', 314562738, '2024-11-20'),
(29, 'juliana', 'lopez', 11211212323, 'juli@gmail.com', 'santa fe', 314562738, '2024-11-20'),
(30, 'juliana', 'lopez', 11211212323, 'juli@gmail.com', 'santa fe', 314562738, '2024-11-20'),
(31, 'juliana', 'lopez', 11211212323, 'juli@gmail.com', 'santa fe', 314562738, '2024-11-20'),
(32, 'juliana', 'lopez', 11211212323, 'juli@gmail.com', 'santa fe', 314562738, '2024-11-20'),
(33, 'juliana', 'lopez', 11211212323, 'juli@gmail.com', 'santa fe', 314562738, '2024-11-20'),
(34, 'juliana', 'lopez', 11211212323, 'juli@gmail.com', 'santa fe', 314562738, '2024-11-20'),
(35, 'juliana', 'lopez', 11211212323, 'juli@gmail.com', 'santa fe', 314562738, '2024-11-20'),
(36, 'juliana', 'lopez', 11211212323, 'juli@gmail.com', 'santa fe', 314562738, '2024-11-20'),
(37, 'juliana', 'lopez', 11211212323, 'juli@gmail.com', 'santa fe', 314562738, '2024-11-20'),
(38, 'juliana', 'lopez', 11211212323, 'juli@gmail.com', 'santa fe', 314562738, '2024-11-20'),
(39, 'juliana', 'lopez', 11211212323, 'juli@gmail.com', 'santa fe', 314562738, '2024-11-20'),
(40, 'juliana', 'lopez', 11211212323, 'juli@gmail.com', 'santa fe', 314562738, '2024-11-20'),
(41, 'juliana', 'lopez', 11211212323, 'juli@gmail.com', 'santa fe', 314562738, '2024-11-20'),
(42, 'juliana', 'lopez', 11211212323, 'juli@gmail.com', 'santa fe', 314562738, '2024-11-20'),
(43, 'juliana', 'lopez', 11211212323, 'juli@gmail.com', 'santa fe', 314562738, '2024-11-20'),
(44, 'juliana', 'lopez', 11211212323, 'juli@gmail.com', 'santa fe', 314562738, '2024-11-20'),
(45, 'ndbceb', 'wnd wndbh', 342434, 'octa@gmail.com', 'santa', 232323, '2024-11-20'),
(46, 'ndbceb', 'wnd wndbh', 342434, 'octa@gmail.com', 'santa', 232323, '2024-11-20'),
(47, 'ndbceb', 'wnd wndbh', 342434, 'octa@gmail.com', 'santa', 232323, '2024-11-20'),
(48, 'ndbceb', 'wnd wndbh', 342434, 'octa@gmail.com', 'santa', 232323, '2024-11-20'),
(49, 'ndbceb', 'wnd wndbh', 342434, 'octa@gmail.com', 'santa', 232323, '2024-11-20'),
(50, 'maria', 'antonia', 119342633, 'mari@gmail.com', 'santta fe', 2147483647, '2024-11-20'),
(51, 'maria', 'antonia', 119342633, 'mari@gmail.com', 'santta fe', 2147483647, '2024-11-20'),
(52, 'maria', 'antonia', 119342633, 'mari@gmail.com', 'santta fe', 2147483647, '2024-11-20'),
(53, 'maria', 'antonia', 119342633, 'mari@gmail.com', 'santta fe', 2147483647, '2024-11-20'),
(54, 'mariana', 'lopez', 1193553983, 'mai@hotmail.com', 'cañasgordas', 2147483647, '2024-11-20'),
(55, 'mariana', 'lopez', 1193553983, 'mai@hotmail.com', 'cañasgordas', 2147483647, '2024-11-20'),
(56, 'mariana', 'lopez', 1193553983, 'mai@hotmail.com', 'cañasgordas', 2147483647, '2024-11-20'),
(57, 'mariana', 'lopez', 1193553983, 'mai@hotmail.com', 'cañasgordas', 2147483647, '2024-11-20'),
(58, 'mariana', 'lopez', 1193553983, 'mai@hotmail.com', 'cañasgordas', 2147483647, '2024-11-20'),
(59, 'maria', 'antonia', 119342633, 'mari@gmail.com', 'santta fe', 2147483647, '2024-11-20'),
(60, 'maria ', 'jacome', 1182553472, 'mari@gmail.com', 'calle 8 # 98-09', 2147483647, '2024-11-20'),
(61, 'maria ', 'jacome', 1182553472, 'mari@gmail.com', 'calle 8 # 98-09', 2147483647, '2024-11-20'),
(62, 'maria ', 'jacome', 1182553472, 'mari@gmail.com', 'calle 8 # 98-09', 2147483647, '2024-11-20'),
(63, 'maria ', 'jacome', 1182553472, 'mari@gmail.com', 'calle 8 # 98-09', 2147483647, '2024-11-20'),
(64, 'maria ', 'jacome', 1182553472, 'mari@gmail.com', 'calle 8 # 98-09', 2147483647, '2024-11-20'),
(65, 'maria ', 'jacome', 1182553472, 'mari@gmail.com', 'calle 8 # 98-09', 2147483647, '2024-11-20'),
(66, 'maria ', 'jacome', 1182553472, 'mari@gmail.com', 'calle 8 # 98-09', 2147483647, '2024-11-20'),
(67, 'maria ', 'jacome', 1182553472, 'mari@gmail.com', 'calle 8 # 98-09', 2147483647, '2024-11-20'),
(68, 'sara', 'suares', 12123232, 'sara@gmail.com', 'santa fe ', 3511453, '2024-11-20'),
(69, 'manuel', 'marin', 13242524646, 'cae@gmail.com', 'santa fe ', 2147483647, '2024-11-21'),
(70, 'manuel', 'marin', 13242524646, 'cae@gmail.com', 'santa fe ', 2147483647, '2024-11-21'),
(71, 'manuel', 'marin', 13242524646, 'cae@gmail.com', 'santa fe ', 2147483647, '2024-11-21'),
(72, 'manuel', 'marin', 13242524646, 'cae@gmail.com', 'santa fe ', 2147483647, '2024-11-21'),
(73, 'manuel', 'marin', 13242524646, 'cae@gmail.com', 'santa fe ', 2147483647, '2024-11-21'),
(74, 'manuel', 'marin', 13242524646, 'cae@gmail.com', 'santa fe ', 2147483647, '2024-11-21'),
(75, 'manuel', 'marin', 13242524646, 'cae@gmail.com', 'santa fe ', 2147483647, '2024-11-21'),
(76, 'manuel', 'marin', 13242524646, 'cae@gmail.com', 'santa fe ', 2147483647, '2024-11-21'),
(77, 'manuel', 'marin', 13242524646, 'cae@gmail.com', 'santa fe ', 2147483647, '2024-11-21'),
(78, 'manuel', 'marin', 13242524646, 'cae@gmail.com', 'santa fe ', 2147483647, '2024-11-21'),
(79, 'manuel', 'marin', 13242524646, 'cae@gmail.com', 'santa fe ', 2147483647, '2024-11-21'),
(80, 'manuel', 'marin', 13242524646, 'cae@gmail.com', 'santa fe ', 2147483647, '2024-11-21'),
(81, 'manuel', 'marin', 13242524646, 'cae@gmail.com', 'santa fe ', 2147483647, '2024-11-21'),
(82, 'manuel', 'marin', 13242524646, 'cae@gmail.com', 'santa fe ', 2147483647, '2024-11-21'),
(83, 'wjdqsj', 'knwjdbwjdb', 545, 'ndvdbn@gmail.com', 'HVDVAD', 5446564, '2024-11-21');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dispositivo`
--

CREATE TABLE `dispositivo` (
  `idDispositivo` bigint(20) NOT NULL,
  `idCliente` bigint(20) NOT NULL,
  `marca` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `modelo` varchar(45) NOT NULL,
  `Per_recibe` varchar(45) NOT NULL,
  `clave_tel` varchar(45) NOT NULL,
  `abono` decimal(10,2) NOT NULL,
  `color` varchar(20) NOT NULL,
  `enciende` varchar(3) NOT NULL,
  `display_quebrado` varchar(3) NOT NULL,
  `tapa_quebrada` varchar(10) NOT NULL,
  `botones` varchar(3) NOT NULL,
  `bandeja_sim` varchar(3) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `estuche` varchar(3) NOT NULL,
  `simcard` varchar(3) NOT NULL,
  `estado` varchar(10) NOT NULL,
  `detalles` varchar(255) NOT NULL,
  `Imei` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `dispositivo`
--

INSERT INTO `dispositivo` (`idDispositivo`, `idCliente`, `marca`, `modelo`, `Per_recibe`, `clave_tel`, `abono`, `color`, `enciende`, `display_quebrado`, `tapa_quebrada`, `botones`, `bandeja_sim`, `estuche`, `simcard`, `estado`, `detalles`, `Imei`) VALUES
(11, 67, 'Iphone', '14 pro max', 'Julian', '23242', 100.00, 'amarillo', 'si', 'si', 'buena', 'si', 'si', 'si', 'si', 'reparacion', 'pantalla rota', ''),
(12, 68, 'Samgung', '2020', 'Julian', '2324', 100000.00, 'amarillo', 'si', 'si', 'buena', 'si', 'si', 'si', 'si', 'Malo', 'nada', '12454534435323'),
(13, 69, 'Iphone', '2020', 'Manuel', '341524', 20.00, 'amarillo', 'si', 'si', 'buena', 'si', 'si', 'si', 'si', 'malo', 'roto', '171625255626241'),
(14, 70, 'Iphone', '2020', 'Manuel', '341524', 20.00, 'amarillo', 'si', 'si', 'buena', 'si', 'si', 'si', 'si', 'malo', 'roto', '171625255626241'),
(15, 71, 'Iphone', '2020', 'Manuel', '341524', 20.00, 'amarillo', 'si', 'si', 'buena', 'si', 'si', 'si', 'si', 'malo', 'roto', '171625255626241'),
(16, 72, 'Iphone', '2020', 'Manuel', '341524', 20.00, 'amarillo', 'si', 'si', 'buena', 'si', 'si', 'si', 'si', 'malo', 'roto', '171625255626241'),
(17, 73, 'Iphone', '2020', 'Manuel', '341524', 20.00, 'amarillo', 'si', 'si', 'buena', 'si', 'si', 'si', 'si', 'malo', 'roto', '171625255626241'),
(18, 74, 'Iphone', '2020', 'Manuel', '341524', 20.00, 'amarillo', 'si', 'si', 'buena', 'si', 'si', 'si', 'si', 'malo', 'roto', '171625255626241'),
(19, 75, 'Iphone', '2020', 'Manuel', '341524', 20.00, 'amarillo', 'si', 'si', 'buena', 'si', 'si', 'si', 'si', 'malo', 'roto', '171625255626241'),
(20, 76, 'Iphone', '2020', 'Manuel', '341524', 20.00, 'amarillo', 'si', 'si', 'buena', 'si', 'si', 'si', 'si', 'malo', 'roto', '171625255626241'),
(21, 77, 'Iphone', '2020', 'Manuel', '341524', 20.00, 'amarillo', 'si', 'si', 'buena', 'si', 'si', 'si', 'si', 'malo', 'roto', '171625255626241'),
(22, 78, 'Iphone', '2020', 'Manuel', '341524', 20.00, 'amarillo', 'si', 'si', 'buena', 'si', 'si', 'si', 'si', 'malo', 'roto', '171625255626241'),
(23, 79, 'Iphone', '2020', 'Manuel', '341524', 20.00, 'amarillo', 'si', 'si', 'buena', 'si', 'si', 'si', 'si', 'malo', 'roto', '171625255626241'),
(24, 80, 'Iphone', '2020', 'Manuel', '341524', 20.00, 'amarillo', 'si', 'si', 'buena', 'si', 'si', 'si', 'si', 'malo', 'roto', '171625255626241'),
(25, 81, 'Iphone', '2020', 'Manuel', '341524', 20.00, 'amarillo', 'si', 'si', 'buena', 'si', 'si', 'si', 'si', 'malo', 'roto', '171625255626241'),
(26, 82, 'Iphone', '2020', 'Manuel', '341524', 20.00, 'amarillo', 'si', 'si', 'buena', 'si', 'si', 'si', 'si', 'malo', 'roto', '171625255626241'),
(27, 83, 'Iphone', '14 pro max', 'Camila', '656565', 100.00, 'amarillo', 'si', 'si', 'buena', 'si', 'si', 'si', 'si', 'malo', 'hvhvahvsahv', '4453534343');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reportefinal`
--

CREATE TABLE `reportefinal` (
  `tec_arregla` varchar(20) NOT NULL,
  `fechaReparacion` date NOT NULL DEFAULT current_timestamp(),
  `fechaEntrega` date NOT NULL DEFAULT current_timestamp(),
  `provedorRepuesto` varchar(30) NOT NULL,
  `valorRepuesto` decimal(10,2) NOT NULL,
  `nombreRepuesto` varchar(20) NOT NULL,
  `valorArreglo` decimal(10,2) NOT NULL,
  `idDispositivo` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` bigint(20) NOT NULL,
  `usuario` varchar(45) NOT NULL,
  `password` varchar(255) NOT NULL,
  `pin` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `usuario`, `password`, `pin`) VALUES
(20, 'octavio', 'scrypt:32768:8:1$fGv22Bt85S1lbc8x$3280851e74a2a2ca9fb946a55d62ca885501c26c1b2bd0689ca5f8bb0e5ef0cab831eb96a0bbb9ecea1a6f7abaacf3385ea992234c3b08f1facbecd46d94647e', 12345),
(21, 'jader', 'scrypt:32768:8:1$fV9RnvPpBpKL15jC$16dd6368b9c73dd94fbf22d8a1663627c0f441b28389ac5fb74d4268de1552244e05b241160c274a4c20e13296508749992120057a4b0f88d62c950685cc6ceb', 1234);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`idCliente`);

--
-- Indices de la tabla `dispositivo`
--
ALTER TABLE `dispositivo`
  ADD PRIMARY KEY (`idDispositivo`),
  ADD KEY `idCliente` (`idCliente`);

--
-- Indices de la tabla `reportefinal`
--
ALTER TABLE `reportefinal`
  ADD KEY `idDispositivo` (`idDispositivo`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `idCliente` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=84;

--
-- AUTO_INCREMENT de la tabla `dispositivo`
--
ALTER TABLE `dispositivo`
  MODIFY `idDispositivo` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `dispositivo`
--
ALTER TABLE `dispositivo`
  ADD CONSTRAINT `dispositivo_ibfk_1` FOREIGN KEY (`idCliente`) REFERENCES `cliente` (`idCliente`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
