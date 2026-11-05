#!/usr/bin/env python3

import sys

current_item = None
views = 0
purchases = 0

for line in sys.stdin:
    line = line.strip()
    item, action = line.split('\t')

    if current_item == item:

        if action == "view":
            views += 1
        elif action == "purchase":
            purchases += 1

    else:

        if current_item:
            rate = purchases / views if views > 0 else 0
            print("%s\t%s"  % (current_item, rate))

        current_item = item
        views = 0
        purchases = 0

        if action == "view":
            views += 1
        elif action == "purchase":
            purchases += 1

if current_item:
    rate = purchases / views if views > 0 else 0
    print("%s\t%s"  % (current_item, rate))