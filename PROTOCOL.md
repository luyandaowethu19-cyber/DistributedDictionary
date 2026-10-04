\# Distributed Dictionary Service Protocol



\## INSERT



Request:

INSERT|key|value



Response:

SUCCESS|Record inserted



\## LOOKUP



Request:

LOOKUP|key



Response:

SUCCESS|value



\## UPDATE



Request:

UPDATE|key|value



Response:

SUCCESS|Record updated



\## DELETE



Request:

DELETE|key



Response:

SUCCESS|Record deleted



\## COUNT



Request:

COUNT



Response:

SUCCESS|<number of records>



Example:

COUNT

SUCCESS|3



\## LIST



Request:

LIST



Response:

SUCCESS|<key1>,<key2>,<key3>



Example:

LIST

SUCCESS|202315370,001,002



If the dictionary is empty:

SUCCESS|

