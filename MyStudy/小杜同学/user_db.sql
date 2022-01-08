-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2020-11-26 17:36:36
-- 服务器版本： 8.0.12
-- PHP 版本： 7.3.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `user_db`
--

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE `user` (
  `user` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `pwd` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `user`
--

INSERT INTO `user` (`user`, `pwd`) VALUES
('hello', 'world'),
('你好', '你好，我是小杜'),
('你叫什么名字', '你好，我叫小杜'),
('你是谁', '我是小杜呀！'),
('格力客服电话', '4008365315'),
('申通快递电话', '95543'),
('小米服务热线', '4001005678'),
('顺丰客服电话', '95338'),
('市民专线', '12345'),
('520是什么意思', '5是五个落实：落实经济结构调整、落实精准扶贫、落实社会保障、落实环境治理、落实反腐倡廉。2是两个要：要经济发展、更要碧水蓝天。0是对违法问题0容忍。');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
