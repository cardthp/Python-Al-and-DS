CREATE TABLE IF NOT EXISTS customers (
	id INT NOT NULL PRIMARY KEY,
	customer_id VARCHAR(255),
	favourite_product VARCHAR(255),
	longest_streak INT
);