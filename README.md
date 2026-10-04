\# Distributed Dictionary Service — Lab 1



\## Group Members



\- LUYANDA SHOZI — 202315370

\- LUYANDA NXUMALO — 202312575

\- SPHESIHLE MAKHATHINI — 202363153

\- LWANDLE BUTHELEZI — 202246127



\## Lab 1: Simple Client-Server Communication



This Lab 1 snapshot implements a basic distributed client-server system using Python TCP sockets and Docker containers.



The system consists of two independent processes:



\- A TCP server running in a Docker container.

\- A TCP client running in a separate Docker container.



The client connects to the server over a Docker bridge network, sends a request, and receives a response.



\## Objectives



The practical demonstrates:



\- Docker containerisation.

\- Docker Compose.

\- TCP/IP socket communication.

\- Communication between independent processes.

\- Docker bridge networking.

\- Docker Compose service-name-based communication.

\- A basic request-and-response communication pattern.



\## Software Requirements



\- Windows 11

\- Docker Desktop

\- Docker Engine

\- Docker Compose

\- Python 3.13-slim Docker image

\- PowerShell



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

├── .gitignore

└── README.md

