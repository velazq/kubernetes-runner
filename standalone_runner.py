import os
import celery
import tempfile


RUNNER_IMAGE = 'alvelazq/kubernetes-runner:0.1' # Must have python3 in path
CTRL_IMAGE_NAME = 'runner-ctrl'


app = celery.Celery('standalone_runner')
app.conf.update(
    broker_url=os.environ['BROKER'],
    result_backend=os.environ['BACKEND'],
)


@app.task
def run_in_container(task_id, source_code):
    f = tempfile.NamedTemporaryFile(mode='w', dir='/tmp/data', suffix='.py')
    f.write(source_code)
    f.flush()
    client = docker.from_env()
    logs = client.containers.run(image=RUNNER_IMAGE, command=['python3', f.name], 
        volumes_from=[CTRL_IMAGE_NAME], remove=True)
    return {'task_id': task_id, 'stdout': logs.decode()}
