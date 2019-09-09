cipher :: [Char] -> Int -> [Char]
cipher [] = []
cipher (x:xs) n = ( rotate x n):(cipher xs)
rotate :: char -> Int -> char 
rotate 
