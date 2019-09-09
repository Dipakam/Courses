data Tree = Normal Tree Int Tree | NULL deriving (Show,Eq,Ord)
addtree :: Tree -> Int
addtree NULL = 0
addtree (Normal left x right) = x + addtree left + addtree right
