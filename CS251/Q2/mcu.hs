import System.IO

distance :: (Double,Double) -> (Double,Double) -> Double
distance (l1,t1) (l2,t2) = (l2-l1)*(l2-l1) + (t2-t1)*(t2-t1)

mindisthq :: (Double,Double) -> [(Double,Double)] -> Int
mindisthq (l,t) hq
    |(minimum (map (distance (l,t)) hq) == distance (l,t) (hq !! 0)) = 1
    |(minimum (map (distance (l,t)) hq) == distance (l,t) (hq !! 1)) = 2
    |(minimum (map (distance (l,t)) hq) == distance (l,t) (hq !! 2)) = 3
    |(minimum (map (distance (l,t)) hq) == distance (l,t) (hq !! 3)) = 4

listtostring :: [(Double,Double)] -> [Char]
listtostring xs = foldl (\acc x -> acc ++ (show (fst x)) ++ ","++(show (snd x))++"\n") [] xs

agents :: [(Double,Double)] -> [(Double,Double)] -> [(Double,Double,Int)]
agents ag hq = foldl (\acc x -> acc ++ [((fst x),(snd x),(mindisthq x hq))] ) [] ag

du :: Int -> Double
du a = read (show a) :: Double

hqn :: (Double,Double,Int) -> Int
hqn (x,y,z) = z

lat :: (Double,Double,Int) -> Double
lat (x,y,z) = x

lon :: (Double,Double,Int) -> Double
lon (x,y,z) = y
agperhq :: [(Double,Double,Int)]->Int -> [(Double,Double,Int)]
agperhq agent x = filter (\y -> (hqn y) == x) agent

sumlat :: [(Double,Double,Int)] -> Double
sumlat xs = sum (map lat xs)

sumlon :: [(Double,Double,Int)] -> Double
sumlon xs = sum (map lon xs)

averagecor :: [(Double,Double,Int)] -> (Double,Double)
averagecor agent = (((sumlat agent)/(du (length agent))),((sumlon agent)/(du (length agent))))

new_hq :: [(Double,Double)] -> [(Double,Double,Int)] -> [(Double,Double)]
new_hq hq agent = map (averagecor . agperhq agent) [1..4]

iteratea :: [(Double,Double)] -> [(Double,Double)] -> [(Double,Double)]
iteratea age hq = new_hq hq (agents age hq)

iterations :: [(Double,Double)] -> [(Double,Double)] -> Int -> [(Double,Double)]
iterations hq age n
        | (n == 0) = hq
        | otherwise = iterations (iteratea age hq) age (n-1)

final_ans :: [(Double,Double)] -> [(Double,Double)] -> Int -> [(Double,Double,Int)]
final_ans hq age n = agents age (iterations hq age (n-1))

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
split x = ((read (beforea x ',') :: Double),(read (aftera x ',') :: Double))

splits :: [Char] -> ([Char],[Char])
splits x = ((beforea x ',') , (aftera x ','))

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
--        putStrLn "Input the number of iterations"
--        n <- getLine
--        csv <- readFile "data.csv"
--        let hq = extract_hq csv
--        let age = extractage csv
--        let numit = (read n :: Int)
  putStrLn (show (final_ans hq age numit))
--  print(numit)
--  print((map removenl (lines csv)))
--  print (map split (map removenl (lines csv)))
  return()
