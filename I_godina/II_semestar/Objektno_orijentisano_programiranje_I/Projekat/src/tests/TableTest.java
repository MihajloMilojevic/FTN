package tests;

import static org.junit.jupiter.api.Assertions.assertDoesNotThrow;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.fail;

import java.util.ArrayList;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import database.Table;
import exceptions.DuplicateIndexException;
import exceptions.NoElementException;
import models.RoomType;

class TableTest {

	private Table<RoomType> table;


	@BeforeEach
	void setUp() throws Exception {
		table = new Table<RoomType>("room_types", new RoomType());
		table.addIndex("name");
	}

	@AfterEach
	void tearDown() throws Exception {
		table = null;
	}

	@Test
	void testGetRows() {
		try {
			RoomType roomType1 = new RoomType("1", "Room Type 1", 1);
			table.insert(roomType1);
			RoomType roomType2 = new RoomType("2", "Room Type 2", 2);
			table.insert(roomType2);
			RoomType roomType3 = new RoomType("3", "Room Type 3", 3);
			table.insert(roomType3);
			RoomType roomType4 = new RoomType("4", "Room Type 4", 4);
			table.insert(roomType4);
			RoomType roomType5 = new RoomType("5", "Room Type 5", 5);
			table.insert(roomType5);

			ArrayList<RoomType> roomTypes = table.getRows();
			assertNotNull(roomTypes, "Result is null");
			assertEquals(5, roomTypes.size(), "Result size is not 5");
			assertTrue(roomTypes.contains(roomType1), "Result does not contain roomType1");
			assertTrue(roomTypes.contains(roomType2), "Result does not contain roomType2");
			assertTrue(roomTypes.contains(roomType3), "Result does not contain roomType3");
			assertTrue(roomTypes.contains(roomType4), "Result does not contain roomType4");
			assertTrue(roomTypes.contains(roomType5), "Result does not contain roomType5");

		} catch (Exception e) {
			fail("Failed to insert data");
		}
	}

	@Test
	void testInsert() {
		assertTrue(table.getRows().isEmpty(), "Table is not empty");
		RoomType roomType = new RoomType("1", "Room Type 1", 1);

		assertDoesNotThrow(() -> table.insert(roomType), "Failed to insert roomType");

		assertFalse(table.getRows().isEmpty(), "Table is empty");
		assertEquals(1, table.getRows().size(), "Table size is not 1");
		assertTrue(table.getRows().contains(roomType), "Table does not contain roomType");
		RoomType roomType2 = new RoomType("2", "Room Type 2", 2);
		assertDoesNotThrow(() -> table.insert(roomType2), "Failed to insert roomType2");
		assertEquals(2, table.getRows().size(), "Table size is not 2");
		assertTrue(table.getRows().contains(roomType2), "Table does not contain roomType2");
		RoomType roomType2Agin = new RoomType("2", "Room Type 2", 3);
		assertThrows(DuplicateIndexException.class, () -> table.insert(roomType2Agin),
				"Failed to throw DuplicateIndexException");
		assertEquals(2, table.getRows().size(), "Table size is not 2");
		assertTrue(table.getRows().contains(roomType2), "Table does not contain roomType2");
	}

