# start docker compose
docker compose up -d
# docker compose down
docker compose down
# extract skaila
tar -xvzf sakila-db.tar.gz
# import schema
docker exec -i 7af644ad8199 mysql --user root --password=dupa  < /home/x/dockercompose/mariadb/sakila-db/sakila-schema.sql
# import data
docker exec -i 7af644ad8199 mysql --user root --password=dupa  < /home/x/dockercompose/mariadb/sakila-db/sakila-data.sql
# insert
insert into  actor ( first_name, last_name ) values ('Michal', 'Sadura');
# decribe table
desc actor;
# backup
docker exec 7af644ad8199 /usr/bin/mysqldump -u root --password=dupa sakila > /home/x/dockercompose/mariadb/sakilabck.sql
# restore
docker exec -i 7af644ad8199 sh -c 'exec mysql -uroot -pdupa sakila' < /home/x/dockercompose/mariadb/sakilabck.sql
