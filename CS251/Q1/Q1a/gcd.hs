gcdm :: Int -> Int -> Int
gcdm x y
    | x > y = gcd (x-y) y
    | y > x = gcd x (y-x)
    | x == y = x
    | x == 0 = y
    | y == 0 = x
