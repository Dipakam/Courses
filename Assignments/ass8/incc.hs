incc ::[Int] -> (Int,Int) -> [Int]
incc [] (_,_) = []
incc a (1,1) = ((head a) + 1 ) : tail a
incc a (1,y) = ((head a) + 1 ) : (incc (tail a) (1,(y-1)))
incc a (x,y) = (head a) : (incc (tail a) ((x-1),(y-1)))
