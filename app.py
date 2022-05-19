from flask import Flask  , request ,redirect , jsonify
import threading
from time import sleep
from json import dumps
from kafka import KafkaProducer
import os
app = Flask(__name__)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

def function_attente(aa,bb):

    for e in range(bb):
        o= aa + '   ' + str (bb) + ' Temps Restants '

        data = {o : bb-e }
        sleep(1)
        producer.send('numb', value=data)
        print(data)

@app.route('/post', methods=['POST'])
def add_parametre():
    d=request.get_json()
    a = d["a"]
    b = d["b"]
    print(d)

    download_thread = threading.Thread(target=function_attente, args=(a,b,))
    download_thread.start()
    return  jsonify(d)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")