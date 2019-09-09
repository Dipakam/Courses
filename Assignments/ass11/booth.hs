shiftright :: [Int] -> [Int]
shiftright a = init ((head a) : a)

extendbits :: [Int] -> Int -> [Int]
extendbits x 0 = x
extendbits x i = [ (head x) | t <- [1..i]] ++ x
shiftleft :: [Int] -> Int -> [Int]
shiftleft x 0 = x
shiftleft x i = x ++ [0|y<- [1..i]]
sumb :: Int -> Int ->  Int -> Int
sumb a b c
    | (a+b+c) < 2 = (a+b+c)
    | otherwise = (a+b+c-2)
carry :: Int -> Int -> Int -> Int
carry a b c
    | (a+b+c) < 2 = 0
    | otherwise = 1
adder0 :: [Int] -> [Int] -> Int -> [Int]
adder0 [] [] x = []
adder0 a [] x = (adder0 (init a) [] (carry (last a) 0 x)) ++ [(sumb (last a) 0 x)]
adder0 [] b x = (adder0 [] (init b) (carry 0 (last b) x)) ++ [(sumb 0 (last b) x)]
adder0 a b c = (adder0 (init a) (init b) (carry (last a) (last b) c)) ++ [(sumb (last a) (last b) c)]
adder :: [Int] -> [Int] -> [Int]
adder [] x = x
adder x [] = x
adder a b
    | (length a) > (length b) = adder0 a (extendbits b ((length a)-(length b))) 0
    | (length a) < (length b) = adder0 (extendbits a ((length b)-(length a))) b 0
    | (length a) == (length b) = adder0 a b 0

onescomplement :: Int -> Int
onescomplement a
    | a == 0 = 1
    | otherwise = 0
twoscomplement :: [Int] -> [Int]
twoscomplement x = adder (map onescomplement x) [0,1]

accomoder :: [Int] -> Int -> [Int]
accomoder xs n = take n xs

multiplicand :: [Int] -> Int -> [Int]
multiplicand xs n = reverse (take n (reverse (init xs)))

leftl :: [Int] -> Int -> [Int]
leftl xs 0 = xs
leftl xs i = xs ++ [0] ++ (leftl [] (i-1))


booth :: [Int] -> [Int] -> [Int] -> Int -> Int -> Int -> [Int] -> ([Int],[Int])
booth x y xs q i n gl
    | i == n = (xs,gl ++ [-1] ++ xs ++ [-2] ++ [-1])
    | q == (last y) = booth x (init y) xs q (i+1) n (gl ++ [-2] ++ xs ++ [-2])
    | (q == 1) && ((last y) == 0) = booth x (init y) (adder xs (leftl x (i))) 0 (i+1) n (gl ++ [-3] ++ xs ++ [-3])
    | (q == 0) && ((last y) == 1) = booth x (init y) (adder xs (twoscomplement (leftl x i))) 1 (i+1) n (gl ++ [-4] ++ xs ++ [-4])

multiply :: [Int] -> [Int] -> Int -> ([Int],[Int])
multiply a b n = booth a b [] 0 0 n []
