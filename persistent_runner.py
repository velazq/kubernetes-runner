import os
import cfg
import celery
import docker
import tempfile


RUNNER_IMAGE = 'alvelazq/kubernetes-runner' # Must have python3 in path
CTRL_IMAGE_NAME = 'runner-ctrl'


app = celery.Celery(broker=cfg.get_broker(), backend=cfg.get_backend())


@app.task
def run(task_id, source_code):
    f = tempfile.NamedTemporaryFile(mode='w', dir='/tmp/data', suffix='.py')
    f.write(source_code)
    f.flush()
    client = docker.from_env()
    logs = client.containers.run(image=RUNNER_IMAGE, command=['python3', f.name], 
        volumes_from=[CTRL_IMAGE_NAME], remove=True)
    return {'task_id': task_id, 'stdout': logs.decode()}
