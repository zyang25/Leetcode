package com.sho.hire.hw.YangZihao;

import static org.junit.Assert.assertEquals;
import org.junit.Test;
import com.sho.hire.hw.YangZihao.YangZihao;

public class TestEcalpeReserver {
	
	@Test
	public void testEcalpe() {
		
		// Empty toBeReplaced
		String t9 = YangZihao.ecalpeResrever("Hello", "", "");
		assertEquals(t9, "Hello");
		
		// Empty string
		String t8 = YangZihao.ecalpeResrever("", "", "dog");
		assertEquals(t8, "");
		
		// Empty token
		String t6 = YangZihao.ecalpeResrever("I like cats", "", "dog");
		assertEquals(t6, "cats like I");
		
		// replace one token
		String t1 = YangZihao.ecalpeResrever("I like cats", "cat", "dog");
		assertEquals(t1, "dogs like I");
		
		// replace multiple tokens 
		String t2 = YangZihao.ecalpeResrever("I like catscat", "cat", "dog");
		assertEquals(t2, "dogsdog like I");
		
		// replace word with space
		String t3 = YangZihao.ecalpeResrever("I like cats", "like cats", "hello world");
		assertEquals(t3, "world hello I");
				
		// first space last space
		String t5 = YangZihao.ecalpeResrever(" I like cats ", "cat", "dog");
		assertEquals(t5, " dogs like I ");
		
		// Multipul space
		String t7 = YangZihao.ecalpeResrever("I  like  cats", "a", "dog");
		assertEquals(t7, "cdogts  like  I");
	}
}
