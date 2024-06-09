package views.admin;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Component;
import java.awt.Font;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;
import java.time.LocalDate;
import java.time.ZoneId;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;

import javax.swing.Box;
import javax.swing.DefaultListModel;
import javax.swing.DefaultListSelectionModel;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.ListModel;
import javax.swing.border.EmptyBorder;

import org.knowm.xchart.CategoryChart;
import org.knowm.xchart.CategorySeries.CategorySeriesRenderStyle;
import org.knowm.xchart.PieChart;
import org.knowm.xchart.XChartPanel;

import com.toedter.calendar.JDateChooser;

import controllers.ReportsController;
import controllers.ReportsController.Revenue;
import controllers.ReportsController.RoomsReport;
import models.Maid;
import models.enums.ReservationStatus;
import utils.Pair;

public class ReportsTab extends JPanel {

	private static final long serialVersionUID = 1L;

	private JDateChooser startCalendar;
	private JDateChooser endCalendar;
	private JLabel lblIncomeValue;
	private JLabel lblExpensesValue;
	private JLabel lblProfitValue;
	private JList<String> maidsList;
	private JLabel approvedReservationsValue;
	private JLabel cancelledReservationsValue;
	private JLabel rejectedReservationsValue;
	private JLabel totalReservationsValue;
	private JList<String> roomsList;

