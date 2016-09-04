# -*- coding: utf-8 -*-
from MetroRouteFinder.data import getRoute
import json
import sys


if __name__ == '__main__':
    print json.dumps(getRoute(sys.argv[1].decode("GBK"),
                              sys.argv[2].decode("GBK"),
                              sys.argv[3].decode("GBK")),
                     ensure_ascii=False, sort_keys=True, indent=4)
