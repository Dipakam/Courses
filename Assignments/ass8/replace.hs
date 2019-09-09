index :: Char -> [Char] -> Int
index x y
    | x == (head y ) = 0
    | otherwise = 1 + (index x (tail y))
replace :: Char -> [Char] -> [Char] -> Char
replacecap :: Char -> [Char] -> [Char] -> Char
--dereplace :: Char -> [Char] -> Char
--dereplacecap :: Char -> [Char] -> Char
--dereplace x y = ['a' .. 'z'] !! (index x y)
--dereplacecap x y = ['A'..'Z'] !! (index x y)
replace x y z = y !! (index x z )
replacecap x y z = y !! (index x z)
encode :: [Char] -> [Char] -> [Char] ->[Char] -> [Char] -> [Char]
--subst :: [Char] -> [Char] -> [Char]
--subst [] y = []
--subst x y = [(replace (head x) y)] ++ ( subst (tail x) y)
encode [] x y z w = []
encode x y z w v
    | elem (head x) ['a'..'z'] = [(replace (head x) y w)] ++ (encode (tail x) y z w v)
    | elem (head x) ['A'..'Z'] = [(replacecap (head x) z v)] ++ (encode (tail x) y z w v)
    | otherwise = [(head x)] ++ (encode (tail x) y z w v)

