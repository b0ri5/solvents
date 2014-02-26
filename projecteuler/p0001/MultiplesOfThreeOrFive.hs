module Projecteuler.P0001.MultiplesOfThreeOrFive where

multSum :: Int -> Int
multSum n = sum threeMults + sum fiveNotThreeMults
  where
      threeMults = [3, 6..(n - 1)]
      fiveNotThreeMults = filter ((/= 0) . (`rem` 3)) [5, 10..(n - 1)]
