INSERT INTO products
SELECT
    generateUUIDv4() AS product_id,
    concat('Product ', toString(number)) AS product_name,
    arrayElement(['Электроника', 'Одежда', 'Книги', 'Спорт', 'Красота', 'Детские товары'], rand() % 6 + 1) AS category,
    arrayElement(['Apple', 'Samsung', 'Nike', 'Adidas', 'Sony', 'LG', 'HP', 'Dell'], rand() % 8 + 1) AS brand,
    round(rand() % 100000, 2) AS price,
    round(rand() % 100, 2) AS discount,
    rand() % 1000 AS stock_quantity,
    rand() % 2 = 1 AS is_available,
    toDateTime(now() - rand() % 365 * 86400) AS created_at,
    toDateTime(now() - rand() % 365 * 86400) AS updated_at,
    concat('Описание продукта ', toString(number)) AS description,
    [arrayElement(['новый', 'популярный', 'скидка', 'бестселлер'], rand() % 4 + 1)] AS tags,
    [('Цвет', arrayElement(['красный', 'синий', 'зеленый', 'черный'], rand() % 4 + 1)), ('Размер', arrayElement(['S', 'M', 'L', 'XL'], rand() % 4 + 1))] AS attributes,
    round(rand() % 5, 1) AS rating,
    rand() % 1000 AS reviews_count,
    toString(rand64()) AS vendor_code,
    round(rand() % 10, 2) AS weight,
    (round(rand() % 100, 2), round(rand() % 100, 2), round(rand() % 100, 2)) AS dimensions,
    toString(rand64()) AS barcode,
    arrayElement(['Supplier A', 'Supplier B', 'Supplier C', 'Supplier D'], rand() % 4 + 1) AS supplier,
    arrayElement(['Китай', 'США', 'Германия', 'Япония', 'Корея'], rand() % 5 + 1) AS country_of_origin,
    rand() % 24 + 1 AS warranty_period,
    [arrayElement(['курьер', 'самовывоз', 'почта'], rand() % 3 + 1)] AS delivery_options,
    [generateUUIDv4(), generateUUIDv4()] AS related_products
FROM numbers(1000000);
