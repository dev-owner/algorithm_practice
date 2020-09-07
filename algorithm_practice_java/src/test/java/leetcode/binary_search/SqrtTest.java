package leetcode.binary_search;

import org.junit.Test;

import static org.assertj.core.api.Assertions.assertThat;

public class SqrtTest {

    @Test
    public void test_mySqrt() {
        assertThat(Sqrt.mySqrt(4)).isEqualTo(2);
        assertThat(Sqrt.mySqrt(8)).isEqualTo(2);
        assertThat(Sqrt.mySqrt(9)).isEqualTo(3);
        assertThat(Sqrt.mySqrt(0)).isEqualTo(0);
        assertThat(Sqrt.mySqrt(100)).isEqualTo(10);
    }
}