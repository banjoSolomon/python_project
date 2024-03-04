class SevenSegDisplay:
    segment = [[0 for _ in range(4)] for _ in range(5)]

    @staticmethod
    def fillA():
        SevenSegDisplay.segment[0][0] = 1
        SevenSegDisplay.segment[0][1] = 1
        SevenSegDisplay.segment[0][2] = 1
        SevenSegDisplay.segment[0][3] = 1

    @staticmethod
    def fillB():
        SevenSegDisplay.segment[0][3] = 1
        SevenSegDisplay.segment[1][3] = 1
        SevenSegDisplay.segment[2][3] = 1

    @staticmethod
    def fillC():
        SevenSegDisplay.segment[2][3] = 1
        SevenSegDisplay.segment[3][3] = 1
        SevenSegDisplay.segment[4][3] = 1

    @staticmethod
    def fillD():
        SevenSegDisplay.segment[4][0] = 1
        SevenSegDisplay.segment[4][1] = 1
        SevenSegDisplay.segment[4][2] = 1
        SevenSegDisplay.segment[4][3] = 1

    @staticmethod
    def fillE():
        SevenSegDisplay.segment[2][0] = 1
        SevenSegDisplay.segment[3][0] = 1
        SevenSegDisplay.segment[4][0] = 1

    @staticmethod
    def fillF():
        SevenSegDisplay.segment[0][0] = 1
        SevenSegDisplay.segment[1][0] = 1
        SevenSegDisplay.segment[2][0] = 1

    @staticmethod
    def fillG():
        SevenSegDisplay.segment[2][0] = 1
        SevenSegDisplay.segment[2][1] = 1
        SevenSegDisplay.segment[2][2] = 1
        SevenSegDisplay.segment[2][3] = 1

    @staticmethod
    def display():
        for i in SevenSegDisplay.segment:
            for j in i:
                if j == 1:
                    print("# ", end="")
                else:
                    print("  ", end="")
            print()

    @staticmethod
    def inputValue(value):
        if len(value) > 7:
            value = value[:7]

        for i in value:
            if i not in ['0', '1']:
                raise ValueError("Input must be 0 or 1")

        for i in range(len(value)):
            bit = value[i]
            if bit == '1':
                if i == 0:
                    SevenSegDisplay.fillA()
                elif i == 1:
                    SevenSegDisplay.fillB()
                elif i == 2:
                    SevenSegDisplay.fillC()
                elif i == 3:
                    SevenSegDisplay.fillD()
                elif i == 4:
                    SevenSegDisplay.fillE()
                elif i == 5:
                    SevenSegDisplay.fillF()
                elif i == 6:
                    SevenSegDisplay.fillG()


if __name__ == "__main__":
    display = SevenSegDisplay()
    value = input("Enter binary number (up to 7 bits): ")
    display.inputValue(value)
    display.display()
