package samples;

import static com.google.common.truth.Truth.assertThat;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

@RunWith(JUnit4.class)
public class FortyTwoTest {
  private final FortyTwo fortyTwo = new FortyTwo();

  @Test
  public void fortyTwoReturnsFortyTwo() {
    assertThat(fortyTwo.fortyTwo()).isEqualTo(42);
  }
}
