shell:
	docker compose exec python bash
create-topic:
	docker compose exec kafka kafka-topics.sh --create \
	--topic order-topic \
	--bootstrap-server localhost:9092 \
	--partitions 3 \
	--replication-factor 1
