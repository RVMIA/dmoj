pushBack :: Int -> [Int] -> [Int]
pushBack x arr = arr ++ [x]

pushFront :: Int -> [Int] -> [Int]
pushFront x arr = x : arr


pushMiddle :: Int -> [Int] -> [Int]
pushMiddle x arr = f ++ [x] ++ s
  where
    l = flip div 2 $ (+ 1) $ length arr
    tup = splitAt l arr
    f = fst tup
    s = snd tup


process :: ([String],[Int],[Int]) -> ([String], [Int], [Int])
process ([],y,z) = ([],y,z)
process (x, y, z)
  | f == "push_back" = (tail x, pushBack i y, z )
  | f == "push_middle" = (tail x, pushMiddle i y, z )
  | f == "push_front" = (tail x, pushFront i y, z )
  | otherwise = (tail x, y, z ++ [y !! i])
  where a = words $ head x 
        f = head a
        i = read $ last a :: Int


main = do
  times <- read <$> getLine :: IO Int
  ops <- sequence $ replicate times getLine 
  putStr $ unlines $ map show $ (\(_,_,x) -> x) $ (!! times) $ iterate process (ops,[],[])
