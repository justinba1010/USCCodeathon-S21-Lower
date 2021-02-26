import Data.Char
main = do
    line <- getLine
    putStrLn $ changeCase (map toLower line) "upper"

changeCase :: [Char] -> [Char] -> [Char]
changeCase (x:xs) lastState 
                | xs == [] && lastState == "lower" = map toUpper [x]
                | xs == [] && lastState == "upper" = [x]
                | [x] == " " = [x] ++ (changeCase xs lastState)
                | lastState == "upper" = [x] ++ changeCase xs "lower"  
                | lastState == "lower" = [toUpper x] ++ changeCase xs "upper"
                | otherwise = [x]