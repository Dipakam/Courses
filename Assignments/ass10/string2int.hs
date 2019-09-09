string2int :: [Char] -> Int
index :: Char -> [Char] -> Int
index x y
    | x == (head y ) = 0
    | otherwise = 1 + (index x (tail y))
string2intrec :: Int -> [Char] -> Int
string2intrec a [] = a
string2intrec a b = string2intrec (10*a + (index (head b) ['0'..'9'])) (tail b)
string2int a = string2intrec 0 a
