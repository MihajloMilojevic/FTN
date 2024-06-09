package behavioral.interpreter.booleaninterpreter;

public class OrExpression implements BooleanExpression {

	private BooleanExpression op1;
	private BooleanExpression op2;

	public OrExpression(BooleanExpression op1, BooleanExpression op2) {
		this.op1 = op1;
		this.op2 = op2;
	}
	
	@Override
	public boolean evaluate(Context ctx) {
		return op1.evaluate(ctx) || op2.evaluate(ctx);
	}

}
