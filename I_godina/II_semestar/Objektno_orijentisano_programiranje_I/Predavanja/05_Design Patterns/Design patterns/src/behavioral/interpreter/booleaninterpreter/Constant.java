package behavioral.interpreter.booleaninterpreter;

public class Constant implements BooleanExpression {

	boolean value;
	
	public Constant(boolean value) {
		this.value = value;
	}
	
	@Override
	public boolean evaluate(Context ctx) {
		return value;
	}

}
