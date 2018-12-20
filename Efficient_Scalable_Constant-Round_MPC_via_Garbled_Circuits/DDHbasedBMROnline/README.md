## DDH based BMROnline

Implementation of the code using key homomorphic PRFs based on DDH in quadratic residues group of a large safe prime.

#### Compilation

The project uses ntl-9.10.0. In order to compile the project you should install it before compiling the project.  
Please install it at your home directory. NTL is available at this [link](https://www.shoup.net/ntl/ntl-9.10.0.tar.gz) 
Compilation is done using cmake: `cmake . && make`

#### Execution

Execution is done by executing:

`./HomOnlineTest.out <Partynum> <CircuitFile> <InputsFile> <IPFile> <Key> 0`

* Partynum is the party id. This number should also match the location of the party's IP in the IP file.  
For non-local execution, it is possible to use "-1" and the party number is taken as the location in the IP file.

* CircuitFile is the file of the circuit. All parties must use the exact same file.

* InputsFile contains the inputs for the input wires of the party.

* IPFile is the IPs (IPv4) of the parties. The file contains the IPs written row after row, without spaces. 
The IP of party p should appear at row p+1 (party 0 written on the first row, etc.). All parties must use the exact same file.

* Key should be a random secret key.