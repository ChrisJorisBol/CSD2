#include <iostream>

/*
  Assignment: complete this program by putting your code in all the locations
    that say -- your code here --

  Make sure that the program compiles and builds and check the output
    after every change.

  Tip: before you look at the output, always think ahead what you expect to
    see and then check if your assumption was correct.
 */

int main()
{
char letter = 97; // find this in the ASCII table (type 'man ascii')
char *letterpointer;

  std::cout << "Contents of the variable letter: ";

  std::cout << letter;

  letterpointer = &letter;
  std::cout << "\nContents of letterpointer: ";

  std::cout<<letterpointer;
  std::cout << "\nContents of what letterpointer points to: ";

  std::cout << letterpointer;
  *letterpointer = 'b';
  std::cout << "\nThe variabele letter has gotten a new value through letterpointer.";
  std::cout << "\nContents of what letterpointer points to: ";
  // -- your code here --
  std::cout<<*letterpointer;

  std::cout << "\nContents of the variable letter: ";
  // -- your code here --
  std::cout<<letter;

  /*
   * Create the necessary pointer(s) and use them
   */
	typedef unsigned short ushort;
  ushort year = 2019;
  std::cout << "\nContents of the variabele year: ";
  // -- your code here --
  std::cout<<year;
	ushort *yearpointer;
yearpointer=&year;

  // create a pointer to year
  // -- your code here --

  std::cout << "\nContents of yearpointer: ";
  // -- your code here --
  std::cout<<yearpointer;
  std::cout << "\nContents of what yearpointer points to: ";
  std::cout<<*yearpointer;
  // give year a new value via yearpointer
  // -- your code here --
	// *yearpointer = 2029;
  std::cout << "\nContents of the variabele year: ";
  // -- your code here --
	std::cout<<year;
	ushort *anotheryearpointer;
	anotheryearpointer = &year;
  // create another pointer to year, named anotheryearpointer
  // -- your code here --

  std::cout << "\nContents of anotheryearpointer: ";
  // -- your code here --
	std::cout<<anotheryearpointer;
  std::cout << "\nContents of what anotheryearpointer points to: ";
	std::cout<<*anotheryearpointer;
  // give year a new value via anotheryearpointer
  // -- your code here --
	*anotheryearpointer = 2029;
  std::cout << "\nContents of year: ";
  std::cout<<year;

  std::cout << "\nContents of what anotheryearpointer points to: ";
  // -- your code here --
	std::cout << *anotheryearpointer;
  //anotheryearpointer++;
	anotheryearpointer ++;
  std::cout << "\nContents of anotheryearpointer after ++: ";
  // -- your code here --
  std::cout << anotheryearpointer;


} // main()
