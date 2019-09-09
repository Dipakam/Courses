import Control.Monad

safehead :: [a] -> Maybe a
safehead [] = Nothing
safehead (x:xs) = Just x

safeinit :: [Maybe Int] -> Maybe [Maybe Int]
safeinit [] = Nothing
safeinit xs = Just (init xs)
shiftright :: Maybe [Int] -> Maybe [Maybe Int]
shiftright a
    | a == Nothing = Nothing
    | otherwise = (safeinit ((safehead a) : a))

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

numones :: [Int] -> Int
numones xs = foldl (\y x -> if x == 1 then y+1 else y) 0 xs

numzeros :: [Int] -> Int
numzeros xs = foldl (\y x -> if x == 0 then y+1 else y) 0 xs
adder :: [Int] -> [Int] -> Maybe [Int]
adder a b
    | (numones a) == (numzeros a) = Nothing
    | (numones b) == (numzeros b) = Nothing
    | otherwise = Just (adder0 a b 0)

onescomplement :: Int -> Int
onescomplement a
    | a == 0 = 1
    | otherwise = 0

twoscomplement :: [Int] -> Maybe [Int]
twoscomplement x = adder (map onescomplement x) [1]

bits_int_list :: [Char]->[Int]
bits_int_list [] = []
bits_int_list (x:xs)
    |x=='1' = [1] ++ (bits_int_list xs)
    |x=='0' = [0] ++ (bits_int_list xs)

add_zero_bits :: [Int]->Int->[Int]
add_zero_bits main 0 = main
add_zero_bits main x = (add_zero_bits main (x-1)) ++ [0]



booth_step :: [Int]->[Int]->Int->Int-> Maybe [Int]
booth_step main multiplicand qn len
    |qn==0 && (last main)==0 = (shiftright main)
    |qn==1 && (last main)==1 = (shiftright main)
    |qn==1 && (last main)==0 = shiftright (adder main (add_zero_bits multiplicand len))
    |qn==0 && (last main)==1 = shiftright (adder main (twoscomplement(add_zero_bits multiplicand len)))


final_booth_ans :: [Int]->[Int]->Int->Int->Int->[Int]
final_booth_ans main multiplicand qn len 0 = main
final_booth_ans main multiplicand qn len step = final_booth_ans (booth_step main multiplicand qn len) multiplicand (last main) len (step-1)

booth_step_array :: [Int]->[Int]->Int->Int->Int->[Int]
booth_step_array main multiplicand qn len 0 = [-1]++main ++ [-2] ++ [qn] ++ [-2] ++ [0]
booth_step_array main multiplicand qn len step =
	[-1] ++ main ++ [-2] ++ [qn] ++ [-2] ++ [step]
   ++ ( booth_step_array (booth_step main multiplicand qn len) multiplicand
	 (last main) len (step-1) )


manipulate_array :: [Int]->[Char]
manipulate_array [] = []
manipulate_array (x:xs)
   | x==1 = ['1'] ++ manipulate_array xs
   | x==(-1) = ['\n'] ++ manipulate_array xs
   | x==0 = ['0'] ++ manipulate_array xs
   | x==(-2) = [' '] ++ manipulate_array xs
   |otherwise = (show x) ++ manipulate_array xs

main = do
	putStrLn "Enter the number of bits:"
	bits<-getLine
	putStrLn "Enter the two numbers:"
	ino<-getLine
	iino<-getLine
	let noino= bits_int_list ino
	let noiino= bits_int_list iino
	let inter=add_zero_bits [] (read bits :: Int)
	let ans=booth_step_array (inter++noino) noiino 0 (read bits :: Int) (read bits :: Int)
	putStrLn (manipulate_array ans)
