module Main where 
import System.IO
main = do
	inputfrom <- readFile "input.txt"
	writeFile "output.txt" (reverse inputfrom)
	return ()
