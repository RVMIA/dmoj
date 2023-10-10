import Control.Monad
import Data.List

compareLikeAmt a b = compare (read (b !! 1) :: Int) (read (a !! 1) :: Int)
compareDates a b = (b !! 2) == (a !! 2)
removeDupDates = map unwords . nubBy compareDates . map words
sortInputs = map unwords . sortBy compareLikeAmt . map words
names = map (head . words)
sampleIn = ["Sanna 1 16/03", "Simon 2 16/03", "Saga 3 14/10"]
main = do
  n <- read <$> getLine :: IO Int
  bdays <- sort . names . removeDupDates . sortInputs <$> replicateM n getLine
  print $ length bdays
  putStr $ unlines bdays
