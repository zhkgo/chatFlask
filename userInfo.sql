/*
Navicat MySQL Data Transfer

Source Server         : zhkgo
Source Server Version : 50721
Source Host           : localhost:3306
Source Database       : chatDB

Target Server Type    : MYSQL
Target Server Version : 50721
File Encoding         : 65001

Date: 2018-12-18 22:19:16
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for userInfo
-- ----------------------------
DROP TABLE IF EXISTS `userInfo`;
CREATE TABLE `userInfo` (
  `username` varchar(16) NOT NULL,
  `password` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
