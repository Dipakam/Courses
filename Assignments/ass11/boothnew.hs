import Control.Monad

shiftright :: [Int] -> [Int]
shiftright a = init ((head a) : a)

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
adder a b = adder0 a b 0

onescomplement :: Int -> Int
onescomplement a
    | a == 0 = 1
    | otherwise = 0

twoscomplement :: [Int] -> [Int]
twoscomplement x = adder (map onescomplement x) [1]

bits_int_list :: [Char]->[Int]
bits_int_list [] = []
bits_int_list (x:xs)
    |x=='1' = [1] ++ (bits_int_list xs)
    |x=='0' = [0] ++ (bits_int_list xs)

add_zero_bits :: [Int]->Int->[Int]
add_zero_bits main 0 = main
add_zero_bits main x = (add_zero_bits main (x-1)) ++ [0]

{-multiplicand :: [Int] -> Int -> [Int]
multiplicand xs n = reverse (take n (reverse (init xs)))

multiplicand :: [Int] -> Int -> [Int]
multiplicand xs n = reverse (take n (reverse (init xs)))

leftl :: [Int] -> Int -> [Int]
leftl xs 0 = xs
leftl xs i = xs ++ [0] ++ (leftl [] (i-1))


booth :: [Int] -> [Int] -> [Int] -> Int -> Int -> Int -> [Int] -> ([Int],[Int])
booth x y xs q i n gl
    | i == n = (xs,gl ++ [-1] ++ xs ++ [-1])
    | q == (last y) = booth x (init y) xs q (i+1) n (gl ++ [-2] ++ xs ++ [-2])
    | (q == 1) && ((last y) == 0) = booth x (init y) (adder xs (leftl x (i))) 0
     (i+1) n (gl ++ [-3] ++ xs ++ [-3])
    | (q == 0) && ((last y) == 1) = booth x (init y) (adder xs (twoscomplement
(leftl x i))) 1 (i+1) n (gl ++ [-4] ++ xs ++ [-4])

multiply :: [Int] -> [Int] -> Int -> ([Int],[Int])
multiply a b n = booth a b [] 0 0 n []
-}


booth_step :: [Int]->[Int]->Int->Int->[Int]
booth_step main multiplicand qn len
    |qn==0 && (last main)==0 = (shiftright main)
    |qn==1 && (last main)==1 = (shiftright main)
    |qn==1 && (last main)==0 = shiftright (adder main (add_zero_bits multiplicand len))
    |qn==0 && (last main)==1 = shiftright (adder main (twoscomplement(add_zero_bits multiplicand len)))


final_booth_ans :: [Int]->[Int]->Int->Int->Int->[Int]
final_booth_ans main multiplicand qn len 0 = main
final_booth_ans main multiplicand qn len step = final_booth_ans (booth_step main multiplicand qn len) multiplicand (last main) len (step-1)

booth_step_array :: [Int]->[Int]->Int->Int->Int->[Int]->([Int],[Int])
booth_step_array main multiplicand qn len 0 gl = (main,gl++[-1]++ main ++ [-1])
booth_step_array main multiplicand qn len step gl= booth_step_array (booth_step main multiplicand qn len) multiplicand (last main) len (step-1) (gl++[-1]++(booth_step main multiplicand qn len)++[-2]++[(last main)]++[-2]++[(step)])
