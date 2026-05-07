from rq import Worker, Queue
from redis import Redis
import os

redis_conn = Redis.from_url(os.getenv('REDIS_URL'))
queues = [Queue('ia-reconcile', connection=redis_conn)]
worker = Worker(queues, connection=redis_conn)
worker.work(with_scheduler=True)  # Auto-retries + dashboard