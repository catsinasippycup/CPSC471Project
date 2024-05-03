# CPSC 471 Project

# Members
* James peou
* Renell Miller
* Jhoshua Ampo 
* Carlos Fuentes
* Thanedh Sithisombath 

# How to Run
1. With a terminal open run `python server.py <SERVER PORT>` and replace `<SERVER PORT>` with your own port number:
    - Ex: `python server.py 4444`
2. In another terminal run `python client.py <SERVER ADDRESS> <SERVER PORT>` and replace with an address and the same port number from before.
    - Ex: `python client.py localhost 4444`
3. Once connected, `client.py` will indicate you are connected and in `server.py` will indicate a connection has been established. `client.py` will print `ftp>` meaning its ready to take commands.
4.  There are only four commands `get`, `put`, `ls` and `quit` respectively.
    - `get` downloads a file from the server via filename.
        - `ftp>get file.txt`
    -   `put` uploads a file to the server you must specify an exact path with filename.
        - `ftp>put C:\Users\foo\Desktop\example.txt`
    -   `ls` lists all the files on the server.
        - `ftp>ls`
    -   `quit` disconnects from the server and ends the program.
        - `ftp> quit`
5. Once finished use `quit` to exit.