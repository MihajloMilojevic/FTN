package behavioral.interpreter.romandigitsintepreter;

import java.util.ArrayList;

public class Test {

	public static void main(String[] args) {

		String roman = "MCMXCVIII";
		Context context = new Context(roman);

		// Build the 'parse tree'
		ArrayList<Expression> tree = new ArrayList<Expression>();
		tree.add(new ThousandExpression());
		tree.add(new HundredExpression());
		tree.add(new TenExpression());
		tree.add(new OneExpression());

		// Interpret
		for (Expression exp : tree) {
			exp.interpret(context);
		}

		System.out.println(roman + " = "
				+ Integer.toString(context.getOutput()));
	}
}
