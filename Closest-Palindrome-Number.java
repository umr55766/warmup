/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		Scanner scan = new Scanner(System.in);
		short testCases = scan.nextShort();
		while (testCases-- > 0) {
		    System.out.println(get_pallindrome_of(scan.nextLong()));
		}
	}
	
	public static String get_pallindrome_of(long num) {
	    if (num < 10) {
	        return num + "";
	    }
	    String number = (num + ""), result;
	    if (number.length() % 2 == 0) {
	        result = number.substring(0, number.length()/2) + reverse_it(number.substring(0, number.length()/2));
	    } else {
	        result = number.substring(0, number.length()/2+1) + reverse_it(number.substring(0, number.length()/2));
	    }
	    if (Long.parseLong(result) > num) {
	        if (is_pallindrome((num-(Long.parseLong(result)-num))+"")) {
	            return (num-(Long.parseLong(result)-num)) + "";
	        }
	    }
	    return result;
	}
	
	public static String reverse_it(String str) {
	    StringBuilder string = new StringBuilder(str);
	    return string.reverse().toString();
	}
	
	public static Boolean is_pallindrome(String num) {
	    StringBuilder str1 = new StringBuilder(num);
	    StringBuilder str2 = new StringBuilder(num);
	    if (str1.toString().equals(str2.reverse().toString())) {
	        return true;
	    } else {
	        return false;
	    }
	}
}
