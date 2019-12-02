All : inheritance

inheritance.o : inheritance.cpp
		g++ -c inheritance.cpp

main.o : main.cpp
		g++ -c main.cpp

inheritance : main.o inheritance.o
		g++ -o inheritance main.o inheritance.o

clean:
	rm -f *.o inheritance
