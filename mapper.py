#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()

    user, date, action, item = line.split(",")

    if action == "view" or action == "purchase":
        print(f"{item}\t{action}")