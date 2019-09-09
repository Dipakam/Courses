let array = "etaoinshrdlcumwfgypbvkjxqz"
let array1 = zip [1..26] ['a'..'z']
mapping :: [Char] -> Char -> Char
--mapping xs x = [ (fst tup) | tup <- (zip xs [1..26]),(snd tup)==(snd tup1),tup1 <- index,(fst tup1)==x]
mapping xs x = xs !! ([(fst tup )| tup <- array1,(snd tup)== x]!!0)
 
