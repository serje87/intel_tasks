import re
import sys

SECOND_CHAR = "s"
MINUTE_CHAR = "m"
HOUR_CHAR = "h"
DAY_CHAR = "d"

MULTIPLIER = {SECOND_CHAR: 1, MINUTE_CHAR: 60, HOUR_CHAR: 60 * 60, DAY_CHAR: 60 * 60 * 24}


class InvalidArgumentError(ValueError):
    pass


def parse_line(line):
    pattern = re.compile(r"^(\d*\.?\d*)([{}{}{}{}]?)$".format(*MULTIPLIER.keys()))
    res = pattern.match(line)
    if res and line:
        value = float(res.group(1)) if res.group(1) else 1
        units = res.group(2) if res.group(2) else "s"
        seconds = float(value * MULTIPLIER[units])
        seconds = int(seconds) if seconds.is_integer() else seconds
        return seconds
    else:
        raise InvalidArgumentError("Invalid Time Delta Specifier! Got: \"{}\".".format(line))
