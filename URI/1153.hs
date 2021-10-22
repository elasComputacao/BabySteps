fatorial :: Int -> Int
fatorial 0 = 1
fatorial 1 = 1
fatorial n = n * (fatorial (n - 1))

main = do
    n <- getLine
    let result = show (fatorial (read n))
    putStrLn result