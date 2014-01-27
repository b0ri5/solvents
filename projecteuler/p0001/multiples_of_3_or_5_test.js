'use strict';

const assert = require('assert');
const multiples_of_3_or_5 = require('./multiples_of_3_or_5');

describe('multiples_of_3_or_5', function() {
  describe('#sum_divisors()', function() {
    it('should be exclusive', function() {
      assert.equal(0, multiples_of_3_or_5.sum_divisors(3, 3, 5));
      assert.equal(3, multiples_of_3_or_5.sum_divisors(4, 3, 5));
      assert.equal(3, multiples_of_3_or_5.sum_divisors(5, 3, 5));
      assert.equal(8, multiples_of_3_or_5.sum_divisors(6, 3, 5));
    });
    it('should solve small example', function() {
      assert.equal(23, multiples_of_3_or_5.sum_divisors(10, 3, 5));
    });
    it('should solve large problem', function() {
      assert.equal(233168, multiples_of_3_or_5.sum_divisors(1000, 3, 5));
    });
  });
});
