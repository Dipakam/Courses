fib2 :: Int -> Integer
fibo :: Integer -> Integer -> [Integer]
fibo a b = a : (fibo b (a+b))
fib2 n = (fibo 0 1) !! (n-1)