	/**
	 * Create the panel.
	 */
	public ReportsTab() {
		int y = 0;
		JPanel panel = new JPanel();
		panel.setBorder(new EmptyBorder(10, 10, 10, 10));
		panel.setForeground(new Color(255, 255, 255));
		panel.setBackground(new Color(73, 73, 73));
		GridBagLayout gridBagLayout = new GridBagLayout();
		gridBagLayout.columnWidths = new int[] { 0, 0 };
		gridBagLayout.rowHeights = new int[] { 0, 0, 0, 0, 0, 0, 0 };
		gridBagLayout.columnWeights = new double[] { 0.0, Double.MIN_VALUE };
		gridBagLayout.rowWeights = new double[] { 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, Double.MIN_VALUE };
		panel.setLayout(gridBagLayout);

		JLabel lblNewLabel = new JLabel("Reports");
		lblNewLabel.setForeground(new Color(255, 255, 255));
		lblNewLabel.setFont(new Font("Times New Roman", Font.PLAIN, 24));
		GridBagConstraints gbc_lblNewLabel = new GridBagConstraints();
		gbc_lblNewLabel.insets = new Insets(0, 0, 5, 0);
		gbc_lblNewLabel.gridx = 0;
		gbc_lblNewLabel.gridy = y++;
		gbc_lblNewLabel.gridwidth = 2;
		panel.add(lblNewLabel, gbc_lblNewLabel);

		Component verticalStrut = Box.createVerticalStrut(20);
		GridBagConstraints gbc_verticalStrut = new GridBagConstraints();
		gbc_verticalStrut.insets = new Insets(0, 0, 5, 0);
		gbc_verticalStrut.gridx = 0;
		gbc_verticalStrut.gridy = y++;
		panel.add(verticalStrut, gbc_verticalStrut);

		JLabel lblRevenueInLast = new JLabel("Revenue in last 12 months:");
		lblRevenueInLast.setForeground(Color.WHITE);
		lblRevenueInLast.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_lblRevenueInLast = new GridBagConstraints();
		gbc_lblRevenueInLast.insets = new Insets(0, 0, 5, 0);
		gbc_lblRevenueInLast.anchor = GridBagConstraints.WEST;
		gbc_lblRevenueInLast.gridx = 0;
		gbc_lblRevenueInLast.gridy = y++;
		gbc_lblRevenueInLast.gridwidth = 2;
		panel.add(lblRevenueInLast, gbc_lblRevenueInLast);

		Component verticalStrut_1 = Box.createVerticalStrut(5);
		GridBagConstraints gbc_verticalStrut_1 = new GridBagConstraints();
		gbc_verticalStrut_1.insets = new Insets(0, 0, 5, 0);
		gbc_verticalStrut_1.gridx = 0;
		gbc_verticalStrut_1.gridy = y++;
		panel.add(verticalStrut_1, gbc_verticalStrut_1);

		// REVENUE CHART

		ArrayList<Revenue> revenues = ReportsController.getRevenue();
		CategoryChart revenueChart = new CategoryChart(1300, 600);
		revenueChart.getStyler().setDefaultSeriesRenderStyle(CategorySeriesRenderStyle.Line);
		revenueChart.getStyler().setMarkerSize(5);
		revenueChart.setCustomXAxisTickLabelsFormatter(i -> revenues.get(0).getMonths()[(int) (double) i]);
		XChartPanel<CategoryChart> revenueChartPanel = new XChartPanel<>(revenueChart);
		double xData[] = new double[12];
		for (int i = 0; i < 12; i++) {
			xData[i] = i;
		}
		for (Revenue revenue : revenues) {
			revenueChart.addSeries(revenue.getType().getName(), xData, revenue.getMonthlyRevenue());
		}
		revenueChartPanel.setSize((int) (panel.getSize().width * 0.8), (int) (panel.getSize().height * 0.8));
		GridBagConstraints gbc_revenueChart = new GridBagConstraints();
		gbc_revenueChart.insets = new Insets(0, 0, 5, 0);
		gbc_revenueChart.gridx = 0;
		gbc_revenueChart.gridy = y++;
		gbc_revenueChart.gridwidth = 2;
		panel.add(revenueChartPanel, gbc_revenueChart);

		Component verticalStrut_2 = Box.createVerticalStrut(5);
		GridBagConstraints gbc_verticalStrut_2 = new GridBagConstraints();
		gbc_verticalStrut_2.insets = new Insets(0, 0, 5, 0);
		gbc_verticalStrut_2.gridx = 0;
		gbc_verticalStrut_2.gridy = y++;
		panel.add(verticalStrut_2, gbc_verticalStrut_2);

		JLabel lblMaidsInLast = new JLabel("Maids work in last 30 days:");
		lblMaidsInLast.setForeground(Color.WHITE);
		lblMaidsInLast.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_lblmaidInLast = new GridBagConstraints();
		gbc_lblmaidInLast.insets = new Insets(0, 0, 5, 0);
		gbc_lblmaidInLast.anchor = GridBagConstraints.WEST;
		gbc_lblmaidInLast.gridx = 0;
		gbc_lblmaidInLast.gridy = y++;
		gbc_lblmaidInLast.gridwidth = 2;
		panel.add(lblMaidsInLast, gbc_lblmaidInLast);

		Component verticalStrut_3 = Box.createVerticalStrut(5);
		GridBagConstraints gbc_verticalStrut_3 = new GridBagConstraints();
		gbc_verticalStrut_3.insets = new Insets(0, 0, 5, 0);
		gbc_verticalStrut_3.gridx = 0;
		gbc_verticalStrut_3.gridy = y++;
		panel.add(verticalStrut_3, gbc_verticalStrut_3);

		// MAID WORKLOAD CHART

		HashMap<Maid, Integer> maidWorkLoad30 = ReportsController.getMaidWorkload(LocalDate.now().minusDays(30),
				LocalDate.now());

		PieChart maidWorkLoad30Chart = new PieChart(500, 500);
		for (Maid maid : maidWorkLoad30.keySet()) {
			maidWorkLoad30Chart.addSeries(maid.getName(), maidWorkLoad30.get(maid));
		}
		XChartPanel<PieChart> maidWorkLoad30ChartPanel = new XChartPanel<>(maidWorkLoad30Chart);
		maidWorkLoad30ChartPanel.setSize((int) (panel.getSize().width * 0.8), (int) (panel.getSize().height * 0.8));
		GridBagConstraints gbc_maidWorkLoad30Chart = new GridBagConstraints();
		gbc_maidWorkLoad30Chart.insets = new Insets(0, 0, 5, 0);
		gbc_maidWorkLoad30Chart.gridx = 0;
		gbc_maidWorkLoad30Chart.gridy = y++;
		gbc_maidWorkLoad30Chart.gridwidth = 2;
		panel.add(maidWorkLoad30ChartPanel, gbc_maidWorkLoad30Chart);

		Component verticalStrut_4 = Box.createVerticalStrut(5);
		GridBagConstraints gbc_verticalStrut_4 = new GridBagConstraints();
		gbc_verticalStrut_4.insets = new Insets(0, 0, 5, 0);
		gbc_verticalStrut_4.gridx = 0;
		gbc_verticalStrut_4.gridy = y++;
		panel.add(verticalStrut_4, gbc_verticalStrut_4);

		JLabel lblStatusesLast30 = new JLabel("Reservation statuses of reservations created in last 30 days:");
		lblStatusesLast30.setForeground(Color.WHITE);
		lblStatusesLast30.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_lblStatusesLast30 = new GridBagConstraints();
		gbc_lblStatusesLast30.insets = new Insets(0, 0, 5, 0);
		gbc_lblStatusesLast30.anchor = GridBagConstraints.WEST;
		gbc_lblStatusesLast30.gridx = 0;
		gbc_lblStatusesLast30.gridy = y++;
		gbc_lblStatusesLast30.gridwidth = 2;
		panel.add(lblStatusesLast30, gbc_lblStatusesLast30);

		Component verticalStrut_5 = Box.createVerticalStrut(5);
		GridBagConstraints gbc_verticalStrut_5 = new GridBagConstraints();
		gbc_verticalStrut_5.insets = new Insets(0, 0, 5, 0);
		gbc_verticalStrut_5.gridx = 0;
		gbc_verticalStrut_5.gridy = y++;
		panel.add(verticalStrut_5, gbc_verticalStrut_5);

		// RESERVATION STATUSES CHART

		HashMap<ReservationStatus, Integer> reservationStatuses30 = ReportsController.getReservationStatuses();
		PieChart reservationStatuses30Chart = new PieChart(500, 500);
		for (ReservationStatus status : reservationStatuses30.keySet()) {
			reservationStatuses30Chart.addSeries(status.toString(), reservationStatuses30.get(status));
		}
		XChartPanel<PieChart> reservationStatuses30ChartPanel = new XChartPanel<>(reservationStatuses30Chart);
		reservationStatuses30ChartPanel.setSize((int) (panel.getSize().width * 0.8),
				(int) (panel.getSize().height * 0.8));
		GridBagConstraints gbc_reservationStatuses30Chart = new GridBagConstraints();
		gbc_reservationStatuses30Chart.insets = new Insets(0, 0, 5, 0);
		gbc_reservationStatuses30Chart.gridx = 0;
		gbc_reservationStatuses30Chart.gridy = y++;
		gbc_reservationStatuses30Chart.gridwidth = 2;
		panel.add(reservationStatuses30ChartPanel, gbc_reservationStatuses30Chart);

		Component verticalStrut_6 = Box.createVerticalStrut(25);
		GridBagConstraints gbc_verticalStrut_6 = new GridBagConstraints();
		gbc_verticalStrut_6.insets = new Insets(0, 0, 5, 0);
		gbc_verticalStrut_6.gridx = 0;
		gbc_verticalStrut_6.gridy = y++;
		panel.add(verticalStrut_6, gbc_verticalStrut_6);

		JLabel lblPeriod = new JLabel("Select a period:");
		lblPeriod.setForeground(Color.WHITE);
		lblPeriod.setFont(new Font("Times New Roman", Font.PLAIN, 20));
		GridBagConstraints gbc_lblPeriod = new GridBagConstraints();
		gbc_lblPeriod.insets = new Insets(0, 0, 5, 0);
		gbc_lblPeriod.anchor = GridBagConstraints.WEST;
		gbc_lblPeriod.gridx = 0;
		gbc_lblPeriod.gridy = y++;
		gbc_lblPeriod.gridwidth = 2;
		panel.add(lblPeriod, gbc_lblPeriod);

		Component verticalStrut_7 = Box.createVerticalStrut(5);
		GridBagConstraints gbc_verticalStrut_7 = new GridBagConstraints();
		gbc_verticalStrut_7.insets = new Insets(0, 0, 5, 0);
		gbc_verticalStrut_7.gridx = 0;
		gbc_verticalStrut_7.gridy = y++;
		panel.add(verticalStrut_7, gbc_verticalStrut_7);

		JLabel lblStartDate = new JLabel("Start date:");
		lblStartDate.setForeground(Color.WHITE);
		lblStartDate.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_lblStartDate = new GridBagConstraints();
		gbc_lblStartDate.insets = new Insets(0, 0, 5, 0);
		gbc_lblStartDate.anchor = GridBagConstraints.WEST;
		gbc_lblStartDate.gridx = 0;
		gbc_lblStartDate.gridy = y;
		panel.add(lblStartDate, gbc_lblStartDate);

		PropertyChangeListener listener = new PropertyChangeListener() {
			@Override
			public void propertyChange(PropertyChangeEvent evt) {
				fillReports();
			}
		};

		startCalendar = new JDateChooser();
		startCalendar.setForeground(Color.WHITE);
		startCalendar.setBackground(new Color(73, 73, 73));
		startCalendar.setDate(
				Date.from(LocalDate.now().minusDays(30).atStartOfDay().atZone(ZoneId.systemDefault()).toInstant()));
		GridBagConstraints gbc_startCalendar = new GridBagConstraints();
		gbc_startCalendar.insets = new Insets(0, 0, 5, 0);
		gbc_startCalendar.gridx = 1;
		gbc_startCalendar.gridy = y++;
		gbc_startCalendar.fill = GridBagConstraints.HORIZONTAL;
		panel.add(startCalendar, gbc_startCalendar);

		Component verticalStrut_8 = Box.createVerticalStrut(5);
		GridBagConstraints gbc_verticalStrut_8 = new GridBagConstraints();
		gbc_verticalStrut_8.insets = new Insets(0, 0, 5, 0);
		gbc_verticalStrut_8.gridx = 0;
		gbc_verticalStrut_8.gridy = y++;
		panel.add(verticalStrut_8, gbc_verticalStrut_8);

		JLabel lblEndDate = new JLabel("End date:");
		lblEndDate.setForeground(Color.WHITE);
		lblEndDate.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_lblEndDate = new GridBagConstraints();
		gbc_lblEndDate.insets = new Insets(0, 0, 5, 0);
		gbc_lblEndDate.anchor = GridBagConstraints.WEST;
		gbc_lblEndDate.gridx = 0;
		gbc_lblEndDate.gridy = y;
		panel.add(lblEndDate, gbc_lblEndDate);

		endCalendar = new JDateChooser();
		endCalendar.setForeground(Color.WHITE);
		endCalendar.setBackground(new Color(73, 73, 73));
		endCalendar.setDate(Date.from(LocalDate.now().atStartOfDay().atZone(ZoneId.systemDefault()).toInstant()));
		GridBagConstraints gbc_endCalendar = new GridBagConstraints();
		gbc_endCalendar.insets = new Insets(0, 0, 5, 0);
		gbc_endCalendar.gridx = 1;
		gbc_endCalendar.gridy = y++;
		gbc_endCalendar.fill = GridBagConstraints.HORIZONTAL;
		panel.add(endCalendar, gbc_endCalendar);

		Component verticalStrut_9 = Box.createVerticalStrut(5);
		GridBagConstraints gbc_verticalStrut_9 = new GridBagConstraints();
		gbc_verticalStrut_9.insets = new Insets(0, 0, 5, 0);
		gbc_verticalStrut_9.gridx = 0;
		gbc_verticalStrut_9.gridy = y++;
		panel.add(verticalStrut_9, gbc_verticalStrut_9);

		JLabel lblRevenueInPeriod = new JLabel("Revenue in selected period:");
		lblRevenueInPeriod.setForeground(Color.WHITE);
		lblRevenueInPeriod.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_lblRevenueInPeriod = new GridBagConstraints();
		gbc_lblRevenueInPeriod.insets = new Insets(0, 0, 5, 0);
		gbc_lblRevenueInPeriod.anchor = GridBagConstraints.WEST;
		gbc_lblRevenueInPeriod.gridx = 0;
		gbc_lblRevenueInPeriod.gridy = y++;
		gbc_lblRevenueInPeriod.gridwidth = 2;
		panel.add(lblRevenueInPeriod, gbc_lblRevenueInPeriod);

		Component verticalStrut_10 = Box.createVerticalStrut(5);
		GridBagConstraints gbc_verticalStrut_10 = new GridBagConstraints();
		gbc_verticalStrut_10.insets = new Insets(0, 0, 5, 0);
		gbc_verticalStrut_10.gridx = 0;
		gbc_verticalStrut_10.gridy = y++;
		panel.add(verticalStrut_10, gbc_verticalStrut_10);

		JLabel lblIncome = new JLabel("Income:");
		lblIncome.setForeground(Color.WHITE);
		lblIncome.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_lblIncome = new GridBagConstraints();
		gbc_lblIncome.insets = new Insets(0, 0, 5, 0);
		gbc_lblIncome.anchor = GridBagConstraints.WEST;
		gbc_lblIncome.gridx = 0;
		gbc_lblIncome.gridy = y;
		panel.add(lblIncome, gbc_lblIncome);

		lblIncomeValue = new JLabel("0");
		lblIncomeValue.setForeground(Color.WHITE);
		lblIncomeValue.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_lblIncomeValue = new GridBagConstraints();
		gbc_lblIncomeValue.insets = new Insets(0, 0, 5, 0);
		gbc_lblIncomeValue.anchor = GridBagConstraints.WEST;
		gbc_lblIncomeValue.gridx = 1;
		gbc_lblIncomeValue.gridy = y++;
		panel.add(lblIncomeValue, gbc_lblIncomeValue);

		JLabel lblExpenses = new JLabel("Expenses:");
		lblExpenses.setForeground(Color.WHITE);
		lblExpenses.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_lblExpenses = new GridBagConstraints();
		gbc_lblExpenses.insets = new Insets(0, 0, 5, 0);
		gbc_lblExpenses.anchor = GridBagConstraints.WEST;
		gbc_lblExpenses.gridx = 0;
		gbc_lblExpenses.gridy = y;
		panel.add(lblExpenses, gbc_lblExpenses);

		lblExpensesValue = new JLabel("0");
		lblExpensesValue.setForeground(Color.WHITE);
		lblExpensesValue.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_lblExpensesValue = new GridBagConstraints();
		gbc_lblExpensesValue.insets = new Insets(0, 0, 5, 0);
		gbc_lblExpensesValue.anchor = GridBagConstraints.WEST;
		gbc_lblExpensesValue.gridx = 1;
		gbc_lblExpensesValue.gridy = y++;
		panel.add(lblExpensesValue, gbc_lblExpensesValue);

		JLabel lblProfit = new JLabel("Profit:");
		lblProfit.setForeground(Color.WHITE);
		lblProfit.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_lblProfit = new GridBagConstraints();
		gbc_lblProfit.insets = new Insets(0, 0, 5, 0);
		gbc_lblProfit.anchor = GridBagConstraints.WEST;
		gbc_lblProfit.gridx = 0;
		gbc_lblProfit.gridy = y;
		panel.add(lblProfit, gbc_lblProfit);

		lblProfitValue = new JLabel("0");
		lblProfitValue.setForeground(Color.WHITE);
		lblProfitValue.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_lblProfitValue = new GridBagConstraints();
		gbc_lblProfitValue.insets = new Insets(0, 0, 5, 0);
		gbc_lblProfitValue.anchor = GridBagConstraints.WEST;
		gbc_lblProfitValue.gridx = 1;
		gbc_lblProfitValue.gridy = y++;
		panel.add(lblProfitValue, gbc_lblProfitValue);

		Component verticalStrut_13 = Box.createVerticalStrut(5);
		GridBagConstraints gbc_verticalStrut_13 = new GridBagConstraints();
		gbc_verticalStrut_13.insets = new Insets(0, 0, 5, 0);
		gbc_verticalStrut_13.gridx = 0;
		gbc_verticalStrut_13.gridy = y++;
		panel.add(verticalStrut_13, gbc_verticalStrut_13);

		JLabel lblMaidsInPeriod = new JLabel("Maids work in selected period:");
		lblMaidsInPeriod.setForeground(Color.WHITE);
		lblMaidsInPeriod.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_lblMaidsInPeriod = new GridBagConstraints();
		gbc_lblMaidsInPeriod.insets = new Insets(0, 0, 5, 0);
		gbc_lblMaidsInPeriod.anchor = GridBagConstraints.NORTHWEST;
		gbc_lblMaidsInPeriod.gridx = 0;
		gbc_lblMaidsInPeriod.gridy = y;
		gbc_lblMaidsInPeriod.ipadx = 10;
		panel.add(lblMaidsInPeriod, gbc_lblMaidsInPeriod);

		maidsList = new JList<>();
		maidsList.setForeground(Color.WHITE);
		maidsList.setBackground(new Color(73, 73, 73));
		maidsList.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		maidsList.setSelectionModel(new DefaultListSelectionModel() {

			private static final long serialVersionUID = 6892769336507203231L;

			@Override
			public void setAnchorSelectionIndex(final int anchorIndex) {
			}

			@Override
			public void setLeadAnchorNotificationEnabled(final boolean flag) {
			}

			@Override
			public void setLeadSelectionIndex(final int leadIndex) {
			}

			@Override
			public void setSelectionInterval(final int index0, final int index1) {
			}
		});
		GridBagConstraints gbc_maidsList = new GridBagConstraints();
		gbc_maidsList.insets = new Insets(0, 0, 5, 0);
		gbc_maidsList.gridx = 1;
		gbc_maidsList.gridy = y++;
		gbc_maidsList.fill = GridBagConstraints.BOTH;
		panel.add(maidsList, gbc_maidsList);

		Component verticalStrut_14 = Box.createVerticalStrut(5);
		GridBagConstraints gbc_verticalStrut_14 = new GridBagConstraints();
		gbc_verticalStrut_14.insets = new Insets(0, 0, 5, 0);
		gbc_verticalStrut_14.gridx = 0;
		gbc_verticalStrut_14.gridy = y++;
		panel.add(verticalStrut_14, gbc_verticalStrut_14);

		JLabel lblStatusesInPeriod = new JLabel("Reservation statuses of reservations in selected period:");
		lblStatusesInPeriod.setForeground(Color.WHITE);
		lblStatusesInPeriod.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_lblStatusesInPeriod = new GridBagConstraints();
		gbc_lblStatusesInPeriod.insets = new Insets(0, 0, 5, 0);
		gbc_lblStatusesInPeriod.anchor = GridBagConstraints.WEST;
		gbc_lblStatusesInPeriod.gridx = 0;
		gbc_lblStatusesInPeriod.gridy = y++;
		gbc_lblStatusesInPeriod.gridwidth = 2;
		panel.add(lblStatusesInPeriod, gbc_lblStatusesInPeriod);

		Component verticalStrut_15 = Box.createVerticalStrut(5);
		GridBagConstraints gbc_verticalStrut_15 = new GridBagConstraints();
		gbc_verticalStrut_15.insets = new Insets(0, 0, 5, 0);
		gbc_verticalStrut_15.gridx = 0;
		gbc_verticalStrut_15.gridy = y++;
		panel.add(verticalStrut_15, gbc_verticalStrut_15);

		JLabel lblApprovedReservations = new JLabel("Approved:");
		lblApprovedReservations.setForeground(Color.WHITE);
		lblApprovedReservations.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_lblApprovedReservations = new GridBagConstraints();
		gbc_lblApprovedReservations.insets = new Insets(0, 0, 5, 0);
		gbc_lblApprovedReservations.anchor = GridBagConstraints.WEST;
		gbc_lblApprovedReservations.gridx = 0;
		gbc_lblApprovedReservations.gridy = y;
		panel.add(lblApprovedReservations, gbc_lblApprovedReservations);

		approvedReservationsValue = new JLabel("0");
		approvedReservationsValue.setForeground(Color.WHITE);
		approvedReservationsValue.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_approvedReservationsValue = new GridBagConstraints();
		gbc_approvedReservationsValue.insets = new Insets(0, 0, 5, 0);
		gbc_approvedReservationsValue.anchor = GridBagConstraints.WEST;
		gbc_approvedReservationsValue.gridx = 1;
		gbc_approvedReservationsValue.gridy = y++;
		panel.add(approvedReservationsValue, gbc_approvedReservationsValue);

		JLabel lblCancelledReservations = new JLabel("Cancelled:");
		lblCancelledReservations.setForeground(Color.WHITE);
		lblCancelledReservations.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_lblCancelledReservations = new GridBagConstraints();
		gbc_lblCancelledReservations.insets = new Insets(0, 0, 5, 0);
		gbc_lblCancelledReservations.anchor = GridBagConstraints.WEST;
		gbc_lblCancelledReservations.gridx = 0;
		gbc_lblCancelledReservations.gridy = y;
		panel.add(lblCancelledReservations, gbc_lblCancelledReservations);

		cancelledReservationsValue = new JLabel("0");
		cancelledReservationsValue.setForeground(Color.WHITE);
		cancelledReservationsValue.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_cancelledReservationsValue = new GridBagConstraints();
		gbc_cancelledReservationsValue.insets = new Insets(0, 0, 5, 0);
		gbc_cancelledReservationsValue.anchor = GridBagConstraints.WEST;
		gbc_cancelledReservationsValue.gridx = 1;
		gbc_cancelledReservationsValue.gridy = y++;
		panel.add(cancelledReservationsValue, gbc_cancelledReservationsValue);

		JLabel lblRejectedReservations = new JLabel("Rejected:");
		lblRejectedReservations.setForeground(Color.WHITE);
		lblRejectedReservations.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_lblRejectedReservations = new GridBagConstraints();
		gbc_lblRejectedReservations.insets = new Insets(0, 0, 5, 0);
		gbc_lblRejectedReservations.anchor = GridBagConstraints.WEST;
		gbc_lblRejectedReservations.gridx = 0;
		gbc_lblRejectedReservations.gridy = y;
		panel.add(lblRejectedReservations, gbc_lblRejectedReservations);

		rejectedReservationsValue = new JLabel("0");
		rejectedReservationsValue.setForeground(Color.WHITE);
		rejectedReservationsValue.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_rejectedReservationsValue = new GridBagConstraints();
		gbc_rejectedReservationsValue.insets = new Insets(0, 0, 5, 0);
		gbc_rejectedReservationsValue.anchor = GridBagConstraints.WEST;
		gbc_rejectedReservationsValue.gridx = 1;
		gbc_rejectedReservationsValue.gridy = y++;
		panel.add(rejectedReservationsValue, gbc_rejectedReservationsValue);

		JLabel lblTotalReservations = new JLabel("Processed in total:");
		lblTotalReservations.setForeground(Color.WHITE);
		lblTotalReservations.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_lblTotalReservations = new GridBagConstraints();
		gbc_lblTotalReservations.insets = new Insets(0, 0, 5, 0);
		gbc_lblTotalReservations.anchor = GridBagConstraints.WEST;
		gbc_lblTotalReservations.gridx = 0;
		gbc_lblTotalReservations.gridy = y;
		panel.add(lblTotalReservations, gbc_lblTotalReservations);

		totalReservationsValue = new JLabel("0");
		totalReservationsValue.setForeground(Color.WHITE);
		totalReservationsValue.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_totalReservationsValue = new GridBagConstraints();
		gbc_totalReservationsValue.insets = new Insets(0, 0, 5, 0);
		gbc_totalReservationsValue.anchor = GridBagConstraints.WEST;
		gbc_totalReservationsValue.gridx = 1;
		gbc_totalReservationsValue.gridy = y++;
		panel.add(totalReservationsValue, gbc_totalReservationsValue);
		
		Component verticalStrut_16 = Box.createVerticalStrut(5);
		GridBagConstraints gbc_verticalStrut_16 = new GridBagConstraints();
		gbc_verticalStrut_16.insets = new Insets(0, 0, 5, 0);
		gbc_verticalStrut_16.gridx = 0;
		gbc_verticalStrut_16.gridy = y++;
		panel.add(verticalStrut_16, gbc_verticalStrut_16);
		
		JLabel lblRoomsInPeriod = new JLabel("Rooms in selected period:");
		lblRoomsInPeriod.setForeground(Color.WHITE);
		lblRoomsInPeriod.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		GridBagConstraints gbc_lblRoomsInPeriod = new GridBagConstraints();
		gbc_lblRoomsInPeriod.insets = new Insets(0, 0, 5, 0);
		gbc_lblRoomsInPeriod.anchor = GridBagConstraints.NORTHWEST;
		gbc_lblRoomsInPeriod.gridx = 0;
		gbc_lblRoomsInPeriod.gridy = y;
		gbc_lblRoomsInPeriod.gridwidth = 2;
		panel.add(lblRoomsInPeriod, gbc_lblRoomsInPeriod);
		
		roomsList = new JList<>();
		roomsList.setForeground(Color.WHITE);
		roomsList.setBackground(new Color(73, 73, 73));
		roomsList.setFont(new Font("Times New Roman", Font.PLAIN, 14));
		roomsList.setSelectionModel(new DefaultListSelectionModel() {

			private static final long serialVersionUID = 6892769336507203231L;

			@Override
			public void setAnchorSelectionIndex(final int anchorIndex) {
			}

			@Override
			public void setLeadAnchorNotificationEnabled(final boolean flag) {
			}

			@Override
			public void setLeadSelectionIndex(final int leadIndex) {
			}

			@Override
			public void setSelectionInterval(final int index0, final int index1) {
			}
		});
		GridBagConstraints gbc_roomsList = new GridBagConstraints();
		gbc_roomsList.insets = new Insets(0, 0, 5, 0);
		gbc_roomsList.gridx = 1;
		gbc_roomsList.gridy = y++;
		gbc_roomsList.fill = GridBagConstraints.BOTH;
		panel.add(roomsList, gbc_roomsList);

		// SCROLL PANE

		setLayout(new BorderLayout(0, 0));
		JScrollPane scrollPane = new JScrollPane();
		scrollPane.setViewportView(panel);
		add(scrollPane, BorderLayout.CENTER);

		startCalendar.addPropertyChangeListener("date", listener);
		endCalendar.addPropertyChangeListener("date", listener);

		fillReports();
	}

