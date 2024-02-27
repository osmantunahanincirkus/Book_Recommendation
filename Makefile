start:
	docker-compose up -d --build --force-recreate vue
	sleep 10
	make restore_mysql
	echo 'Sistem başlatıldı. http://localhost:9777'

stop:
	docker-compose down --rmi all -v
#	docker system prune -a -f --all
#	docker system prune -a -f --volumes

restore_mysql:
	docker cp ./deps/kitap_oneri-dump.sql kitap-oneri-mysql:/kitap_oneri-dump.sql
	docker exec kitap-oneri-mysql /bin/sh -c "mysql -u root -prootpass kitap-oneri < /kitap_oneri-dump.sql"

dump_mysql:
	docker exec kitap-oneri-mysql /bin/sh -c "mysqldump -u root -prootpass kitap-oneri > /kitap_oneri-dump.sql"
	docker cp kitap-oneri-mysql:/kitap_oneri-dump.sql ./deps/kitap_oneri-dump.sql