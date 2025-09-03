import gzip
import os

filename = "C:/Users/2261266/Downloads/hadoop-3.4.0-src.tar.gz"
with gzip.open(filename, 'rb') as f_in:
    content = f_in.read()
    with open(os.path.join('C:/Users/2261266/Downloads/hadoop-3.4.0-src', filename[:-3]).replace('tar', ''), 'wb') as out_f:
        out_f.write(content)

print("Extracted the files---")