	@Test
	void testDelete() {
		try {
			RoomType roomType1 = new RoomType("1", "Room Type 1", 1);
			table.insert(roomType1);
			RoomType roomType2 = new RoomType("2", "Room Type 2", 2);
			table.insert(roomType2);
			RoomType roomType3 = new RoomType("3", "Room Type 3", 3);
			table.insert(roomType3);
			RoomType roomType4 = new RoomType("4", "Room Type 4", 4);
			table.insert(roomType4);
			RoomType roomType5 = new RoomType("5", "Room Type 5", 5);
			table.insert(roomType5);

			assertTrue(table.getRows().size() == 5, "Table size is not 5");
			assertTrue(table.getRows().contains(roomType1), "Table does not contain roomType1");
			assertTrue(table.getRows().contains(roomType2), "Table does not contain roomType2");
			assertTrue(table.getRows().contains(roomType3), "Table does not contain roomType3");
			assertTrue(table.getRows().contains(roomType4), "Table does not contain roomType4");
			assertTrue(table.getRows().contains(roomType5), "Table does not contain roomType5");

			assertEquals(5, table.select(r -> !r.isDeleted()).size(), "Some rows are deleted");

			assertDoesNotThrow(() -> table.delete(roomType1), "Failed to delete roomType1");
			assertTrue(roomType1.isDeleted(), "roomType1 is not deleted");
			assertEquals(4, table.select(r -> !r.isDeleted()).size(), "Size is not 4");

			assertDoesNotThrow(() -> table.delete(roomType2), "Failed to delete roomType2");
			assertTrue(roomType2.isDeleted(), "roomType2 is not deleted");
			assertEquals(3, table.select(r -> !r.isDeleted()).size(), "Size is not 3");

			assertDoesNotThrow(() -> table.delete(roomType3), "Failed to delete roomType3");
			assertTrue(roomType3.isDeleted(), "roomType3 is not deleted");
			assertEquals(2, table.select(r -> !r.isDeleted()).size(), "Size is not 2");

			assertDoesNotThrow(() -> table.delete(roomType4), "Failed to delete roomType4");
			assertTrue(roomType4.isDeleted(), "roomType4 is not deleted");
			assertEquals(1, table.select(r -> !r.isDeleted()).size(), "Size is not 1");

			assertDoesNotThrow(() -> table.delete(roomType5), "Failed to delete roomType5");
			assertTrue(roomType5.isDeleted(), "roomType5 is not deleted");
			assertEquals(0, table.select(r -> !r.isDeleted()).size(), "All rows are not deleted");

		} catch (Exception e) {
			fail("Failed to insert data");
		}
	}

	@Test
	void testDeleteSelectCondition() {
		try {
			RoomType roomType1 = new RoomType("1", "Room Type 1", 1);
			table.insert(roomType1);
			RoomType roomType2 = new RoomType("2", "Room Type 2", 2);
			table.insert(roomType2);
			RoomType roomType3 = new RoomType("3", "Room Type 3", 3);
			table.insert(roomType3);
			RoomType roomType4 = new RoomType("4", "Room Type 4", 4);
			table.insert(roomType4);
			RoomType roomType5 = new RoomType("5", "Room Type 5", 5);
			table.insert(roomType5);

			assertTrue(table.getRows().size() == 5, "Table size is not 5");
			assertTrue(table.getRows().contains(roomType1), "Table does not contain roomType1");
			assertTrue(table.getRows().contains(roomType2), "Table does not contain roomType2");
			assertTrue(table.getRows().contains(roomType3), "Table does not contain roomType3");
			assertTrue(table.getRows().contains(roomType4), "Table does not contain roomType4");
			assertTrue(table.getRows().contains(roomType5), "Table does not contain roomType5");

			assertDoesNotThrow(() -> table.delete(r -> r.getId().equals("1")), "Failed to delete roomType1");
			assertTrue(roomType1.isDeleted(), "roomType1 is not deleted");
			assertEquals(4, table.select(r -> !r.isDeleted()).size(), "Size is not 4");

			assertDoesNotThrow(() -> table.delete(r -> r.getId().equals("2")), "Failed to delete roomType2");
			assertTrue(roomType2.isDeleted(), "roomType2 is not deleted");
			assertEquals(3, table.select(r -> !r.isDeleted()).size(), "Size is not 3");

			assertDoesNotThrow(() -> table.delete(r -> r.getId().equals("3")), "Failed to delete roomType3");
			assertTrue(roomType3.isDeleted(), "roomType3 is not deleted");
			assertEquals(2, table.select(r -> !r.isDeleted()).size(), "Size is not 2");

			assertDoesNotThrow(() -> table.delete(r -> r.getId().equals("4")), "Failed to delete roomType4");
			assertTrue(roomType4.isDeleted(), "roomType4 is not deleted");
			assertEquals(1, table.select(r -> !r.isDeleted()).size(), "Size is not 1");

			assertDoesNotThrow(() -> table.delete(r -> r.getId().equals("5")), "Failed to delete roomType5");
			assertTrue(roomType5.isDeleted(), "roomType5 is not deleted");
			assertEquals(0, table.select(r -> !r.isDeleted()).size(), "All rows are not deleted");

			RoomType roomType6 = new RoomType("6", "Room Type 6", 6);
			table.insert(roomType6);
			assertEquals(1, table.select(r -> !r.isDeleted()).size(), "Size is not 1");
			assertDoesNotThrow(() -> table.delete(r -> ((RoomType) r).getName().startsWith("Room Type")),
					"Failed to delete roomType6");
			assertTrue(roomType6.isDeleted(), "roomType6 is not deleted");
		} catch (Exception e) {
			fail("Failed to insert data");
		}
	}

