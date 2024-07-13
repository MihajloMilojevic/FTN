#include "SimWindow.h"
#include <iostream>

SimWindow::SimWindow(Point xy, int w, int h, const string& title) :
Window(xy, w, h, title),
	runButton(
	Point(x_max()-BUTTON_W, 0), 
	BUTTON_W, 
	BUTTON_H, 
	"RUN", 
	cb_run),
	stopButton(
	Point(x_max()-BUTTON_W, BUTTON_H), 
	BUTTON_W, 
	BUTTON_H, 
	"STOP", 
	cb_stop),
	runPushed(false),
	x(Axis::x,
		Point(100, y_max()/2),		
		400,					
		20,						
		"x axis"),
	y(Axis::y,
		Point(x_max()/2, 350),
		300,
		20,
		"y axis"),
	sine(sin,
		-10, 10,					
		Point(300, y_max()/2),			
		500,					
		20, 20),
	stopPushed(false)
{
	// @TODO - something missing ?
	y.set_color(Color::dark_green);
	y.label.set_color(Color::dark_green);
	x.set_color(Color::dark_green);
	x.label.set_color(Color::dark_green);
	sine.set_style(Line_style::dashdot);
	sine.set_color(Color::dark_red);
	attach(sine);
	attach(runButton);
	attach(stopButton);
	attach(x);
	attach(y);
	simulate();
}


void SimWindow::simulate()
{
	show();
	float p = 0.1;
	
	while(1)
	{
		
		runPushed = false;
		stopPushed = false;
		while(!runPushed && !stopPushed) Fl::wait();

		while (runPushed && !stopPushed)
		{
			detach(sine);
			sine.reset(-10, 10, 500, Point(300, y_max() / 2), 20, 20, sin, p);
			attach(sine);
			Fl::redraw();
			Fl::wait();
			p += 0.1;
			Sleep(50);
		}
		if (stopPushed)
		{

		}
	}
	return;
}


void SimWindow::cb_run(Address, Address pw)
{
	reference_to<SimWindow>(pw).run();
}


void SimWindow::cb_stop(Address, Address pw)
{
	reference_to<SimWindow>(pw).stop();
}


void SimWindow::run()
{
	runPushed = true;
}


void SimWindow::stop()
{
	stopPushed = true;
}
