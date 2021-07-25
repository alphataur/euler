import glob
import os

def resolve_dir(fname):
    if fname == "clearner.py":
        return fname
    idx = fname.split(".")[0]
    res = ""
    for i in range(3-len(idx)):
        res += "0"
    res += idx
    res += ".py"
    return res

files = glob.glob("*.py")
ofiles = map(resolve_dir, files)



for o, f in zip(files, ofiles):
    os.rename(o, f)