	@Test
	void testDeleteById() {
		try {
			RoomType roomType1 = new RoomType("1", "Room Type 1", 1);
			table.insert(roomType1);
			RoomType roomType2 = new RoomType("2", "Room Type 2", 2);
			table.insert(roomType2);
			RoomType roomType3 = new RoomType("3", "Room Type 3", 3);
			table.insert(roomType3);
			RoomType roomType4 = new RoomType("4", "Room Type 4", 4);
			table.insert(roomType4);
			RoomType roomType5 = new RoomType("5", "Room Type 5", 5);
			table.insert(roomType5);

			assertTrue(table.getRows().size() == 5, "Table size is not 5");
			assertTrue(table.getRows().contains(roomType1), "Table does not contain roomType1");
			assertTrue(table.getRows().contains(roomType2), "Table does not contain roomType2");
			assertTrue(table.getRows().contains(roomType3), "Table does not contain roomType3");
			assertTrue(table.getRows().contains(roomType4), "Table does not contain roomType4");
			assertTrue(table.getRows().contains(roomType5), "Table does not contain roomType5");

			assertEquals(5, table.select(r -> !r.isDeleted()).size(), "Some rows are deleted");

			assertDoesNotThrow(() -> table.deleteById("1"), "Failed to delete roomType1");
			assertTrue(roomType1.isDeleted(), "roomType1 is not deleted");
			assertEquals(4, table.select(r -> !r.isDeleted()).size(), "Size is not 4");

			assertDoesNotThrow(() -> table.deleteById("2"), "Failed to delete roomType2");
			assertTrue(roomType2.isDeleted(), "roomType2 is not deleted");
			assertEquals(3, table.select(r -> !r.isDeleted()).size(), "Size is not 3");

			assertDoesNotThrow(() -> table.deleteById("3"), "Failed to delete roomType3");
			assertTrue(roomType3.isDeleted(), "roomType3 is not deleted");
			assertEquals(2, table.select(r -> !r.isDeleted()).size(), "Size is not 2");

			assertDoesNotThrow(() -> table.deleteById("4"), "Failed to delete roomType4");
			assertTrue(roomType4.isDeleted(), "roomType4 is not deleted");
			assertEquals(1, table.select(r -> !r.isDeleted()).size(), "Size is not 1");

			assertDoesNotThrow(() -> table.deleteById("5"), "Failed to delete roomType5");
			assertTrue(roomType5.isDeleted(), "roomType5 is not deleted");
			assertEquals(0, table.select(r -> !r.isDeleted()).size(), "All rows are not deleted");

		} catch (Exception e) {
			fail("Failed to insert data");
		}
	}

