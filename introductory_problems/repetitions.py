# Repetitions
# https://cses.fi/problemset/task/1069


def main():
    string = input()
    longest_sequence = 1
    sequence_length = 1
    sequence_char = string[0]
    counter = 0
    for c in string[1:]:
        counter += 1
        if c == sequence_char:
            sequence_length += 1
        else:
            sequence_char = c
            if sequence_length > longest_sequence:
                longest_sequence = sequence_length
            sequence_length = 1

    if sequence_length > longest_sequence:
        longest_sequence = sequence_length

    print(longest_sequence)


if __name__ == '__main__':
    main()
