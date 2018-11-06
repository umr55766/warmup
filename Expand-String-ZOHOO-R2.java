import java.io.*; 
import java.util.*;

public class ExpandExpression {
    public static void main(String []args) {
        Stack<String> stack = new Stack<String>();
        String input = "a(b(c){2}){2}d", temp, peek;
        int i = 0, c = 0;
        
        while (i < input.length()) {
            if (input.charAt(i) == '{') {
                temp = "";
                peek = stack.pop();
                c = 0;
                while (c < (int)(input.charAt(i+1)-48)) {
                    temp += peek;
                    c++;
                }
                stack.push(temp);
                i += 2;
            } else if (input.charAt(i) == ')') {
                temp = "";
                while (!stack.isEmpty()) {
                    if (stack.peek().equals("(")) {
                        stack.pop();
                        break;
                    } else {
                        temp = stack.pop() + temp;
                    }
                }
                stack.push(temp);
            } else {
                stack.push(input.charAt(i)+"");
            }
            i++;
        }
        temp = "";
        while (!stack.isEmpty()) {
           temp = stack.pop() + temp;
        }
        System.out.println(temp);
    }
}
