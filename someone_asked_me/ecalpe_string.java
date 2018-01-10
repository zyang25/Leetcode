package com.sho.hire.hw.YangZihao;

import java.util.Iterator;
import java.util.Scanner;
import java.util.Stack;

/**
 * @author zihaoyang
 *
 */
public class YangZihao {

	public static void main(String[] args) {
		System.out.println(ecalpeResrever("I like cats","cat","dog"));
	}
	
	// 1. replace all token in the string, O(n)
	// 2. load the string into stack, O(n)
	// 3. build the string from stack, O(n)
	// Total time complexity O(3n)
	public static String ecalpeResrever(String sen, String token, String toBeReplaced) {
		
		// If the string is empty
		if(sen.length() == 0)
			return "";
		
		// If the token is blank, return the reverse string
		if(token.length() == 0)
			return reverseString(sen);
		
		// Translate sentence and token to char array
		char[] senCharArray = sen.toCharArray();
		char[] tokenCharArray = token.toCharArray();
		
		
		int countChar = 0;
		int tokenLen = token.length();
		
		// Construct one word
		StringBuilder constructWord = new StringBuilder();
		
		// Buffer to store the match word
		StringBuilder tempConstructWord = new StringBuilder();
		
		// Result
		StringBuilder wordString = new StringBuilder();
		
		for(int i = 0; i < senCharArray.length; i++) {
			
			// Load the current char
			char currentChar = senCharArray[i];

			// Compare the current char with token
			if(currentChar == tokenCharArray[countChar]) {
				
				countChar += 1;
				// Append the match character to the buffer
				tempConstructWord.append(currentChar);
				
				// Found the token matched, append the buffer to the word we need to construct
				if(tokenLen == countChar) {
					countChar = 0;
					constructWord.append(toBeReplaced);
					tempConstructWord.setLength(0);
				}
			}else{
				// If we don't see a match, clear all counts and take the buffer to construct a word
				if(tempConstructWord.length() > 0) {
					constructWord.append(tempConstructWord);
					// Init the temporary word
					countChar = 0;
					tempConstructWord.setLength(0);
				}

				// Construct the word by current char
				constructWord.append(currentChar);
			}
			
			// If there is space, construct the word to result
			if(tempConstructWord.length() == 0 && currentChar == ' ' || (i == senCharArray.length-1)) {
				countChar = 0;
				wordString.append(constructWord.toString());
				constructWord.setLength(0);
				tempConstructWord.setLength(0);
			}
		}
		
		// Last step reverse the whole string
		return reverseString(wordString.toString());
	}
	
	// Time complexity O(2n)
	public static String reverseString(String s) {
		
		// Translate the sentence and character to array
		char[] stringArray = s.toCharArray();
		StringBuilder buffer = new StringBuilder();
		Stack<String> wordStack = new Stack<String>();
		
		// last space scenario
		boolean lastSpace = stringArray[stringArray.length-1] == ' ' ? true : false;
		
		// read the current char to buffer, if it's space, load it to stack
		// Time complexity O(n)
		for(int i = 0; i < stringArray.length; i++) {
			char currentChar = stringArray[i];
			
			if(currentChar != ' ')
				buffer.append(currentChar);
			
			if(currentChar == ' ' || i == stringArray.length-1) {
				wordStack.push(buffer.toString());
				buffer.setLength(0);
			}
				
		}
		
		StringBuilder sentence = new StringBuilder();
		int count = 0;
		int sizeOfStack = wordStack.size();
		// build a string from stack, Time complexity O(n)
		while(!wordStack.isEmpty()) {
			if(lastSpace) {
				lastSpace = false;
				sentence.append(" ");
			}
			String word = (String) wordStack.pop();
			sentence.append(word);
			
			count += 1;
			
			if(count != sizeOfStack)
				sentence.append(" ");
		}
		return sentence.toString();
	}

}
