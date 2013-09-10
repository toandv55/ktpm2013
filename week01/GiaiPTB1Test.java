package week01;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;

/**
 * This class is used to test the methods of the class GiaiPTB1
 * 
 * @author toandv55
 * @see week01.GiaiPTB1
 */
public class GiaiPTB1Test {

	/**
	 * The field for testing
	 */
	GiaiPTB1 pt;

	/**
	 * Initializes an object of the class GiaiPTB1 for testing
	 * 
	 * @throws Exception
	 */
	@Before
	public void setUp() throws Exception {
		pt = new GiaiPTB1();
	}

	/**
	 * Test-case 1 : input a = 1.0 and b = 1.0, expected output is -1.0
	 */
	@Test
	public void testGiaiPT() {
		assertEquals(pt.giaiPT(1f, 1f), -1f, 0f);
	}

	/**
	 * Test-case 2 : input a = 10.0 and b = -90.0, expected output is 9.0
	 */
	@Test
	public void testGiaiPT1() {
		assertEquals(pt.giaiPT(10f, -90f), 9f, 0f);
	}
}
