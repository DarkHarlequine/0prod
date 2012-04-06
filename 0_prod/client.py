import random
import uuid
import pika
import setconnect as sc


class Client(object):
    """Descripes client functions"""
    def __init__(self):
        """Make connect to RabbitMQ server using pika"""
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host=con0.rhost))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        """"""
        if self.corr_id == props.correlation_id:
            self.response = body

    def job(self):
        """Generate task using random int values"""
        key = random.randint(1, 5)
        if key == 1:
            self.task = "Play a game"
        elif key == 2:
            self.task = "Play guitar"
        elif key == 3:
            self.task = "Kill all humans"
        elif key == 4:
            self.task = "Conquer this world"
        elif key == 5:
            self.task = "Drink a bottle"
        return (self.task)

    def call(self, job, mark):
        """Send message to RabbitMQ. Message contains string 'marker,task/\
        tasknumber'"""
        tcode = (mark, job)
        code = str(tcode)
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                         reply_to=self.callback_queue,
                                         correlation_id=self.corr_id,
                                         ),
                                   body=code)
        while self.response is None:
            self.connection.process_data_events()
        return str(self.response)


def marker(mark):
    """Return mark for server. Z - if we want to give new task,
       Y - if we want to view task by number"""
    s = None
    if mark == 1:
        s = 'Z'
        return (s)
    elif mark == 2:
        s = 'Y'
        return (s)

if __name__ == "__main__":
    con0 = sc.Connect()
    rpc = Client()
    print "If you want to start session press 1, if you don't press 0"
    key = int(raw_input())
    while key != 0:
        print "1. If you want to give a task press 1,\
               \n2. If you want to know task status press 2,\
               \n3. If you don't press 0"
        key = int(raw_input())
        tag = marker(key)
        if key == 1:
            work = rpc.job()
            print " [x] Requesting number"
            response = rpc.call(work, tag)
            print " [.] Task number is %s" % (response,)
        if key == 2:
            print "Print number of task"
            number = int(raw_input())
            print " [x] Requesting status"
            response = rpc.call(number, tag)
            print " [.] Task status is %s" % (response,)
    else:
            print "Session close manually"
