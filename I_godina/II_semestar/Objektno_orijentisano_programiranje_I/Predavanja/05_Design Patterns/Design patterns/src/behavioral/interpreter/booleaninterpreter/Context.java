package behavioral.interpreter.booleaninterpreter;

import java.util.HashMap;
import java.util.Map;

public class Context {
	Map<BooleanExpression, Boolean> expressions;
	
	public Context() {
		expressions = new HashMap<BooleanExpression, Boolean>();
	}
	public boolean lookup(BooleanExpression expr) {
		return expressions.get(expr);
	}
	
	public void assign(VariableExpression expr, boolean value) {
		expressions.put(expr, value);
	}
	
}
