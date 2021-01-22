from helpers.config import *
import subprocess

#  main
path = getDocumentsPath()
os.mkdirs(path)
URL = DOMAIN_NAME + ":" + PORT
subprocess.run(["/opt/couchbase/bin/cbexport", "json", "-c", URL, "-u", USERNAME, "-p", PASSWORD, "-b", BUCKET, "-f", "lines", "-o", path])
