------------------------------------------------------------------------------------------------------------------------------

EJERCICIO 1

------------------------------------------------------------------------------------------------------------------------------

The function to calculate the type of number is called "calculate" (main.py file)
- As argument accepts a list of numbers (int or str), 
- Print the type of number 
- It has a minimum error control in order to know if it is a number and greater than 1, and if it is integer (no fractionary numbers allowed)
- It was tested up to numbers of twelve digits, more than that the performance could be affected (take into account the prime seed should be incremented)

In addition, there is a main function in order to execute the program which accepts numbers sepparated by blanks (type main.py --h for more information).
- For instance: python.exe main.py 2 5 6 20 496 468 8589869056

The method used for calculating the divisors of a number consists in decomposing it in their prime factors (In order to get a prime list we are using 
the sieve of Eratosthenes) and then multiply all their comninations, for instance:	
	72 = 2^3 * 3^2
	2^0 * 3^0 = 1
	2^1 * 3^0 = 2
	2^2 * 3^0 = 4
	2^3 * 3^0 = 8
	2^0 * 3^1 = 3	
	2^1 * 3^1 = 6
	2^2 * 3^1 = 12
	2^3 * 3^1 = 24
	2^0 * 3^2 = 9
	2^1 * 3^2 = 18
	2^2 * 3^2 = 36	
	2^3 * 3^2 = 72
	

In utils.py there are some functions to support the operations, mainly there are two functions, "prime_generator" which allow us to generate a list of prime numbers
following the sieve of Eratosthenes and "calculate_divisors" which will give us the divisors following the method explained above. It is important to note that these
functions were taken from internet, not developed by my own.

There are two configuration files in "conf" folder:
- logging_config.ini which allow us to configure the messages of the output, right now it shows INFO messages on standard output and log/ejercicio1.log file
- application.ini which allow us to configure the prime seed used for the sieve of Eratosthenes, the recommmended value is 10000000 for dealing with twelve digit 
numbers, for bigger numbers this value should be increased but it would affect the performance.



------------------------------------------------------------------------------------------------------------------------------

EJERCICIO 2

------------------------------------------------------------------------------------------------------------------------------

The files located here must be deployed into a server directly (under a folder whith the application name, for instance ejercicio2)
- ejercicio2.html: Has all the code, basically when the page starts it reads the datasource from a local structure (now we have only three sources but we could
have more only adding them to the structure and writing the formatter function for each additional source). Once all the sources are being readed and processed 
(the callback function of ajax is going to be executed sequentially so there is no need to synchronize the data, once a callback is attended it must finish before 
another one starts) by means of promise the charts will be printed.
- js: directory with highcharts and jquery functions.
- data: directory with the three different sources. They were originally located at http://s3.amazonaws.com/logtrust-static/test/test/dataX.json but reading 
from a different domain is not allowed due to a Cross Domain issue (which can be resolved by means of CORS or JSONP which requires configuration on server side),
so finally the quick solution is having them locally.

It was tested only in latest versions of IE/FF/Chrome