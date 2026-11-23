class ProductOfNumbers:

    def __init__(self):
        # Initialize with 1 to make prefix product calculations easier
        self.prefix_products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # If we encounter a 0, reset the prefix products.
            # Any product spanning across this 0 will be 0.
            self.prefix_products = [1]
        else:
            # Append the product of the current number and the last prefix product
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k is greater than the available valid prefix products, it means
        # the sequence of the last k numbers includes at least one 0.
        if k >= len(self.prefix_products):
            return 0
            
        # The product of the last k numbers is the current total product
        # divided by the product before those k numbers.
        return self.prefix_products[-1] // self.prefix_products[-(k + 1)]