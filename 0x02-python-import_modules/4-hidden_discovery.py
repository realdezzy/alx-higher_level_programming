#!/usr/bin/python3

import hidden_4


def check_hidden():
    methds = dir(hidden_4)
    for x in range(len(methds)):
        new_methd = methds[x]
        if new_methd[0] == "_":
            continue
        else:
            print(new_methd)


if __name__ == "__main__":
    check_hidden()
