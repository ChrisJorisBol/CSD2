All : inheritance

inheritance.o : inheritance.cpp
		g++ -c inheritance.cpp

keys.o : keys.cpp
		g++ -c keys.cpp

winds.o : winds.cpp
		g++ -c winds.cpp

main.o : main.cpp
		g++ -c main.cpp

inheritance : main.o inheritance.o keys.o winds.o
		g++ -o inheritance main.o inheritance.o keys.o winds.o

clean:
	rm -f *.o inheritance
