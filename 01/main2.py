
#!/usr/bin/env python

from common import filename, get_line_value_02


def main():
    with open(filename, "r") as file:
        line_values = []
        for line in file:
            line_value = get_line_value_02(line)
            line_values.append(line_value)

            # Uncomment to spot check line values
            # print(line)
            # print(line_value)

        result = sum(line_values)
        print('SUM:', result)

if __name__ == "__main__":
    main()

