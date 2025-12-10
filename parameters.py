#!/usr/bin/env python

"Command line tools and exit status"

import os
import sys

fn = sys.argv[1]


if not os.path.exists(fn):
    with open(fn, 'w') as _f:
        _f.write("New file created\n")
else:
    print("Error, the file {} already exists!".format(fn))
    sys.exit(1)