	@Test
	void testDeleteByIndex() {
		try {
			RoomType roomType1 = new RoomType("1", "Room Type 1", 1);
			table.insert(roomType1);
			RoomType roomType2 = new RoomType("2", "Room Type 2", 2);
			table.insert(roomType2);
			RoomType roomType3 = new RoomType("3", "Room Type 3", 3);
			table.insert(roomType3);
			RoomType roomType4 = new RoomType("4", "Room Type 4", 4);
			table.insert(roomType4);
			RoomType roomType5 = new RoomType("5", "Room Type 5", 5);
			table.insert(roomType5);

			assertTrue(table.getRows().size() == 5, "Table size is not 5");
			assertTrue(table.getRows().contains(roomType1), "Table does not contain roomType1");
			assertTrue(table.getRows().contains(roomType2), "Table does not contain roomType2");
			assertTrue(table.getRows().contains(roomType3), "Table does not contain roomType3");
			assertTrue(table.getRows().contains(roomType4), "Table does not contain roomType4");
			assertTrue(table.getRows().contains(roomType5), "Table does not contain roomType5");

			assertEquals(5, table.select(r -> !r.isDeleted()).size(), "Some rows are deleted");
			assertDoesNotThrow(() -> table.deleteByIndex("name", "Room Type 1"), "Failed to delete roomType1");
			assertTrue(roomType1.isDeleted(), "roomType1 is not deleted");
			assertEquals(4, table.select(r -> !r.isDeleted()).size(), "Size is not 4");

			assertDoesNotThrow(() -> table.deleteByIndex("name", "Room Type 2"), "Failed to delete roomType2");
			assertTrue(roomType2.isDeleted(), "roomType2 is not deleted");
			assertEquals(3, table.select(r -> !r.isDeleted()).size(), "Size is not 3");

			assertDoesNotThrow(() -> table.deleteByIndex("id", "3"), "Failed to delete roomType3");
			assertTrue(roomType3.isDeleted(), "roomType3 is not deleted");
			assertEquals(2, table.select(r -> !r.isDeleted()).size(), "Size is not 2");

			assertDoesNotThrow(() -> table.deleteByIndex("id", "4"), "Failed to delete roomType4");
			assertTrue(roomType4.isDeleted(), "roomType4 is not deleted");
			assertEquals(1, table.select(r -> !r.isDeleted()).size(), "Size is not 1");

			assertDoesNotThrow(() -> table.deleteByIndex("name", "Room Type 5"), "Failed to delete roomType5");
			assertTrue(roomType5.isDeleted(), "roomType5 is not deleted");
			assertEquals(0, table.select(r -> !r.isDeleted()).size(), "All rows are not deleted");

		} catch (Exception e) {
			fail("Failed to insert data");
		}
	}

