# Oh! A wild Pokemon appeared!

Here you will find a general purpose project to test Apache Kafka functionalities.
In order to make it easy to use, everything runs with Docker.

# Modules

## Consumer
Here you will find an ad-hoc data streaming producer.
It takes randomly pokemons from a full list of them (pokedex.json) , add some attributes and finally send all to a Kafka
topic.

## Producer
Kafka consumer linked to the previous Kafka producer.

To facilitate future analysis, upcoming data is stored a postgres database.

## Query
Necessary queries to set up our postgres schema and table.

# How to run it at home

1st run in terminal:
```
docker-compose up
```

Once Docker containers are ready. Execute consumer container (bash mode).
```
docker-compose exec consumer bash
```

At consumer container, run in terminal our kafka consumer python script and see what happens.
```
python3 kafka_consumer.py
```
