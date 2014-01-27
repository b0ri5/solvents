'use strict'; // Required first line for all solvents *.js files

const assert = require('assert');
const fortytwo = require('./fortytwo');

describe('fortytwo', function() {
  describe('#fortytwo()', function() {
    it('should return 42', function() {
      assert.equal(42, fortytwo.fortytwo());
    });
  });
});
