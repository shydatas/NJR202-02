```
git clone
```

```
uv sync
```

## 建立 docker network
```
docker network create njr20202_network
```

## MySQL
```
docker compose -f docker_compose/docker-compose-mysql.yml up -d
```

## Airflow
```
docker build -f airflow/Dockerfile -t shydatas/airflow:latest .
```

```
docker compose -f airflow/docker-compose-airflow.yml up
```

## Message Queue
```
docker build -f Dockerfile -t shydatas/data_ingestion:latest .
```

```
docker compose -f docker_compose/docker-compose-broker.yml up -d
docker compose -f docker_compose/docker-compose-producer.yml up
docker compose -f docker_compose/docker-compose-worker.yml up
```
