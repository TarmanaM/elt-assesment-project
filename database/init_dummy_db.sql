CREATE TABLE store (
    store_id INT PRIMARY KEY,
    store_name VARCHAR(100),
    store_format_name VARCHAR(100),
    store_city VARCHAR(100),
    store_state VARCHAR(10)
);

CREATE TABLE trx_total (
    trx_id INT PRIMARY KEY,
    store_id INT,
    customer_id BIGINT,
    trx_amount BIGINT,
    FOREIGN KEY (store_id) REFERENCES store(store_id)
);

INSERT INTO store (store_id, store_name, store_format_name, store_city, store_state) VALUES
(484, 'HPM PALANGKARAYA', 'Hypermart', 'Palangkaraya', 'KTG'),
(205, 'HPM KEMANG', 'Hypermart', 'Jakarta Selatan', 'DKI'),
(302, 'HPM PONTIANAK', 'Hypermart', 'Pontianak', 'KBR'),
(241, 'HPM CYBERPARK KRWC', 'Hypermart', 'Tangerang', 'BNT');

INSERT INTO trx_total (trx_id, store_id, customer_id, trx_amount) VALUES
(1, 484, 437490892, 2518160),
(2, 205, 537483745, 9179920),
(3, 302, 954727277, 5843077),
(4, 241, 954727277, 2889998),
(5, 241, 548738747, 3482058);
