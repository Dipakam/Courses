word3digit :: [Char] -> [Char]
word2digit :: [Char]  -> [Char]
string2int :: [Char] -> Int
index :: Char -> [Char] -> Int
index x y
    | x == (head y ) = 0
    | otherwise = 1 + (index x (tail y))
string2intchar :: Char -> Int
string2intchar a = index a ['0'..'9']
string2intrec :: Int -> [Char] -> Int
string2intrec a [] = a
string2intrec a b = string2intrec (10*a + (index (head b) ['0'..'9'])) (tail b)
string2int a = string2intrec 0 a


word2digit i
    | i == "00" = ""
    | i == "10" = "ten"
    | i == "11" = "eleven"
    | i == "12" = "twleve"
    | i == "13" = "thirteen"
    | i == "14" = "forteen"| x == "000" = ""
    | (tail x) == "00" = (worddigi (string2intchar (x !! 0))) ++ " hundread"
    | not ((x!!0) == '0')  = (worddigi (string2intchar (x !! 0))) ++ " hundread and " ++ (word2digit (tail x))
    | (x !! 0 ) == '0' =  (word2digit (tail x))
    | i == "15" = "fifteen"
    | i == "16" = "sixteen"
    | i == "17" = "seventeen"
    | i == "18" = "eighteen"
    | i == "19" = "nineteen"
    | (i !! 0)== '2' = "twenty " ++ (worddigi (string2int (tail i)))
    | (i !! 0)== '3' = "thirty " ++ (worddigi (string2int (tail i)))
    | (i !! 0)== '4' = "fourty " ++ (worddigi (string2int (tail i)))
    | (i !! 0)== '5' = "fifty " ++ (worddigi (string2int (tail i)))
    | (i !! 0)== '6' = "sixty " ++ (worddigi (string2int (tail i)))
    | (i !! 0)== '7' = "seventy " ++ (worddigi (string2int (tail i)))
    | (i !! 0)== '8' = "eighty " ++ (worddigi (string2int (tail i)))
    | (i !! 0)== '9' = "ninety " ++ (worddigi (string2int (tail i)))
    | (i !! 0)== '0' = (worddigi (string2int (tail i)))
worddigi :: Int -> [Char]
worddigi i
    | i == 0 = ""
    | i == 1 = "one"
    | i == 2 = "two"
    | i == 3 = "three"
    | i == 4 = "four"
    | i == 5 = "five"
    | i == 6 = "six"
    | i == 7 = "seven"
    | i == 8 = "eight"
    | i == 9 = "nine"
word3digit x
    | x == "000" = ""
    | (tail x) == "00" = (worddigi (string2intchar (x !! 0))) ++ " hundread"
    | not ((x!!0) == '0')  = (worddigi (string2intchar (x !! 0))) ++ " hundread and " ++ (word2digit (tail x)) 
    | (x !! 0 ) == '0' =  (word2digit (tail x))
word3digitnew :: [Char] -> Bool -> [Char]
issingledigit :: [Char] -> Bool
issingledigit x
    | (string2int x) < 20 = True
    | (x !! 2) == 0 = True
    | otherwise = False
word3digitnew x y
    | (y && (issingledigit x)) = " and" ++ (word3digit x)
    | otherwise = word3digit x
split3 :: [Char] -> [[Char]]
split3 xs
    | xs == "0" = ["000"]
    | xs == "" = []
    | (length xs) == 1 = [("00" ++ xs)]
    | (length xs) == 2 = [("0" ++ xs)]
    | (length xs) >= 3 = (split3 (map (xs !!) [0..((length xs)-4)]))++[(reverse (take 3 (reverse xs)))]
word2string :: [[Char]] -> [Char]
word3digitbuff ::  Int ->Int -> [Char]
word3digitbuff x y
    | x == 1 = ""
    | y == 0 = "."
    | y == 1 = " thousand,"
    | y == 2 = " million,"
    | y == 3 = " billion,"
    | y == 4 = " trillion,"
iszero :: [Char] -> Int
iszero xs 
    | (string2int xs ) == 0 = 1
    | otherwise = 0
word2string xs
    | (length xs) == 0 = ""
    | otherwise = word3digit (head xs) ++ (word3digitbuff (iszero (head xs)) ((length xs)-1)) ++ (word2string (tail xs))
convert2string :: Int -> [Char]
convert2string x = word2string (split3 (show x))
convert :: Int -> [Char]
convert x
    | (last (convert2string x)) == ',' = init (convert2string x)
    | otherwise = convert2string x
