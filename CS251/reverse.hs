reverseString :: [Char] -> [Char]
reverseString [] = []
reverseString (x:xs) = reverseString xs ++ [x]

