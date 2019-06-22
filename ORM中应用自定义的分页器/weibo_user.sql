/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80016
 Source Host           : localhost:3306
 Source Schema         : student

 Target Server Type    : MySQL
 Target Server Version : 80016
 File Encoding         : 65001

 Date: 22/06/2019 16:47:39
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for weibo_user
-- ----------------------------
DROP TABLE IF EXISTS `weibo_user`;
CREATE TABLE `weibo_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(256) COLLATE utf8mb4_general_ci NOT NULL,
  `nickname` varchar(32) COLLATE utf8mb4_general_ci NOT NULL,
  `status` smallint(6) NOT NULL,
  `create_at` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of weibo_user
-- ----------------------------
BEGIN;
INSERT INTO `weibo_user` VALUES (5, 'kiki', '112233', '小花', 1, '2019-06-19 09:13:08.000000');
INSERT INTO `weibo_user` VALUES (6, 'xixi', '112233', '美女', 1, '2019-06-21 13:51:31.000000');
INSERT INTO `weibo_user` VALUES (7, 'zhangsan', '112233', '张三', 0, '2019-06-20 17:07:36.000000');
INSERT INTO `weibo_user` VALUES (8, 'user1', '112233', '用户1', 1, '2019-06-15 19:51:48.000000');
INSERT INTO `weibo_user` VALUES (9, 'user2', '112233', '用户2', 2, NULL);
INSERT INTO `weibo_user` VALUES (10, 'user3', '112233', '用户3', 1, '2019-06-21 07:52:00.000000');
INSERT INTO `weibo_user` VALUES (11, 'user0', '123456', '用户0', 1, NULL);
INSERT INTO `weibo_user` VALUES (12, 'user1', '123456', '用户1', 1, NULL);
INSERT INTO `weibo_user` VALUES (13, 'user2', '123456', '用户2', 1, NULL);
INSERT INTO `weibo_user` VALUES (14, 'user3', '123456', '用户3', 1, NULL);
INSERT INTO `weibo_user` VALUES (15, 'lisi', '123456', '李四', 1, NULL);
INSERT INTO `weibo_user` VALUES (16, 'user5', '123456', '用户5', 1, NULL);
INSERT INTO `weibo_user` VALUES (17, 'user6', '123456', '用户6', 1, NULL);
INSERT INTO `weibo_user` VALUES (18, 'user7', '123456', '张小三', 2, NULL);
INSERT INTO `weibo_user` VALUES (19, 'user8', '123456', '用户8', 1, NULL);
INSERT INTO `weibo_user` VALUES (20, 'user9', '123456', '用户9', 1, NULL);
INSERT INTO `weibo_user` VALUES (21, 'user10', '123456', '用户10', 1, NULL);
INSERT INTO `weibo_user` VALUES (22, 'user11', '123456', '用户11', 4, NULL);
INSERT INTO `weibo_user` VALUES (23, 'user12', '123456', '用户12', 1, NULL);
INSERT INTO `weibo_user` VALUES (24, 'zhangsan', '123456', 'ZhangSan3', 1, NULL);
INSERT INTO `weibo_user` VALUES (25, 'user14', '123456', '用户14', 1, NULL);
INSERT INTO `weibo_user` VALUES (26, 'user15', '123456', '小张三', 1, NULL);
INSERT INTO `weibo_user` VALUES (27, 'user16', '123456', 'zhangsan', 1, NULL);
INSERT INTO `weibo_user` VALUES (28, 'ZhangSan', '123456', '用户17', 1, NULL);
INSERT INTO `weibo_user` VALUES (29, 'user18', '123456', '用户18', 1, NULL);
INSERT INTO `weibo_user` VALUES (30, 'user19', '123456', '用户19', 1, NULL);
INSERT INTO `weibo_user` VALUES (31, 'zhangSan', '123456', '用户20', 1, NULL);
INSERT INTO `weibo_user` VALUES (32, 'user21', '123456', '用户21', 1, NULL);
INSERT INTO `weibo_user` VALUES (33, 'Zhangsan', '123456', '用户22', 1, NULL);
INSERT INTO `weibo_user` VALUES (34, 'user23', '123456', '用户23', 1, NULL);
INSERT INTO `weibo_user` VALUES (35, 'user24', '123456', '用户24', 1, NULL);
INSERT INTO `weibo_user` VALUES (36, 'user25', '123456', '用户25', 1, NULL);
INSERT INTO `weibo_user` VALUES (37, 'user26', '123456', '用户26', 1, NULL);
INSERT INTO `weibo_user` VALUES (38, 'user27', '123456', '用户27', 1, NULL);
INSERT INTO `weibo_user` VALUES (39, 'user28', '123456', '用户28', 1, NULL);
INSERT INTO `weibo_user` VALUES (40, 'user29', '123456', '用户29', 1, NULL);
INSERT INTO `weibo_user` VALUES (41, 'user30', '123456', '用户30', 1, NULL);
INSERT INTO `weibo_user` VALUES (42, 'user31', '123456', '用户31', 1, NULL);
INSERT INTO `weibo_user` VALUES (43, 'user32', '123456', '用户32', 1, NULL);
INSERT INTO `weibo_user` VALUES (44, 'user33', '123456', '用户33', 1, NULL);
INSERT INTO `weibo_user` VALUES (45, 'user34', '123456', '用户34', 1, NULL);
INSERT INTO `weibo_user` VALUES (46, 'user35', '123456', '用户35', 1, NULL);
INSERT INTO `weibo_user` VALUES (47, 'user36', '123456', '用户36', 1, NULL);
INSERT INTO `weibo_user` VALUES (48, 'user37', '123456', '用户37', 1, NULL);
INSERT INTO `weibo_user` VALUES (49, 'user38', '123456', '用户38', 1, NULL);
INSERT INTO `weibo_user` VALUES (50, 'user39', '123456', '用户39', 1, NULL);
INSERT INTO `weibo_user` VALUES (51, 'user40', '123456', '用户40', 1, NULL);
INSERT INTO `weibo_user` VALUES (52, 'user41', '123456', '用户41', 1, NULL);
INSERT INTO `weibo_user` VALUES (53, 'user42', '123456', '用户42', 1, NULL);
INSERT INTO `weibo_user` VALUES (54, 'user43', '123456', '用户43', 1, NULL);
INSERT INTO `weibo_user` VALUES (55, 'user44', '123456', '用户44', 1, NULL);
INSERT INTO `weibo_user` VALUES (56, 'user45', '123456', '用户45', 1, NULL);
INSERT INTO `weibo_user` VALUES (57, 'user46', '123456', '用户46', 1, NULL);
INSERT INTO `weibo_user` VALUES (58, 'user47', '123456', '用户47', 1, NULL);
INSERT INTO `weibo_user` VALUES (59, 'user48', '123456', '用户48', 1, NULL);
INSERT INTO `weibo_user` VALUES (60, 'user49', '123456', '用户49', 1, NULL);
INSERT INTO `weibo_user` VALUES (61, 'user50', '123456', '用户50', 1, NULL);
INSERT INTO `weibo_user` VALUES (62, 'user51', '123456', '用户51', 1, NULL);
INSERT INTO `weibo_user` VALUES (63, 'user52', '123456', '用户52', 1, NULL);
INSERT INTO `weibo_user` VALUES (64, 'user53', '123456', '用户53', 1, NULL);
INSERT INTO `weibo_user` VALUES (65, 'user54', '123456', '用户54', 1, NULL);
INSERT INTO `weibo_user` VALUES (66, 'user55', '123456', '用户55', 1, NULL);
INSERT INTO `weibo_user` VALUES (67, 'user56', '123456', '用户56', 1, NULL);
INSERT INTO `weibo_user` VALUES (68, 'user57', '123456', '用户57', 1, NULL);
INSERT INTO `weibo_user` VALUES (69, 'user58', '123456', '用户58', 1, NULL);
INSERT INTO `weibo_user` VALUES (70, 'user59', '123456', '用户59', 1, NULL);
INSERT INTO `weibo_user` VALUES (71, 'user60', '123456', '用户60', 1, NULL);
INSERT INTO `weibo_user` VALUES (72, 'user61', '123456', '用户61', 1, NULL);
INSERT INTO `weibo_user` VALUES (73, 'user62', '123456', '用户62', 1, NULL);
INSERT INTO `weibo_user` VALUES (74, 'user63', '123456', '用户63', 1, NULL);
INSERT INTO `weibo_user` VALUES (75, 'user64', '123456', '用户64', 1, NULL);
INSERT INTO `weibo_user` VALUES (76, 'user65', '123456', '用户65', 1, NULL);
INSERT INTO `weibo_user` VALUES (77, 'user66', '123456', '用户66', 1, NULL);
INSERT INTO `weibo_user` VALUES (78, 'user67', '123456', '用户67', 1, NULL);
INSERT INTO `weibo_user` VALUES (79, 'user68', '123456', '用户68', 1, NULL);
INSERT INTO `weibo_user` VALUES (80, 'user69', '123456', '用户69', 1, NULL);
INSERT INTO `weibo_user` VALUES (81, 'user70', '123456', '用户70', 1, NULL);
INSERT INTO `weibo_user` VALUES (82, 'user71', '123456', '用户71', 1, NULL);
INSERT INTO `weibo_user` VALUES (83, 'user72', '123456', '用户72', 1, NULL);
INSERT INTO `weibo_user` VALUES (84, 'user73', '123456', '用户73', 1, NULL);
INSERT INTO `weibo_user` VALUES (85, 'user74', '123456', '用户74', 1, NULL);
INSERT INTO `weibo_user` VALUES (86, 'user75', '123456', '用户75', 1, NULL);
INSERT INTO `weibo_user` VALUES (87, 'user76', '123456', '用户76', 1, NULL);
INSERT INTO `weibo_user` VALUES (88, 'user77', '123456', '用户77', 1, NULL);
INSERT INTO `weibo_user` VALUES (89, 'user78', '123456', '用户78', 1, NULL);
INSERT INTO `weibo_user` VALUES (90, 'user79', '123456', '用户79', 1, NULL);
INSERT INTO `weibo_user` VALUES (91, 'user80', '123456', '用户80', 1, NULL);
INSERT INTO `weibo_user` VALUES (92, 'user81', '123456', '用户81', 1, NULL);
INSERT INTO `weibo_user` VALUES (93, 'user82', '123456', '用户82', 1, NULL);
INSERT INTO `weibo_user` VALUES (94, 'user83', '123456', '用户83', 1, NULL);
INSERT INTO `weibo_user` VALUES (95, 'user84', '123456', '用户84', 1, NULL);
INSERT INTO `weibo_user` VALUES (96, 'user85', '123456', '用户85', 1, NULL);
INSERT INTO `weibo_user` VALUES (97, 'user86', '123456', '用户86', 1, NULL);
INSERT INTO `weibo_user` VALUES (98, 'user87', '123456', '用户87', 1, NULL);
INSERT INTO `weibo_user` VALUES (99, 'user88', '123456', '用户88', 1, NULL);
INSERT INTO `weibo_user` VALUES (100, 'user89', '123456', '用户89', 1, NULL);
INSERT INTO `weibo_user` VALUES (101, 'user90', '123456', '用户90', 1, NULL);
INSERT INTO `weibo_user` VALUES (102, 'user91', '123456', '用户91', 1, NULL);
INSERT INTO `weibo_user` VALUES (103, 'user92', '123456', '用户92', 1, NULL);
INSERT INTO `weibo_user` VALUES (104, 'user93', '123456', '用户93', 1, NULL);
INSERT INTO `weibo_user` VALUES (105, 'user94', '123456', '用户94', 1, NULL);
INSERT INTO `weibo_user` VALUES (106, 'user95', '123456', '用户95', 1, NULL);
INSERT INTO `weibo_user` VALUES (107, 'user96', '123456', '用户96', 1, NULL);
INSERT INTO `weibo_user` VALUES (108, 'user97', '123456', '用户97', 1, NULL);
INSERT INTO `weibo_user` VALUES (109, 'user98', '123456', '用户98', 1, NULL);
INSERT INTO `weibo_user` VALUES (110, 'user99', '123456', '用户99', 1, NULL);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
