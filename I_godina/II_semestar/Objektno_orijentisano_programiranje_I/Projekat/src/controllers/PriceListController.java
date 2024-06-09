package controllers;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Comparator;

import app.AppState;
import database.SelectCondition;
import exceptions.DuplicateIndexException;
import exceptions.NoElementException;
import models.Model;
import models.PriceList;

public class PriceListController {

	public static ArrayList<PriceList> getPrices() {
		return AppState.getInstance().getDatabase().getPriceLists().select(new SelectCondition() {

			@Override
			public boolean check(Model row) {
				return !row.isDeleted();
			}
		});
	}

	public static ArrayList<PriceList> getPricesForPeriod(LocalDate startDate, LocalDate endDate) {
		ArrayList<PriceList> res = AppState.getInstance().getDatabase().getPriceLists().select(new SelectCondition() {
			@Override
			public boolean check(Model row) {
				PriceList priceList = (PriceList) row;
				return !priceList.isDeleted() && ((priceList.getEndDate() == null
						&& priceList.getStartDate().isBefore(startDate))
						|| (priceList.getStartDate().isBefore(endDate) && priceList.getEndDate().isAfter(startDate)));
			}
		});
		res.sort(new Comparator<PriceList>() {
			@Override
			public int compare(PriceList p1, PriceList p2) {
				return p1.getStartDate().compareTo(p2.getStartDate());
			}
		});
		return res;
	}

	public static ControllerActionStatus updatePriceList(PriceList priceList) {
		try {
			if (priceList == null || !priceList.isValid()) {
				return ControllerActionStatus.INCOPLETE_DATA;
			}
			AppState.getInstance().getDatabase().getPriceLists().update(priceList);
			return ControllerActionStatus.SUCCESS;
		} catch (Exception e) {
			return ControllerActionStatus.ERROR;
		}
	}

	public static ControllerActionStatus addPriceList(PriceList priceList) {
		try {
			if (priceList == null || !priceList.isValid()) {
				return ControllerActionStatus.INCOPLETE_DATA;
			}
			insertPriceList(priceList);
			return ControllerActionStatus.SUCCESS;
		} catch (DuplicateIndexException e) {
			e.printStackTrace();
			return ControllerActionStatus.DUPLICATE_INDEX;
		} catch (NoElementException e) {
			e.printStackTrace();
			return ControllerActionStatus.INCOPLETE_DATA;
		} catch (CloneNotSupportedException e) {
			e.printStackTrace();
			return ControllerActionStatus.ERROR;
		} catch (Exception e) {
			e.printStackTrace();
			return ControllerActionStatus.ERROR;
		}
	}

	public static ControllerActionStatus editPriceList(PriceList priceList) {
		try {
			if (priceList == null || !priceList.isValid()) {
				return ControllerActionStatus.INCOPLETE_DATA;
			}
			insertPriceList(priceList);
			return ControllerActionStatus.SUCCESS;
		} catch (DuplicateIndexException e) {
			e.printStackTrace();
			return ControllerActionStatus.DUPLICATE_INDEX;
		} catch (NoElementException e) {
			e.printStackTrace();
			return ControllerActionStatus.INCOPLETE_DATA;
		} catch (CloneNotSupportedException e) {
			e.printStackTrace();
			return ControllerActionStatus.ERROR;
		} catch (Exception e) {
			e.printStackTrace();
			return ControllerActionStatus.ERROR;
		}
	}

	public static ControllerActionStatus removePriceList(PriceList priceList) {
		try {
			if (priceList == null) {
				return ControllerActionStatus.INCOPLETE_DATA;
			}
			priceList.delete();
			AppState.getInstance().getDatabase().getPriceLists().delete(priceList);
			return ControllerActionStatus.SUCCESS;
		} catch (Exception e) {
			return ControllerActionStatus.ERROR;
		}
	}

