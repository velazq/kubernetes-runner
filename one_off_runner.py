import os
import cfg
import celery
import signal
import tempfile
import subprocess


app = celery.Celery(broker=cfg.get_broker(), backend=cfg.get_backend())


@app.task
def run(task_id, source_code):
    f = tempfile.NamedTemporaryFile(mode='w', dir='/tmp/data', suffix='.py')
    f.write(source_code)
    f.flush()
    out, err = subprocess.Popen(['python3', f.name], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    with open('/tmp/celery.pid') as pid:
        os.kill(int(pid.read()), signal.SIGTERM)
    return {'task_id': task_id, 'stdout': out.decode(), 'stderr': err.decode()}
