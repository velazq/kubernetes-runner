import os
import celery
import tempfile
import subprocess


app = celery.Celery('runner')
app.conf.update(
    broker_url=os.environ['BROKER'],
    result_backend=os.environ['BACKEND'],
    task_acks_late=True,
    worker_prefetch_multiplier=1,
    worker_pool='solo',
    worker_concurrency=1,
)


@app.task
def run(task_id, source_code):
    f = tempfile.NamedTemporaryFile(mode='w', dir='/tmp/data', suffix='.py')
    f.write(source_code)
    f.flush()
    out, err = subprocess.Popen(['python3', f.name], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    os.system('celery control shutdown')
    return {'task_id': task_id, 'stdout': out.decode(), 'stderr': err.decode()}
