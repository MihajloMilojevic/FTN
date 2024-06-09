package behavioral.interpreter.booleaninterpreter;

public class VariableExpression implements BooleanExpression {
	public String name;
	
	public VariableExpression(String name) {
		this.name = name;
	}
	
	@Override
	public boolean evaluate(Context ctx) {
		return ctx.lookup(this);
	}

}
