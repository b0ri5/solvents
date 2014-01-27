package samples.p01;

import static org.hamcrest.CoreMatchers.equalTo;
import static org.junit.Assert.assertThat;

import org.junit.Test;

public class FortyTwoTest {
  private final FortyTwo fortyTwo = new FortyTwo();

  @Test
  public void testFortyTwo() {
    assertThat(fortyTwo.fortyTwo(), equalTo(42));
  }
}
