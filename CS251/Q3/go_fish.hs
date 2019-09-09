{-# LANGUAGE FlexibleInstances #-}
--import System.Random
import System.Environment

--instance {-# OVERLAPPING #-} Show String where
--    show = id

-- data-structures for the deck of cards
data Suit = Club | Diamond | Heart | Spade deriving (Enum, Bounded)
data Number = Ace | Two | Three | Four | Five | Six | Seven | Eight | Nine | Ten | Jack | Queen | King deriving (Enum, Bounded)
data Card = Card Suit Number  deriving (Bounded)

-- the STATE of the game:
-- the first component is the player's hand of cards
-- the second component is the computer's hand of cards
-- the third component is the remaining cards on the table 
data State = State ([Card], [Card], [Card]) deriving (Show)

instance Show Suit where
  show a = case a of
                 Club -> "\9827"
                 Diamond -> "\9830"
                 Heart -> "\9829"
                 Spade -> "\9824"

instance Show Number where
  show a = case a of
                 Ace -> "1"
                 Two -> "2"
                 Three -> "3"
                 Four -> "4"
                 Five -> "5"
                 Six -> "6"
                 Seven -> "7"
                 Eight -> "8"
                 Nine -> "9"
                 Ten -> "10"
                 Jack -> "J"
                 Queen -> "Q"
                 King -> "K"

instance Show Card where
  show (Card a b) = (show a) ++ (show b)

stringtocard :: [Char] -> Card
stringtocard x
	| x == "A" = Ace
	| x == "K" = King
	| x == "Q" = Queen
	| x == "J" = Jack
	| x == "10" = Ten
	| x == "9" = Nine
	| x == "8" = Eight
	| x == "7" = Seven
	| x == "6" = Six
	| x == "5" = Five
	| x == "4" = Four
	| x == "3" = Three
	| x == "2" = Two
shuffle :: Int -> [Card] -> [Card]
shuffle n (d:ds) = xs ++ [d] ++ ys where
                        (xs, ys) = splitAt n ds

-- returns a shuffled deck of cards
shuffled_deck :: IO [Card]
shuffled_deck = do
--        g <- getStdGen
        let deck = [ (Card s n) | s <- [Club .. Spade], n <- [Ace .. King] ]
        let ns = [1..52] --take 100000 $ randomRs (0,51) g
        let strs = foldr shuffle deck ns
        return strs

-- show logging
-- parameters:
-- arg1: initial state
-- arg2: card selected by player
-- arg3: updated state
log :: State -> Card -> State -> IO ()
log s1 c s2 = print $ "Log: " ++ (show s1) ++ (show c) ++ (show s2)

main = do
        args <- getArgs
        x <- shuffled_deck -- returns a shuffled deck of cards
        print $ take 10 x
        if (((length args) > 0) && (args!!0 == "-log")) then 
								print "Logging enabled,Enter the guess"
								newcard <- getLine
								
							else print "Logging disabled"
        
