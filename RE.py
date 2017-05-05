import re

if __name__ == "__main__":
    s = "http.org"
    m = re.match("ht+p(\S+)",s)
    print m.group(1)