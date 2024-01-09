import json
import random
from confluent_kafka import Producer
import time

# Kafka Topic
topic_name = 'pokemon'


# Test Pokemon names
# pokemons = ["Bulbasaur", "Charmander", "Squirtle", "Pikachu", "Jigglypuff", "Snorlax", "Mewtwo", "Eevee"]

def read_file(path):
    with open(path, 'r') as f:
        data = json.load(f)
    return data


def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


# Start kafka producer
producer = Producer({'bootstrap.servers': 'kafka'})


pokedex_data = read_file(path='pokedex.json')

# Send random pokemon data to pokemon topic
while True:
    pokemon_data = {
        'pokemon': random.choice(pokedex_data),
        'level': random.randint(1, 100),
        'health': random.randint(50, 100),
        'attack': random.randint(20, 50),
        'defense': random.randint(10, 30)
    }
    producer.poll(0)
    producer.produce(topic='pokemon', value=json.dumps(pokemon_data).encode('utf-8'), callback=delivery_report)

    # Just wait
    time.sleep(1)

p.flush()
