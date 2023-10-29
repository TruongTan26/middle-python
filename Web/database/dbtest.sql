-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th10 29, 2023 lúc 10:57 AM
-- Phiên bản máy phục vụ: 10.4.28-MariaDB
-- Phiên bản PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `dbtest`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `messages`
--

CREATE TABLE `messages` (
  `id` int(11) NOT NULL,
  `sender` varchar(255) NOT NULL,
  `message` text NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `messages`
--

INSERT INTO `messages` (`id`, `sender`, `message`, `created_at`) VALUES
(1, 'User', 's', '2023-10-28 03:47:17'),
(2, 'User', 'sss', '2023-10-28 03:47:19'),
(3, 'User', '5', '2023-10-28 04:09:05'),
(4, 'User', '45', '2023-10-28 04:09:15'),
(5, 'User', '22', '2023-10-28 04:16:15'),
(6, 'User', '123aas', '2023-10-28 04:16:47'),
(7, 'User', '1', '2023-10-28 09:36:58'),
(8, 'User', '123', '2023-10-29 09:44:32'),
(9, 'User', '123', '2023-10-29 09:49:07'),
(10, 'User', '4s', '2023-10-29 09:49:42');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `tbl_info`
--

CREATE TABLE `tbl_info` (
  `id` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `tbl_info`
--

INSERT INTO `tbl_info` (`id`, `name`, `lastname`, `contact`, `address`) VALUES
(1, 'sample1', 'sample1', 'sample1', 'sample1'),
(2, 'sample2', 'sample2', 'sample2', 'sample2'),
(3, 'sample3', 'sample3', 'sample3', 'sample3');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `tbl_menu`
--

CREATE TABLE `tbl_menu` (
  `menu_id` int(11) NOT NULL,
  `menu_name` varchar(100) NOT NULL,
  `menu_price` varchar(100) NOT NULL,
  `menu_group` varchar(100) NOT NULL,
  `menu_` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `tbl_menu`
--

INSERT INTO `tbl_menu` (`menu_id`, `menu_name`, `menu_price`, `menu_group`, `menu_`) VALUES
(1, 'Cà phê', '10000', 'Đồ uống', ''),
(2, 'Sting vàng', '12000', 'Đồ uống', ''),
(3, 'Sting dâu', '12000', 'Đồ uống', ''),
(4, 'Bò cụng', '15000', 'Đồ uống', '');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `messages`
--
ALTER TABLE `messages`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `tbl_info`
--
ALTER TABLE `tbl_info`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `tbl_menu`
--
ALTER TABLE `tbl_menu`
  ADD PRIMARY KEY (`menu_id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `messages`
--
ALTER TABLE `messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT cho bảng `tbl_info`
--
ALTER TABLE `tbl_info`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT cho bảng `tbl_menu`
--
ALTER TABLE `tbl_menu`
  MODIFY `menu_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
