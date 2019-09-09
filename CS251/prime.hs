prime :: Int -> Int
primes = [x|x<-[3..],null ([y|y<-[2..(ceiling (sqrt (fromIntegral x)))],((mod x y)==0)])]
prime 1 = 2
prime n = primes !! (n-2)
--To calculate nth prime use echo "prime n" | ghci prime.hs
--To output the prime numbers echo "primes" | ghci prime.hs

fib :: Int -> Integer
fibo :: Integer -> Integer -> [Integer]
fibo a b = a : (fibo b (a+b))
fib n = (fibo 0 1) !! (n-1)
--To calculate nth element in fibonacci series echo "fib n" | ghci prime.hs
--To output the fibonacci series with first two elements as a and b echo "fibo a b"|ghci prime.hs
