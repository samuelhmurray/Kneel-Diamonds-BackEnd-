DROP TABLE IF EXISTS Orders;


CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carats` NUMERIC(5,2) NOT NULL, 
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metalId` INTEGER NOT NULL,
    `sizeId` INTEGER NOT NULL,
    `styleId` INTEGER NOT NULL,
    FOREIGN KEY(`metalId`) REFERENCES `Metals`(`id`),
    FOREIGN KEY(`styleId`) REFERENCES `Styles`(`id`),
    FOREIGN KEY(`sizeId`) REFERENCES `Sizes`(`id`)
);

INSERT INTO `Metals` VALUES (null, 'Sterling Silver', 12.42);
INSERT INTO `Metals` VALUES (null, '14K Gold', 736.4);
INSERT INTO `Metals` VALUES (null, '24K Gold', 12.42);
INSERT INTO `Metals` VALUES (null, 'Platinum', 795.45);
INSERT INTO `Metals` VALUES (null, 'Palladium', 1241);

INSERT INTO `Styles` VALUES (null, 'Classic', 500);
INSERT INTO `Styles` VALUES (null, 'Modern', 710);
INSERT INTO `Styles` VALUES (null, 'Vintage', 965);

INSERT INTO `Sizes` VALUES (null, 0.5, 405);
INSERT INTO `Sizes` VALUES (null, 0.75, 782);
INSERT INTO `Sizes` VALUES (null, 1, 1470);
INSERT INTO `Sizes` VALUES (null, 1.5, 1997);
INSERT INTO `Sizes` VALUES (null, 2, 3638);

INSERT INTO `Orders` VALUES (null, 2, 2, 2);
INSERT INTO `Orders` VALUES (null, 2, 3, 1);
INSERT INTO `Orders` VALUES (null, 1, 2, 1);
INSERT INTO `Orders` VALUES (null, 2, 1, 3);