	private void fillReports() {
		if (startCalendar.getDate() == null) {
			resetReports("Select start date");
			return;
		}
		if (endCalendar.getDate() == null) {
			resetReports("Select end date");
			return;
		}
		LocalDate startDate = startCalendar.getDate().toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
		LocalDate endDate = endCalendar.getDate().toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
		if (startDate.isAfter(endDate)) {
			resetReports("Start date is after end date");
			return;
		}

		Pair<Double, Double> incomeExpenses = ReportsController.getRevenueForPeriod(startDate, endDate);
		lblIncomeValue.setText(String.format("%+.2f", incomeExpenses.getFirst()));
		lblExpensesValue.setText(String.format("%+.2f", -incomeExpenses.getSecond()));
		lblProfitValue.setText(String.format("%+.2f", incomeExpenses.getFirst() - incomeExpenses.getSecond()));
		lblProfitValue
				.setForeground(incomeExpenses.getFirst() - incomeExpenses.getSecond() < 0 ? Color.RED : Color.GREEN);

		HashMap<Maid, Integer> maidWorkLoad = ReportsController.getMaidWorkload(startDate, endDate);
		ListModel<String> maidsListModel = new DefaultListModel<>();
		for (Maid maid : maidWorkLoad.keySet()) {
			((DefaultListModel<String>) maidsListModel).addElement(maid.getName() + ": " + maidWorkLoad.get(maid));
		}
		maidsList.setModel(maidsListModel);

		HashMap<ReservationStatus, Integer> reservationStatuses = ReportsController
				.getReservationStatusesForPeriod(startDate, endDate);

		int approved = reservationStatuses.get(ReservationStatus.APPROVED) == null ? 0
				: reservationStatuses.get(ReservationStatus.APPROVED);
		int cancelled = reservationStatuses.get(ReservationStatus.CANCELLED) == null ? 0
				: reservationStatuses.get(ReservationStatus.CANCELLED);
	    int rejected = reservationStatuses.get(ReservationStatus.REJECTED) == null ? 0
	                    : reservationStatuses.get(ReservationStatus.REJECTED);
	    int total = approved + cancelled + rejected;
		approvedReservationsValue.setText(String.valueOf(approved));
		cancelledReservationsValue.setText(String.valueOf(cancelled));
		rejectedReservationsValue.setText(String.valueOf(rejected));
		
		totalReservationsValue.setText(String.valueOf(total));
	
		ArrayList<RoomsReport> roomsReport = ReportsController.getRoomsReportForPeriod(startDate, endDate);
		ListModel<String> roomsListModel = new DefaultListModel<>();
		for (RoomsReport room : roomsReport) {
			((DefaultListModel<String>) roomsListModel)
					.addElement("Room: " + room.getRoom().getNumber() + "  -  " + room.getNights() + " nights  -  " + String.format("%.2f", room.getRevenue()) + "rsd");
		}
		roomsList.setModel(roomsListModel);
	}

	private void resetReports(String msg) {
		lblIncomeValue.setText(msg);
		lblExpensesValue.setText(msg);
		lblProfitValue.setText(msg);
		approvedReservationsValue.setText(msg);
		cancelledReservationsValue.setText(msg);
		rejectedReservationsValue.setText(msg);
		totalReservationsValue.setText(msg);
		((DefaultListModel<String>) maidsList.getModel()).removeAllElements();
		((DefaultListModel<String>) maidsList.getModel()).addElement(msg);
		((DefaultListModel<String>) roomsList.getModel()).removeAllElements();
		((DefaultListModel<String>) roomsList.getModel()).addElement(msg);
	}
}
