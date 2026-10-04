\# Distributed Dictionary Service



\## Group Members



\* LUYANDA SHOZI — 202315370

\* LUYANDA NXUMALO — 202312575

\* SPHESIHLE MAKHATHINI — 202363153

\* LWANDLE BUTHELEZI — 202246127



\## Project Description



This project implements a distributed dictionary service using a client-server architecture.



The system is developed incrementally throughout the Distributed Systems Laboratory practicals. In Lab 2, the dictionary protocol was extended to support the `COUNT` and `LIST` commands in addition to the existing `INSERT`, `LOOKUP`, `UPDATE`, and `DELETE` commands.



The client and dictionary server run in separate Docker containers and communicate using TCP over a Docker Compose bridge network.



\## Software Requirements



\* Windows 11

\* Docker Desktop

\* Docker Engine

\* Docker Compose

\* Python 3.13

\* PowerShell



\## Project Structure



```text

DistributedDictionary/

├── client/

│   └── src/

│       └── client.py

├── naming-service/

│   └── src/

│       └── .gitkeep

├── dictionary-server/

│   └── src/

│       └── server.py

├── shared/

│   └── .gitkeep

├── Dockerfile

├── docker-compose.yml

├── PROTOCOL.md

├── README.md

└── .gitignore

```



\## System Components



\### Dictionary Server



The dictionary server accepts TCP connections from clients and processes dictionary commands.



The server supports:



\* INSERT

\* LOOKUP

\* UPDATE

\* DELETE

\* COUNT

\* LIST



The server stores dictionary records in an in-memory data store.



\### Client



The client connects to the dictionary server through the Docker Compose service name:



```text

server:5000

```



The client sends dictionary commands to the server and displays the responses received from the server.



\## Lab 2 Protocol Extension



Lab 2 extends the dictionary protocol with two additional commands.



\### COUNT



The `COUNT` command returns the number of records currently stored in the dictionary.



Request:



```text

COUNT

```



Response:



```text

SUCCESS|<number of records>

```



Example:



```text

COUNT

SUCCESS|3

```



\### LIST



The `LIST` command returns the keys currently stored in the dictionary.



Request:



```text

LIST

```



Response:



```text

SUCCESS|<key1>,<key2>,<key3>

```



If the dictionary is empty:



```text

SUCCESS|

```



\## Lab 2 Demonstration



Before testing `COUNT` and `LIST`, at least three records are inserted into the dictionary.



One of the required records uses the student's student number and full name:



```text

INSERT|202315370|LUYANDA SHOZI

```



Additional records used in the demonstration are:



```text

INSERT|001|Distributed Systems

INSERT|002|Computer Science

```



The `COUNT` command then returns:



```text

SUCCESS|3

```



The `LIST` command returns the stored keys:



```text

SUCCESS|202315370,001,002

```



After deleting one record:



```text

DELETE|001

```



the `COUNT` command returns:



```text

SUCCESS|2

```



and `LIST` returns:



```text

SUCCESS|202315370,002

```



This demonstrates that `COUNT` and `LIST` correctly reflect changes to the dictionary.



\## Building the Project



From the project root directory, run:



```powershell

docker compose up --build

```



This builds the client and dictionary-server Docker images and starts the distributed system.



\## Running the Project



The system can also be started in detached mode using:



```powershell

docker compose up -d

```



To stop the system, use:



```powershell

docker compose down

```



\## Network Communication



The client and dictionary server communicate using TCP through the Docker Compose bridge network.



The dictionary server listens on:



```text

0.0.0.0:5000

```



The client connects using the Docker Compose service name:



```text

server:5000

```



Docker Compose provides service-name-based networking between the containers.



\## Protocol Documentation



The supported commands and their request and response formats are documented in:



```text

PROTOCOL.md

```



The protocol documentation includes:



\* INSERT

\* LOOKUP

\* UPDATE

\* DELETE

\* COUNT

\* LIST



\## Notes



The project is continuously developed across the Distributed Systems Laboratory practicals. Each laboratory extends the previous implementation rather than creating a separate project.



