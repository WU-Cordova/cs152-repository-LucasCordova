

def next_prime_after_double(n: int) -> int:
    
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    
    next_prime = n * 2
    while not is_prime(next_prime):
        next_prime += 1
    
    return next_prime
    


def main():
    
   next_prime = next_prime_after_double(7)
   print(f"next prime after 7 is {next_prime}") 

    



if __name__ == '__main__':
    main()
