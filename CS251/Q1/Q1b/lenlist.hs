lenlist :: [a] -> Int
lenlist [] = 0
lenlist (x:xs) = 1 + (lenlist xs)
