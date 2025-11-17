def fib(n: int) -> int:

    if n <= 1:

        return n

    return fib(n - 1) + fib(n - 2)

 

def compute_fib_value():

    expansion = 20

    return fib(expansion) 

 

if __name__ == "__main__":

    print(compute_fib_value())

