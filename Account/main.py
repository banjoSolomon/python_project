from Account.sevensegmentdisplay import SevenSegmentDisplay


def main():
    display = SevenSegmentDisplay()
    for digit in range(10):
        display.set_digit(digit)

        current_segments = display.get_segment()
        print(f"Digit: {digit}")
        print(f"Segments: {current_segments}")
        print()


if __name__ == "__main__":
    main()
