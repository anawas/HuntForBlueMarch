import sys

__platform = sys.platform
if __platform != "darwin":
    print("Sorry, must be run on darwin (is ") + __platform + (")")
    quit()

ver = sys.version_info
if ver.major < 3:
    print ("Sorry, must be run with Python 3.0 or higher (is %d.%d)") % (ver.major, ver.minor)
    quit()