	@Test
	void testSelect() {
		try {
			RoomType roomType1 = new RoomType("1", "Room Type 1", 1);
			table.insert(roomType1);
			RoomType roomType2 = new RoomType("2", "Room Type 2", 2);
			table.insert(roomType2);
			RoomType roomType3 = new RoomType("3", "Room Type 3", 3);
			table.insert(roomType3);
			RoomType roomType4 = new RoomType("4", "Room Type 4", 4);
			table.insert(roomType4);
			RoomType roomType5 = new RoomType("5", "Room Type 5", 5);
			table.insert(roomType5);

			assertTrue(table.getRows().size() == 5, "Table size is not 5");
			assertTrue(table.getRows().contains(roomType1), "Table does not contain roomType1");
			assertTrue(table.getRows().contains(roomType2), "Table does not contain roomType2");
			assertTrue(table.getRows().contains(roomType3), "Table does not contain roomType3");
			assertTrue(table.getRows().contains(roomType4), "Table does not contain roomType4");
			assertTrue(table.getRows().contains(roomType5), "Table does not contain roomType5");

			assertEquals(5, table.select(r -> !r.isDeleted()).size(), "Some rows are deleted");

			assertEquals(1, table.select(r -> r.getId().equals("1")).size(), "Size is not 1");
			assertEquals(1, table.select(r -> ((RoomType) r).getName().equals("Room Type 1")).size(), "Size is not 1");

			assertEquals(1, table.select(r -> r.getId().equals("2")).size(), "Size is not 1");
			assertEquals(1, table.select(r -> ((RoomType) r).getName().equals("Room Type 2")).size(), "Size is not 1");

			assertEquals(1, table.select(r -> r.getId().equals("3")).size(), "Size is not 1");
			assertEquals(1, table.select(r -> ((RoomType) r).getName().equals("Room Type 3")).size(), "Size is not 1");

			assertEquals(1, table.select(r -> r.getId().equals("4")).size(), "Size is not 1");
			assertEquals(1, table.select(r -> ((RoomType) r).getName().equals("Room Type 4")).size(), "Size is not 1");

			assertEquals(1, table.select(r -> r.getId().equals("5")).size(), "Size is not 1");
			assertEquals(1, table.select(r -> ((RoomType) r).getName().equals("Room Type 5")).size(), "Size is not 1");

			assertEquals(0, table.select(r -> r.getId().equals("6")).size(), "Size is not 0");
			assertEquals(0, table.select(r -> ((RoomType) r).getName().equals("Room Type 6")).size(), "Size is not 0");

			assertEquals(0, table.select(r -> r.getId().equals("7")).size(), "Size is not 0");
			assertEquals(0, table.select(r -> ((RoomType) r).getName().equals("Room Type 7")).size(), "Size is not 0");

			assertEquals(roomType1, table.select(r -> r.getId().equals("1")).get(0), "Result is not roomType1");
			assertEquals(roomType1, table.select(r -> ((RoomType) r).getName().equals("Room Type 1")).get(0),
					"Result is not roomType1");

			assertEquals(roomType2, table.select(r -> r.getId().equals("2")).get(0), "Result is not roomType2");
			assertEquals(roomType2, table.select(r -> ((RoomType) r).getName().equals("Room Type 2")).get(0),
					"Result is not roomType2");

			assertEquals(roomType3, table.select(r -> r.getId().equals("3")).get(0), "Result is not roomType3");
			assertEquals(roomType3, table.select(r -> ((RoomType) r).getName().equals("Room Type 3")).get(0),
					"Result is not roomType3");

			assertEquals(roomType4, table.select(r -> r.getId().equals("4")).get(0), "Result is not roomType4");
			assertEquals(roomType4, table.select(r -> ((RoomType) r).getName().equals("Room Type 4")).get(0),
					"Result is not roomType4");

			assertEquals(roomType5, table.select(r -> r.getId().equals("5")).get(0), "Result is not roomType5");
			assertEquals(roomType5, table.select(r -> ((RoomType) r).getName().equals("Room Type 5")).get(0),
					"Result is not roomType5");

		} catch (Exception e) {
			fail("Failed to insert data");
		}
	}

	@Test
	void testSelectById() {
		try {
			RoomType roomType1 = new RoomType("1", "Room Type 1", 1);
			table.insert(roomType1);
			RoomType roomType2 = new RoomType("2", "Room Type 2", 2);
			table.insert(roomType2);
			RoomType roomType3 = new RoomType("3", "Room Type 3", 3);
			table.insert(roomType3);
			RoomType roomType4 = new RoomType("4", "Room Type 4", 4);
			table.insert(roomType4);
			RoomType roomType5 = new RoomType("5", "Room Type 5", 5);
			table.insert(roomType5);

			assertTrue(table.getRows().size() == 5, "Table size is not 5");
			assertTrue(table.getRows().contains(roomType1), "Table does not contain roomType1");
			assertTrue(table.getRows().contains(roomType2), "Table does not contain roomType2");
			assertTrue(table.getRows().contains(roomType3), "Table does not contain roomType3");
			assertTrue(table.getRows().contains(roomType4), "Table does not contain roomType4");
			assertTrue(table.getRows().contains(roomType5), "Table does not contain roomType5");

			assertEquals(5, table.select(r -> !r.isDeleted()).size(), "Some rows are deleted");

			assertEquals(roomType1, table.selectById("1"), "Result is not roomType1");
			assertEquals(roomType2, table.selectById("2"), "Result is not roomType2");
			assertEquals(roomType3, table.selectById("3"), "Result is not roomType3");
			assertEquals(roomType4, table.selectById("4"), "Result is not roomType4");
			assertEquals(roomType5, table.selectById("5"), "Result is not roomType5");

		} catch (Exception e) {
			fail("Failed to insert data");
		}
	}

