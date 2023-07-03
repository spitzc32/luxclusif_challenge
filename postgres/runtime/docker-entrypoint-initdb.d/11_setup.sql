create role prod_admin with login encrypted password 'prod_admin';

--grant all privileges to role prod_admin;

alter user prod_admin with superuser;
alter user prod_admin with createdb;
alter user prod_admin with createrole;

\c postgres;

create schema if not exists commerce;

create table if not exists commerce.products
(
    uniq_id                 text primary key not null,
    crawl_timestamp         timestamp not null,
    product_url             text,
    product_name            varchar(200) not null,
    product_category_tree   text[] not null,
    pid                     text,
    retail_price            text,
    discounted_price        varchar(200) not null,
    image                   text [],
    is_FK_Advantage_product boolean,
    product_rating          varchar(100),
    overall_rating          varchar(100),
    brand                   text,
    product_specifications  JSON
);