def generate_prime(n):
    primes = []  # membentuk sebuah list kosong untuk menampung bilangan prima yang dihasilkan
    
    for num in range(2, n+1): #melakukan perulangan untuk bilangan dari 2 hingga n+1
        is_prime = True  #mengeset nilai awal is_prime sebagai True
        
        for i in range(2, num): #melakukan perulangan untuk bilangan dari 2 hingga bilangan num-1
            if num % i == 0:  #melakukan pengecekan jika bilangan num bisa dibagi dengan bilangan i
                is_prime = False   #mengubah nilai is_prime menjadi False
                break   #mengakhiri perulangan

        if is_prime:   #melakukan pengecekan jika is_prime masih bernilai True
            primes.append(num)   #list primes akan menambahkan bilangan num
            
    return print(primes)   #menghasilkan list primes yang berisi bilangan prima

generate_prime(1000)