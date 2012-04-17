import pika
import MySQLdb as mdb
import setconnect as sc


class Server(object):
    """Describes server functions"""
    def __init__(self):
        """Make connect to RabbitMQ server using pika"""
        con0 = sc.Connect()
        self.konnekt = mdb.connect(
                         con0.mhost, con0.user, con0.passwd, con0.base)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                 host=con0.rhost))

        self.channel = self.connection.channel()

        self.channel.queue_declare(queue='rpc_queue')

        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(self.on_request, queue='rpc_queue')

    def cut(self, x):
        """Format string. Delete """
        x = x.strip("\n()L,ZY'")
        return(x)


    def insert(self, msg):
        """Put new task to MySQL db"""
        t = msg.lstrip(" '")
        t = t.rstrip()
        cur = self.konnekt.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS\
                    Jobs(Id INT PRIMARY KEY AUTO_INCREMENT,\
                    Task VARCHAR(25),\
                    Time TIMESTAMP)")
        cur.execute("INSERT INTO Jobs(Task) VALUES('%s')" %\
                     (t))


    def last_added_id_request(self):
        """Return id of last task added to MySQL db"""
        cur = self.konnekt.cursor()
        cur.execute("SELECT Id FROM Jobs")
        res = cur.fetchall()
        key = str(res[-1])
        return (key)


    def task_stat_request(number):
        """Return task type by number from MySQL db"""
        num = int(number)
        cur = self.konnekt.cursor()
        cur.execute("SELECT Task FROM Jobs")
        res = cur.fetchall()
        key = str(res[num - 1])
        return (key)


    def on_request(self, ch, method, props, body):
        """Handle incoming message from RabbitMQ server"""
        key = body[2]
        newmsg = self.cut(body)
        self.response = ''
        if  key == 'Z':
            self.insert(newmsg)
            self.response += self.cut(self.last_added_id_request())
        elif key == 'Y':
            self.response += self.cut(self.task_stat_request(newmsg))
        self.channel.basic_publish(exchange='',
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(
                            correlation_id=props.correlation_id),
                         body=str(self.response))
        self.channel.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == "__main__":
    server = Server()
    print " Server ready. If you want to stop server please press Ctrl+C"
    try:
        server.channel.start_consuming()
    except:
        print " \n Server stopped manually"
        server.connection.close()
