CREATE TABLE `categories`
(
  `id_category` int
(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar
(40) NOT NULL,
  PRIMARY KEY
(`id_category`);

CREATE TABLE `products`
(
  `barcode` varchar
(20) NOT NULL,
  `id_category` int
(11) NOT NULL,
  `food` varchar
(70) NOT NULL,
  `url_food` varchar
(300) NOT NULL,
  `store` varchar
(120) NOT NULL,
  `description_food` varchar
(850) NOT NULL,
  `nutriscore` varchar
(2) NOT NULL,
  PRIMARY KEY
(`barcode`),
  KEY `categories_products_fk`
(`id_category`),
  CONSTRAINT `categories_products_fk` FOREIGN KEY
(`id_category`) REFERENCES `categories`
(`id_category`)
);

CREATE TABLE `products_selected`
(
  `barcode` varchar
(20) NOT NULL,
  `substitute_barcode` varchar
(20) DEFAULT NULL,
  PRIMARY KEY
(`barcode`),
  CONSTRAINT `products_products_selected_fk` FOREIGN KEY
(`barcode`) REFERENCES `products`
(`barcode`)
);