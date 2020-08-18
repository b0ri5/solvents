module Projecteuler.P0001.MultiplesOfThreeOrFiveSpec where
import Test.Hspec

import Projecteuler.P0001.MultiplesOfThreeOrFive

main :: IO ()
main = hspec $ do
  describe "multSum" $ do
    it "should solve small example" $
      multSum 10 `shouldBe` 23
    it "should solve large problem" $
      multSum 1000 `shouldBe` 233168
