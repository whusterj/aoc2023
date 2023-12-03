
#!/usr/bin/env python

from common import filename, get_line_value


def main():
    with open(filename, "r") as file:
        line_values = [get_line_value(line) for line in file]
        result = sum(line_values)
        print('SUM:', result)

if __name__ == "__main__":
    main()

