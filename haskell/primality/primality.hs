import Data.List

isPrime :: Int -> Bool
isPrime 1 = False
isPrime n = (!! 1) (factors n) == 1

factors :: Int -> [Int]
factors 0 = []
factors n = nub (a ++ reverse (fact a) ++ [1])
  where
    a = factors' n
    fact (x : xs) = map (x `div`) xs

factors' :: Int -> [Int]
factors' n = [a | (a, b) <- zip (map (n `div`) [1 .. s]) [1 .. s], a * b == n]
  where
    s = floor $ sqrt $ fromIntegral n


-- main = do
--   n <- read <$> getLine :: IO Int
--   putStr $ isPrime n
