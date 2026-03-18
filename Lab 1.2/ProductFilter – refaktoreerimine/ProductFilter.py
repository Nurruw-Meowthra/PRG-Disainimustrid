class BetterFilter:

    def filter(self, items, spec):
        return [item for item in items if spec.is_satisfied(item)]

    @staticmethod
    def filter_by_size(products, size):

        return [p for p in products if p.size == size]

    @staticmethod
    def filter_by_size_and_color(products, color, size):

        return [p for p in products if p.color == color and p.size == size]