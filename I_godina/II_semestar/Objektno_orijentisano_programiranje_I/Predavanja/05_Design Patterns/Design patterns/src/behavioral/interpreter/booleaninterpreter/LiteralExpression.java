package behavioral.interpreter.booleaninterpreter;

public class LiteralExpression implements BooleanExpression {

	boolean value;
	
	public LiteralExpression(boolean value) {
		this.value = value;
	}
	
	@Override
	public boolean evaluate(Context ctx) {
		return value;
	}

}
