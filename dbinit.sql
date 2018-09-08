-- VERSION 1.0

-- Delete the itemcatalog db if it already exist
DROP DATABASE IF EXISTS itemcatalog;

-- Creates the itemcatalog db
CREATE DATABASE itemcatalog;

-- Creates itemcatalog user if doesn't exists, set user's password,
-- and give all privileges on itemcatalog db.
do
$body$

declare
  num_users integer;

begin
   SELECT count(*) into num_users
   FROM pg_user
   WHERE usename = 'itemcatalog';

   IF num_users = 0 THEN
      CREATE USER itemcatalog WITH PASSWORD 'uD@c1ty185!';
   END IF;
   GRANT ALL PRIVILEGES ON DATABASE itemcatalog to itemcatalog;
   ALTER DATABASE itemcatalog OWNER TO itemcatalog;
end
$body$

;

-- Show available data bases
select datname from pg_database where datistemplate = 'f';