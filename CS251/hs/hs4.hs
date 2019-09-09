module Main where 
import System.IO
main = do
	putStrLn "This is my first output files"
	writeFile "output.txt" ['A'..'Z']
