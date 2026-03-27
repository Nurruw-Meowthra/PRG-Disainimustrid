from random import randint

class Generator:
    def numgen(self, count):
        return [randint(1, 9) for i in range(count)]

class Splitter:
    def split(self, numgen):
        size = len(numgen)
        matrix = []
        matrix.extend(numgen)

        for x in range(size):
            col = []
            for y in range(size):
                row = numgen[y][x]
                col.append(row)
            matrix.append(col)

        d1 = []
        d2 = []
        for x in range(size):
            for y in range(size):
                if x == y:
                    d1.append(matrix[y][x])
        matrix.append(d1)

        for x in range(size):
            yMIN1 = size - x - 1
            d2.append(numgen[x][yMIN1])
        matrix.append(d2)

        return matrix

class Verifier:
    def verify(self, matrix):
        firstrow = sum(matrix[0])
        for i in range(1, len(matrix)):
            sumr = sum(matrix[i])
            if firstrow != sumr:
                return False
        return True

class MagicSquareGenerator:
    def generate(self, size):
        generator = Generator()
        splitter = Splitter()
        verify = Verifier()
        count = size*size
        GenerationTimes = 0

        while True:
            random_num = generator.numgen(count)
            GenerationTimes += 1

            square = []
            
            for i in range(0, len(random_num), size):
                square.append(random_num[i : i + size])
            
            parts = splitter.split(square)
            if verify.verify(parts):
                print(f"Times Generated: {GenerationTimes}")
                return square

gen = MagicSquareGenerator()
magic_square = gen.generate(3)

print("Maagiline ruut on leitud:")
for row in magic_square:
    print(row)