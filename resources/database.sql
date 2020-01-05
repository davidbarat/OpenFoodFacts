
CREATE TABLE categories
(
    id_category INT
    AUTO_INCREMENT NOT NULL PRIMARY KEY,
                category_name VARCHAR
    (40) NOT NULL
);


    CREATE TABLE products
    (
        barcode VARCHAR(20) NOT NULL PRIMARY KEY,
        id_category INT NOT NULL,
        food VARCHAR(25) NOT NULL,
        url_food VARCHAR(300) NOT NULL,
        store VARCHAR(100) NOT NULL,
        description_food VARCHAR(600) NOT NULL,
        nutriscore VARCHAR (2) NOT NULL
    );


    CREATE TABLE products_selected
    (
        barcode VARCHAR(20) NOT NULL PRIMARY KEY,
        products_selected VARCHAR(50) NOT NULL,
        substitute VARCHAR(50) NOT NULL
    );


    ALTER TABLE products ADD CONSTRAINT categories_products_fk
FOREIGN KEY (id_category)
REFERENCES categories (id_category)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

    ALTER TABLE products_selected ADD CONSTRAINT products_products_selected_fk
FOREIGN KEY (barcode)
REFERENCES products (barcode)
ON DELETE NO ACTION
ON UPDATE NO ACTION;