-- not needed because of the env POSTGRES_DB
-- create database user_auth_db;
-- use user_auth_db;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

create table user_table (
    id text NOT NULL PRIMARY KEY,
    -- id bigserial PRIMARY KEY,
    username text NOT NULL,
    email text NOT NULL,
    -- steam64id has to be clear-text or encrypted (tbd later), hashed is no option,
    -- because the user would not want to provide its steamid at every login
    -- steam64id text NOT NULL,
    is_active BOOLEAN NOT NULL,
    is_verified BOOLEAN NOT NULL,
    is_superuser BOOLEAN NOT NULL,
    hashed_password text NOT NULL
    -- last_updated_at timestamptz DEFAULT NOW() NOT NULL
);

-- test for db creation
-- insert into user_auth (salt, pw_hash) values ('krasser-salt', 'krasser-hash');
-- select * from user_auth;
