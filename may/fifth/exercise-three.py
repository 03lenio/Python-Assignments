import shutil
import gzip

with gzip.open('ian.gz', 'rb') as f_in:
    with open('ian.png', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)