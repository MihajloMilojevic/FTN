package behavioral.interpreter.booleaninterpreter;

public class NotExpression implements BooleanExpression {
	
	private BooleanExpression op;
	public NotExpression(BooleanExpression op) {
		this.op = op;
	}
	@Override
	public boolean evaluate(Context ctx) {
		return !op.evaluate(ctx);
	}

}
