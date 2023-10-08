factors x = [i | i <- [1..x], mod x i == 0]
makeList :: Int -> [Int]
makeList x = [1..x]


main = interact $ show . sum . map length . map factors . makeList . abs . read