	private static void insertPriceList(PriceList priceList)
			throws NoElementException, DuplicateIndexException, CloneNotSupportedException {
		if (priceList == null) {
			return;
		}

		// there are 2 types of pricelists:
		// 1. infinite pricelist - whose end date is null
		// 2. fixed length pricelist - whose end date is not null

		// if we try to insert a new infinite pricelist we can diferentiate 3 cases:
		// 1. there is a pricelist with the same start date so we update that pricelist
		// and delete every other pricelist after this one
		// 2. there is a pricelist with no end date that overlaps with this pricelist so
		// we end that pricelist by new pricelist's start date - 1 day
		// 3. there is a pricelist that overlaps with this pricelist so we split that
		// pricelist into two and delete every other pricelist after this one

		// if we try to insert a new fixed length pricelist we can diferentiate 3 cases:
		// 1. there is a pricelist with the same start date and same end date so we
		// update that pricelist
		// 2. we are inserting a pricelist that overlaps with a pricelist with no end
		// date so we end that pricelist by new pricelist's start date - 1 day
		// insert the new pricelist and insert a new infinite pricelist that starts from
		// new pricelist's end date + 1 day
		// we had:
		// |-----------------|--------------------------------------------------------------->
		// we try:
		// |-----------------|-----------------|-----------|--------------------------------->

		ArrayList<PriceList> priceLists;
		// this is an infinite pricelist
		if (priceList.getEndDate() == null) {
			// check if there is a pricelist with the same start date

			priceLists = AppState.getInstance().getDatabase().getPriceLists().select(new SelectCondition() {
				@Override
				public boolean check(Model row) {
					PriceList pl = (PriceList) row;
					return !pl.isDeleted() && pl.getStartDate().equals(priceList.getStartDate());
				}
			});
			if (priceLists.size() > 0) {
				// there is a pricelist with the same start date
				// so we update that pricelist
				PriceList pl = priceLists.get(0);
				pl.update(priceList);
				AppState.getInstance().getDatabase().getPriceLists().update(pl);
				// now we need to delete every other pricelist after this one
				priceLists = AppState.getInstance().getDatabase().getPriceLists().select(new SelectCondition() {
					@Override
					public boolean check(Model row) {
						PriceList pl = (PriceList) row;
						return !pl.isDeleted() && pl.getStartDate().isAfter(priceList.getStartDate());
					}
				});
				for (PriceList pld : priceLists) {
					AppState.getInstance().getDatabase().getPriceLists().delete(pld);
				}
				return; // there is nothing else to do
			}

			// check if this pricelist overlaps with pricelist with no end date
			priceLists = AppState.getInstance().getDatabase().getPriceLists().select(new SelectCondition() {
				@Override
				public boolean check(Model row) {
					PriceList pl = (PriceList) row;
					return !pl.isDeleted() && pl.getEndDate() == null
							&& pl.getStartDate().isBefore(priceList.getStartDate());
				}
			});
			if (priceLists.size() > 0) {
				// there is a pricelist with no end date that overlaps with this pricelist
				// so we end that pricelist by new pricelist's start date - 1 day
				PriceList pl = priceLists.get(0);
				pl.setEndDate(priceList.getStartDate().minusDays(1));
				AppState.getInstance().getDatabase().getPriceLists().update(pl);
				// and we insert the new pricelist
				AppState.getInstance().getDatabase().getPriceLists().insert(priceList);
				return; // there is nothing else to do
			}

			// find a pricelist whose start date is before this pricelist's start date and
			// (end date is null or end date is after this pricelist's start date)
			priceLists = AppState.getInstance().getDatabase().getPriceLists().select(new SelectCondition() {
				@Override
				public boolean check(Model row) {
					PriceList pl = (PriceList) row;
					return !pl.isDeleted() && pl.getStartDate().isBefore(priceList.getStartDate())
							&& (pl.getEndDate() == null || pl.getEndDate().isAfter(priceList.getStartDate()));
				}
			});
			if (priceLists.size() > 0) {
				// there is a pricelist that overlaps with this pricelist
				// so we split that pricelist into two
				PriceList pl = priceLists.get(0);
				pl.setEndDate(priceList.getStartDate().minusDays(1));
				AppState.getInstance().getDatabase().getPriceLists().update(pl);
				// we find all the pricelist that start after this pricelist and delete them
				priceLists = AppState.getInstance().getDatabase().getPriceLists().select(new SelectCondition() {
					@Override
					public boolean check(Model row) {
						PriceList pl = (PriceList) row;
						return !pl.isDeleted() && pl.getStartDate().isAfter(priceList.getStartDate());
					}
				});
				for (PriceList pld : priceLists) {
					AppState.getInstance().getDatabase().getPriceLists().delete(pld);
				}
				// and we insert the new pricelist
				AppState.getInstance().getDatabase().getPriceLists().insert(priceList);
				return; // there is nothing else to do
			}

			// there is no pricelist that overlaps with this pricelist
			// so we just insert it
			AppState.getInstance().getDatabase().getPriceLists().insert(priceList);
			return; // there is nothing else to do

		}
		// infinite pricelist check is done

		// this is a fixed length pricelist

		// check if this pricelist starts the same day as a pricelist with no end date

		priceLists = AppState.getInstance().getDatabase().getPriceLists().select(new SelectCondition() {
			@Override
			public boolean check(Model row) {
				PriceList pl = (PriceList) row;
				return !pl.isDeleted() && pl.getEndDate() == null && pl.getStartDate().equals(priceList.getStartDate());
			}
		});
		if (priceLists.size() > 0) {
			// there is a pricelist with no end date that starts the same day as this
			// pricelist
			// so we move that pricelist to start the day after this pricelist ends
			PriceList pl = priceLists.get(0);
			pl.setStartDate(priceList.getEndDate().plusDays(1));
			AppState.getInstance().getDatabase().getPriceLists().update(pl);
			// and we insert the new pricelist
			AppState.getInstance().getDatabase().getPriceLists().insert(priceList);
			return; // there is nothing else to do
		}
		// check if this pricelist overlaps with a pricelist with no end date
		priceLists = AppState.getInstance().getDatabase().getPriceLists().select(new SelectCondition() {
			@Override
			public boolean check(Model row) {
				PriceList pl = (PriceList) row;
				return !pl.isDeleted() && pl.getEndDate() == null && pl.getStartDate().isBefore(priceList.getEndDate());
			}
		});
		if (priceLists.size() > 0) {
			// there is a pricelist with no end date that overlaps with this pricelist
			// so we end that pricelist by new pricelist's start date - 1 day
			PriceList pl = priceLists.get(0);
			pl.setEndDate(priceList.getStartDate().minusDays(1));
			AppState.getInstance().getDatabase().getPriceLists().update(pl);
			PriceList newInfPriceList = (PriceList) pl.clone();
			newInfPriceList.setId(Model.generateId());
			newInfPriceList.setStartDate(priceList.getEndDate().plusDays(1));
			newInfPriceList.setEndDate(null);
			AppState.getInstance().getDatabase().getPriceLists().insert(newInfPriceList);
			// and we insert the new pricelist
			AppState.getInstance().getDatabase().getPriceLists().insert(priceList);
			// and we insert
			return; // there is nothing else to do
		}
		// check if there is a price list with no end date whose start is before this
		// price list's end date
		priceLists = AppState.getInstance().getDatabase().getPriceLists().select(new SelectCondition() {
			@Override
			public boolean check(Model row) {
				PriceList pl = (PriceList) row;
				return !pl.isDeleted() && pl.getEndDate() == null && pl.getStartDate().isBefore(priceList.getEndDate());
			}
		});
		if (priceLists.size() > 0) {
			// there is a pricelist with no end date that starts the same day as this
			// pricelist
			// so we move that pricelist to start the day after this pricelist ends
			PriceList pl = priceLists.get(0);
			pl.setStartDate(priceList.getEndDate().plusDays(1));
			AppState.getInstance().getDatabase().getPriceLists().update(pl);
			// we dont insert the new pricelist because it can overlap with some pricelists
			// and those checks are next
			// so we just proceed to the next checks
		}

		// check if there is pricelist that fully contains this pricelist
		priceLists = AppState.getInstance().getDatabase().getPriceLists().select(new SelectCondition() {
			@Override
			public boolean check(Model row) {
				PriceList pl = (PriceList) row;
				return !pl.isDeleted() && pl.getStartDate().isBefore(priceList.getStartDate()) && pl.getEndDate() != null
						&& pl.getEndDate().isAfter(priceList.getEndDate());
			}
		});
		if (priceLists.size() > 0) {
			// there is a pricelist that contains this pricelist
			// so we split that pricelist into two
			PriceList pl = priceLists.get(0);
			PriceList newPl = (PriceList) pl.clone();
			newPl.setId(Model.generateId());
			pl.setEndDate(priceList.getStartDate().minusDays(1));
			newPl.setStartDate(priceList.getEndDate().plusDays(1));
			AppState.getInstance().getDatabase().getPriceLists().update(pl);
			AppState.getInstance().getDatabase().getPriceLists().insert(newPl);
			// and we insert the new pricelist
			AppState.getInstance().getDatabase().getPriceLists().insert(priceList);
			return; // there is nothing else to do
		}

		// get the pricelist that contains the start date of this pricelist
		priceLists = AppState.getInstance().getDatabase().getPriceLists().select(new SelectCondition() {
			@Override
			public boolean check(Model row) {
				PriceList pl = (PriceList) row;
				return !pl.isDeleted() && pl.getStartDate().isBefore(priceList.getStartDate())
						&& (pl.getEndDate() != null && pl.getEndDate().isAfter(priceList.getStartDate()));
			}
		});
		if (priceLists.size() > 0) {
            // there is a pricelist that contains the start date of this pricelist
            // so we end it the day before this pricelist starts
            PriceList pl = priceLists.get(0);
            pl.setEndDate(priceList.getStartDate().minusDays(1));
            AppState.getInstance().getDatabase().getPriceLists().update(pl);
        }
		// get the pricelist that contains the end date of this pricelist
		priceLists = AppState.getInstance().getDatabase().getPriceLists().select(new SelectCondition() {
			@Override
			public boolean check(Model row) {
				PriceList pl = (PriceList) row;
				return !pl.isDeleted() && pl.getStartDate().isBefore(priceList.getEndDate())
						&& (pl.getEndDate() != null && pl.getEndDate().isAfter(priceList.getEndDate()));
			}
		});
		if (priceLists.size() > 0) {
			// there is a pricelist that contains the end date of this pricelist
			// so we start it the day after this pricelist ends
			PriceList pl = priceLists.get(0);
			pl.setStartDate(priceList.getEndDate().plusDays(1));
			AppState.getInstance().getDatabase().getPriceLists().update(pl);
		}
		
		// check if there is a pricelist with the same start date and same end date
		priceLists = AppState.getInstance().getDatabase().getPriceLists().select(new SelectCondition() {
			@Override
			public boolean check(Model row) {
				PriceList pl = (PriceList) row;
				return !pl.isDeleted() && pl.getEndDate() != null && pl.getStartDate().equals(priceList.getStartDate())
						&& pl.getEndDate().equals(priceList.getEndDate());
			}
		});
		if (priceLists.size() > 0) {
			// there is a pricelist with the same start date and same end date
			// so we update that pricelist
			PriceList pl = priceLists.get(0);
			pl.update(priceList);
			AppState.getInstance().getDatabase().getPriceLists().update(pl);
			return; // there is nothing else to do
		}

		// get the list of price lists that are completely inside this price list
		ArrayList<PriceList> insidePriceLists = AppState.getInstance().getDatabase().getPriceLists()
				.select(new SelectCondition() {
					@Override
					public boolean check(Model row) {
						PriceList pl = (PriceList) row;
						if (pl.getEndDate() == null) return false;
						return !pl.isDeleted() && !pl.getStartDate().isBefore(priceList.getStartDate())
								&& !pl.getEndDate().isAfter(priceList.getEndDate());
					}
				});
		// they are overriden by this price list
		for (PriceList pl : insidePriceLists) {
			AppState.getInstance().getDatabase().getPriceLists().delete(pl);
		}
		
		
		// insert the new price list
		AppState.getInstance().getDatabase().getPriceLists().insert(priceList);
	}
}
