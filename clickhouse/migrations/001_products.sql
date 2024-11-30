CREATE TABLE IF NOT EXISTS db_clickhouse.products (
    id              UUID                                COMMENT 'Уникальный идентификатор продукта',

    name            String                              COMMENT 'Название продукта',
    category        String                              COMMENT 'Категория продукта',
    brand           String                              COMMENT 'Бренд продукта',
    price           Decimal(18, 2)                      COMMENT 'Цена продукта',
    discount        Decimal(5, 2)                       COMMENT 'Скидка на продукт (в процентах)',
    stock_quantity  Int32                               COMMENT 'Количество товара на складе',
    is_available    Boolean                             COMMENT 'Доступность продукта',
    tags            Array(String)                       COMMENT 'Теги продукта',

    rating          Float32                             COMMENT 'Рейтинг продукта (от 0 до 5)',
    reviews_count   Int32                               COMMENT 'Количество отзывов о продукте',
    vendor_code     String                              COMMENT 'Артикул продукта',
    description     String                              COMMENT 'Описание продукта',

    created_at      DateTime    DEFAULT now()           COMMENT 'Дата создания',
    updated_at      DateTime                            COMMENT 'Дата изменения',
    is_delete       Boolean     DEFAULT FALSE           COMMENT 'Объект удален',

    INDEX idx_id id TYPE bloom_filter GRANULARITY 8192,
    INDEX idx_name  name  TYPE bloom_filter GRANULARITY 8192
) ENGINE = ReplacingMergeTree()
PARTITION BY
    toYYYYMM(created_at)
ORDER BY
    (id, created_at);

--     attributes      Nested (name String, value String)  COMMENT 'Пользователь, создавший строку',
