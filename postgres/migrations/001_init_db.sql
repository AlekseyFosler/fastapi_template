CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS public.users (
    user_id              UUID                        PRIMARY KEY          DEFAULT uuid_generate_v4(),
    full_name            TEXT                                    NOT NULL,
    mobile_phone         VARCHAR(20)                 UNIQUE      NOT NULL,
    created_at           TIMESTAMP WITHOUT TIME ZONE             NOT NULL DEFAULT current_timestamp,
    updated_at           TIMESTAMP WITHOUT TIME ZONE             NOT NULL DEFAULT current_timestamp
);

CREATE UNIQUE INDEX idx_user_mobile_phone ON public.users (mobile_phone);
