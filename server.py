import sys
import string
import pika
import ConfigParser
import MySQLdb as mdb


config = ConfigParser.RawConfigParser()
config.read('conf.cnf')
defmhost = config.get("MySQLopts", "host")
defuser = config.get("MySQLopts", "user")
defpasswd = config.get("MySQLopts", "passwd")
defbase = config.get("MySQLopts", "base")
defrhost = config.get("Rabbitopts", "host")
konnekt = mdb.connect(defmhost, defuser, defpasswd, defbase)


def cut(x):
    x = x.strip("\n()L,ZY'")
    return(x)


def insert(msg):
    t = msg.lstrip(" '")
    t = t.rstrip()
    with konnekt:
        cur = konnekt.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS\
                     Jobs(Id INT PRIMARY KEY AUTO_INCREMENT,\
                     Task VARCHAR(25),\
                     Time TIMESTAMP)")
        cur.execute("INSERT INTO Jobs(Task) VALUES('%s')" % \
                      (t))


def outg():
    with konnekt:
        cur = konnekt.cursor()
        cur.execute("SELECT Id FROM Jobs")
        res = cur.fetchall()
        key = str(res[-1])
    return (key)


def outn(number):
    num = int(number)
    with konnekt:
        cur = konnekt.cursor()
        cur.execute("SELECT Task FROM Jobs")
        res = cur.fetchall()
        key = str(res[num-1])
    return (key)

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=defrhost))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')


def on_request(ch, method, props, body):
    key = body[2]
    newmsg = cut(body)
    response = '' 
    if  key == 'Z':
        insert(newmsg)
        response += cut(outg())
    elif key == 'Y':
        response += cut(outn(newmsg))
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(
                        correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')
print " Server ready. If you want to stop server please press Ctrl+C"
try:
    channel.start_consuming()
except:
    print " \n Server stopped manually"
    connection.close()
