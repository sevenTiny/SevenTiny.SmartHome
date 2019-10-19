/*
Navicat MySQL Data Transfer

Source Server         : 192.168.0.107
Source Server Version : 50644
Source Host           : 192.168.0.107:39901
Source Database       : SmartHome

Target Server Type    : MYSQL
Target Server Version : 50644
File Encoding         : 65001

Date: 2019-10-08 21:38:09
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for DailyMonitor
-- ----------------------------
DROP TABLE IF EXISTS `DailyMonitor`;
CREATE TABLE `DailyMonitor` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `DateTime` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  `Year` int(11) DEFAULT NULL,
  `Month` int(11) DEFAULT NULL,
  `Day` int(11) DEFAULT NULL,
  `Hour` int(11) DEFAULT NULL,
  `Temperature` double(255,0) DEFAULT NULL,
  `Humidity` double(255,0) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=1211 DEFAULT CHARSET=utf8;
