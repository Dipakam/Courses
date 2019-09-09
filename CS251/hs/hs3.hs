module Main where
main = do
	putStrLn "To find the first fibonacci numbers , Enter n"
	n <- getLine
	--putStrLn (if n<0 then "N should be greater than zero" else (square n))
        square :: Int -> Int 
        let square x  = x * x
	putStrLn (if n<0 then "N should be greater than zero" else (square n))
	putStrLn "This is it"