	@Test
	void testSelectByIndex() {
		try {
			RoomType roomType1 = new RoomType("1", "Room Type 1", 1);
			table.insert(roomType1);
			RoomType roomType2 = new RoomType("2", "Room Type 2", 2);
			table.insert(roomType2);
			RoomType roomType3 = new RoomType("3", "Room Type 3", 3);
			table.insert(roomType3);
			RoomType roomType4 = new RoomType("4", "Room Type 4", 4);
			table.insert(roomType4);
			RoomType roomType5 = new RoomType("5", "Room Type 5", 5);
			table.insert(roomType5);

			assertTrue(table.getRows().size() == 5, "Table size is not 5");
			assertTrue(table.getRows().contains(roomType1), "Table does not contain roomType1");
			assertTrue(table.getRows().contains(roomType2), "Table does not contain roomType2");
			assertTrue(table.getRows().contains(roomType3), "Table does not contain roomType3");
			assertTrue(table.getRows().contains(roomType4), "Table does not contain roomType4");
			assertTrue(table.getRows().contains(roomType5), "Table does not contain roomType5");

			assertEquals(5, table.select(r -> !r.isDeleted()).size(), "Some rows are deleted");

			assertEquals(roomType1, table.selectByIndex("name", "Room Type 1"), "Result is not roomType1");
			assertEquals(roomType2, table.selectByIndex("name", "Room Type 2"), "Result is not roomType2");
			assertEquals(roomType3, table.selectByIndex("name", "Room Type 3"), "Result is not roomType3");
			assertEquals(roomType4, table.selectByIndex("name", "Room Type 4"), "Result is not roomType4");
			assertEquals(roomType5, table.selectByIndex("name", "Room Type 5"), "Result is not roomType5");
			assertNull(table.selectByIndex("name", "Room Type 6"), "Result is not null");
			assertNull(table.selectByIndex("name", "Room Type 7"), "Result is not null");
			
			assertEquals(roomType1, table.selectByIndex("id", "1"), "Result is not roomType1");
			assertEquals(roomType2, table.selectByIndex("id", "2"), "Result is not roomType2");
			assertEquals(roomType3, table.selectByIndex("id", "3"), "Result is not roomType3");
			assertEquals(roomType4, table.selectByIndex("id", "4"), "Result is not roomType4");
			assertEquals(roomType5, table.selectByIndex("id", "5"), "Result is not roomType5");
			assertNull(table.selectByIndex("id", "6"), "Result is not null");
			assertNull(table.selectByIndex("id", "7"), "Result is not null");
			

		} catch (Exception e) {
			fail("Failed to insert data");
		}
	}

