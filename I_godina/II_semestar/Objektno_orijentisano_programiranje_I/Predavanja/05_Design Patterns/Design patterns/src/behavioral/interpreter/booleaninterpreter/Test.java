package behavioral.interpreter.booleaninterpreter;

public class Test {

	public static void main(String[] args) {
		Context ctx = new Context();
		// Varijable:
		// x = false
		// y = true
		// z <- rezultat
		// Izraz: 
		// z = (true and x) or (y and not(x))
		VariableExpression x = new VariableExpression("x");
		VariableExpression y = new VariableExpression("y");
		VariableExpression z = new VariableExpression("z");
		ctx.assign(x, new LiteralExpression(false).evaluate(ctx));
		ctx.assign(y, new LiteralExpression(true).evaluate(ctx));

		BooleanExpression expression = new OrExpression(
				new AndExpression(new LiteralExpression(true), x),
				new AndExpression(y, new NotExpression(x)));
		
		ctx.assign(z, expression.evaluate(ctx));
		
		System.out.println(z.evaluate(ctx));
		// kontrola
		boolean _x = false;
		boolean _y = true;
		boolean _z = (true && _x) || (_y && !_x); 
		System.out.println(_z);
		
	}

}
