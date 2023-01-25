//turtle simulator!
//a quick introduction/review of C++ classes!

#include<iostream>
using namespace std;
//standalone function declarations/prototypes would go here too!

//class definition-------------------------------------------



class turtle {
private: //private variables can only be seen/used by members of the class
	string name;
	int hunger;
	bool isSwimming;
public: //can be seen and used by everything in your program
	turtle(); //default constructor: initalizes all the variables in your pig
	turtle(string n); //parameterized constructor
	void print();
	void feed();
	void move();
};//---------------------------------------------------------

int main() {
	turtle t1("Blicky Bruce"); //instantiate a pig object
	turtle t2("YEEEEE");
	while (true) { //game loop!
		t1.move();
		t2.move();
		cout << "Would you like to know the turtles information, feed the turtles, or do nothing" << endl;
		cout << "(i) is information, (f) is feed, (n) is do nothing" << endl;
		char input;
		cin >> input;
		if (input == 'i') {
			t1.print();
			t2.print();
		}
		else if (input == 'f') {
			t1.feed();
			t2.feed();

		}
		else if (input == 'n') {
			cout << "You did nothing" << endl;

		}
		else
			cout << "NAHHH B" << endl;
	}
}

turtle::turtle() {
	hunger = 0;
	isSwimming = true;
}

turtle::turtle(string n) {
	hunger = 0;
	isSwimming = true;
	name = n;
}

void turtle::feed() {
	hunger -= 20;
	cout << "You feed turtles" << endl;
}



void turtle::move() {
	hunger += 20;

	if (isSwimming == true) {
		int r = rand() % 2;
		if (r == 0)
			isSwimming = false;
		else
			isSwimming = true;


	}
	if (isSwimming == false) {
		int ran = rand() % 2;
		if (ran == 0)
			isSwimming = true;
		else
			isSwimming = false;
	}


}

void turtle::print() {
	cout << "I'm da turtle Da name is " << name << endl;

	cout << "Da hunger level is " << hunger << endl;
	if (isSwimming == true) cout << "Da turtle beswimming" << endl;
	else cout << "Dang I am on a rock" << endl;
}