	@Test
	void testUpdate() {
		try {
			RoomType roomType1 = new RoomType("1", "Room Type 1", 1);
			table.insert(roomType1);
			RoomType roomType2 = new RoomType("2", "Room Type 2", 2);
			table.insert(roomType2);
			RoomType roomType3 = new RoomType("3", "Room Type 3", 3);
			table.insert(roomType3);
			RoomType roomType4 = new RoomType("4", "Room Type 4", 4);
			table.insert(roomType4);
			RoomType roomType5 = new RoomType("5", "Room Type 5", 5);
			table.insert(roomType5);

            assertTrue(table.getRows().size() == 5, "Table size is not 5");
            assertTrue(table.getRows().contains(roomType1), "Table does not contain roomType1");
            assertTrue(table.getRows().contains(roomType2), "Table does not contain roomType2");
            assertTrue(table.getRows().contains(roomType3), "Table does not contain roomType3");
            assertTrue(table.getRows().contains(roomType4), "Table does not contain roomType4");
            assertTrue(table.getRows().contains(roomType5), "Table does not contain roomType5");

            assertEquals(5, table.select(r -> !r.isDeleted()).size(), "Some rows are deleted");

            RoomType roomType1Updated = new RoomType("1", "Room Type 1 Updated", 10);
            assertDoesNotThrow(() -> table.update(roomType1Updated), "Failed to update roomType1");
            assertEquals(roomType1Updated, table.selectById("1"), "Result is not roomType1Updated");

            RoomType roomType2Updated = new RoomType("2", "Room Type 2 Updated", 20);
            assertDoesNotThrow(() -> table.update(roomType2Updated), "Failed to update roomType2");
            assertEquals(roomType2Updated, table.selectById("2"), "Result is not roomType2Updated");

            RoomType roomType3Updated = new RoomType("3", "Room Type 3 Updated", 30);
            assertDoesNotThrow(() -> table.update(roomType3Updated), "Failed to update roomType3");
            assertEquals(roomType3Updated, table.selectById("3"), "Result is not roomType3Updated");
            
            RoomType roomType4Updated = new RoomType("4", "Room Type 4 Updated", 40);
            assertDoesNotThrow(() -> table.update(roomType4Updated), "Failed to update roomType4");
            assertEquals(roomType4Updated, table.selectById("4"), "Result is not roomType4Updated");
            
            RoomType roomType5Updated = new RoomType("5", "Room Type 5 Updated", 50);
            assertDoesNotThrow(() -> table.update(roomType5Updated), "Failed to update roomType5");
            assertEquals(roomType5Updated, table.selectById("5"), "Result is not roomType5Updated");
            
            RoomType roomType6 = new RoomType("6", "Room Type 6", 6);
            assertThrows(NoElementException.class, () -> table.update(roomType6), "Failed to throw NoElementException");
            assertEquals(5, table.getRows().size(), "Table size is not 5");
            assertFalse(table.getRows().contains(roomType6), "Table contains roomType6");
            
            
		} catch (Exception e) {
			fail("Failed to insert data");
		}
	}

	@Test
	void testClear() {
		try {
			RoomType roomType1 = new RoomType("1", "Room Type 1", 1);
			table.insert(roomType1);
			RoomType roomType2 = new RoomType("2", "Room Type 2", 2);
			table.insert(roomType2);
			RoomType roomType3 = new RoomType("3", "Room Type 3", 3);
			table.insert(roomType3);
			RoomType roomType4 = new RoomType("4", "Room Type 4", 4);
			table.insert(roomType4);
			RoomType roomType5 = new RoomType("5", "Room Type 5", 5);
			table.insert(roomType5);

			assertTrue(table.getRows().size() == 5, "Table size is not 5");
			assertTrue(table.getRows().contains(roomType1), "Table does not contain roomType1");
			assertTrue(table.getRows().contains(roomType2), "Table does not contain roomType2");
			assertTrue(table.getRows().contains(roomType3), "Table does not contain roomType3");
			assertTrue(table.getRows().contains(roomType4), "Table does not contain roomType4");
			assertTrue(table.getRows().contains(roomType5), "Table does not contain roomType5");


			assertDoesNotThrow(() -> table.clear(), "Failed to clear table");
			assertTrue(table.getRows().isEmpty(), "Table is not empty");
			assertEquals(0, table.getRows().size(), "Table size is not 0");
			
			assertDoesNotThrow(() -> table.insert(roomType1), "Failed to insert roomType1");
			assertDoesNotThrow(() -> table.insert(roomType2), "Failed to insert roomType2");
			assertDoesNotThrow(() -> table.insert(roomType3), "Failed to insert roomType3");
			assertDoesNotThrow(() -> table.insert(roomType4), "Failed to insert roomType4");
			assertDoesNotThrow(() -> table.insert(roomType5), "Failed to insert roomType5");

		} catch (Exception e) {
			fail("Failed to insert data");
		}
	}

}