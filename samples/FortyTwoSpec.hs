module Samples.FortyTwoSpec where

import Samples.FortyTwo
import Test.Hspec

main :: IO ()
main = hspec $ do
  describe "fortytwo" $
    it "should return 42" $
      fortytwo `shouldBe` 42
