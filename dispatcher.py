from __future__ import print_function
import os
import re
import sys
from one_off_runner import run


def get_files(folder, pattern):
    return (os.path.abspath(os.path.join(dirpath, filename))
            for (dirpath, dirnames, filenames) in os.walk(folder)
            for filename in filenames
            if re.search(pattern, filename))

def dispatch(filepath):
    with open(filepath, 'r') as f:
        return run.delay(filepath, f.read())


if len(sys.argv) < 3:
    print('Usage: dispatcher.py <oneoff|persistent> <folder1> [folder2 ... folderN]')
    sys.exit(1)

if sys.argv[1] == 'persistent':
    from persistent_runner import run
else:
    from one_off_runner import run

results = [dispatch(f) for d in sys.argv[1:] for f in get_files(d, '.py$')]

[print(r.get()) for r in results]
