package test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.fail;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

import manage.StudentManager;

public class StudentMenadzerTest {

	private static StudentManager manager;
	
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
		System.out.println("setUpBeforeClass");
	}

	@AfterClass
	public static void tearDownAfterClass() throws Exception {
		System.out.println("tearDownAfterClass");
	}

	@Before
	public void setUp() throws Exception {
		System.out.println("setUp");
		manager = new StudentManager(null, null);
		
	}

	@After
	public void tearDown() throws Exception {
		System.out.println("tearDown");
	}

	@Test
	public void testAdd() { 
		assertEquals(0, manager.getStudenti().size());
		manager.add(1, "Pera", "Peric", "SV1/2023");
		assertEquals(1, manager.getStudenti().size());
		assertNotNull(manager.PronadjiStudentaPoId(1));
		
	}

}
