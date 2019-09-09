mymap :: (a -> b) -> [a] -> [b]
mymap f xs = foldl (\y x -> y ++ [(f x)]) [] xs
myfilter :: (a -> Bool) -> [a] -> [a]
myfilter f xs = foldl (\y x -> if (f x) then y++[x] else y) [] xs 
