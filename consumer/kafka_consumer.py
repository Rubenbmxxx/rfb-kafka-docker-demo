from confluent_kafka import Consumer
import time
import json
# from datetime import datetime
import psycopg2


def store_pokemon(pokemon, level, health, attack, defense):
    sql = """
    INSERT INTO pokedex.random_appears(pokemon, level, health, attack, defense)
    VALUES ( %s, %s, %s, %s, %s );
    """

    cur.execute(sql, (pokemon, level, health, attack, defense))
    conn.commit()


conn = psycopg2.connect(
    database="postgresdb",
    host="postgres",
    user="postgres",
    password="postgres",
    port="5432"
)
cur = conn.cursor()

consumer = Consumer({
    'bootstrap.servers': 'kafka',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['pokemon'])

while True:
    message = consumer.poll(1.0)

    if message is None:
        continue
    if message.error():
        print("Consumer error: {}".format(message.error()))
        continue

    message_value = message.value()
    json_string = message_value.decode('utf-8')
    data = json.loads(json_string)

    # print('Received message: {}'.format(message.value().decode('utf-8')))
    print('Received message: {}'.format(message.value()))
    # print('Pokemon: ' + data.get('pokemon'))
    store_pokemon(pokemon=data.get('pokemon'),
                  level=data.get('level'),
                  health=data.get('health'),
                  attack=data.get('attack'),
                  defense=data.get('defense'))

    time.sleep(5)

consumer.close()
