module Main where

import System.IO
removenl :: [Char] -> [Char]
removenl m = init (init m)

beforea :: [Char] -> Char -> [Char]
beforea [] a = []
beforea (x:xs) a
	| x == a = []
	| otherwise = [x] ++ (beforea xs a)

aftera :: [Char] -> Char -> [Char]
aftera [] a = []
aftera x a = reverse (beforea (reverse x) a)

split :: [Char] -> (Double,Double)
split x = (read (beforea x ',') :: Double,read (aftera x ',') :: Double)

extract_hq :: [Char] -> [(Double,Double)]
extract_hq m = map split (map removenl (take 4 (lines m)))

extractage :: [Char] -> [(Double,Double)]
extractage m = map split (map removenl (tail ( tail ( tail ( tail (lines m))))))

main = do
	putStrLn "Input the number of iterations"
	n <- getLine
	csv <- readFile "data.csv"
	let hq = extract_hq csv
	let age = extractage csv
	let numit = (read n :: Int)
	putStrLn (show numit)
	return()
