import Data.List(sortBy)
import Data.Function(on)
import GHC.OldList
type Poly = [(Float,Int)]
mySort :: Ord b => [(a, b)] -> [(a, b)]
mySort = sortBy (flip compare `on` snd)
freq :: [Char] -> [(Char,Int)]
freqlet :: Char -> [Char] -> [Char]
freqcap :: [Char] -> [(Char,Int)]
freqlet a [] = []
freqlet a xs = [y | y <- xs , y == a ]
freq a = [(x,Prelude.length (freqlet x a)) | x <- ['a' .. 'z']]
freqcap a = [(x,Prelude.length (freqlet x a)) | x <- ['A'..'Z']]
mapfreq :: [Char] -> [Char]
mapfreq a = map fst (mySort (freq a))
mapfreqcap :: [Char] -> [Char]
mapfreqcap a = map fst (mySort (freqcap a))

index :: Char -> [Char] -> Int
index x y
    | x == (head y ) = 0
    | otherwise = 1 + (index x (tail y))
replace :: Char -> [Char] -> [Char] -> Char
replacecap :: Char -> [Char] -> [Char] -> Char
replace x y z = y !! (index x z)
replacecap x y z = y !! (index x z)
encode :: [Char] -> [Char] -> [Char] ->[Char] -> [Char] -> [Char]
encode [] x y z w = []
encode x y z w v
    | Prelude.elem (head x) ['a'..'z'] = [(replace (head x) y w)] ++ (encode (tail x) y z w v)
    | Prelude.elem (head x) ['A'..'Z'] = [(replacecap (head x) z v)] ++ (encode (tail x) y z w v)
    | otherwise = [(head x)] ++ (encode (tail x) y z w v)
permut :: Int -> [Char] -> [[Char]]
permut x [] = []
permut 0 x = [[]]
permut x a = [y ++ [z] | z <- a,y <- (permut (x-1) a),(not (Prelude.elem z y))]
permutationsof :: [Char] -> [[Char]]
permutationsof x = permut (Prelude.length x) x
takelastn :: Int -> [Char] -> [Char]
takelastn n x = reverse(take n (reverse x))
trials :: Int -> [Char] -> [[Char]]
trials x [a] = [[a]]
trials x [] = []
trials x y
    | x == 0 = permutationsof y
    | otherwise = [m ++ n | let m = (take x y) ,n <- (permutationsof (takelastn ((Prelude.length y) - x) y))] ++ trials (x-1) y
cipher :: [Char] -> [[Char]]
cipher [] = []
cipher x = [(encode x y z w v)|let w =(mapfreq x),let v = (mapfreqcap x),y <- (trials 25 "etaoinshrdlcumwfgypbvkjxqz"),z<- (trials 25 "TSAMCINBRPEDHWLOFYGJUKVQXZ")]
decodedwords :: [[Char]] -> [[[Char]]]
decodedwords x = [(words y)| y <- x]


{- Dictionary part -}

dictionary = ["hi","bye"]

correct_count :: [[Char]]->Int
correct_count [] = 0
correct_count (x:xs)
     |(GHC.OldList.elem (x) dictionary) = (1 + (correct_count xs))
     |otherwise = (correct_count xs)

percentage_correct_gt_eighty :: [[[Char]]] -> [[Char]]
percentage_correct_gt_eighty [] = []
percentage_correct_gt_eighty (x:xs)
   | (5*(correct_count x)) > (4*(Prelude.length x))  = x
   | otherwise = (percentage_correct_gt_eighty xs)
