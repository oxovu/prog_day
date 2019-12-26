# prog_day

Simply tells you when was/will be programmer day in a certan year

## to start
gradle startService

## example
$ curl http://localhost?year=2017 
{"errorCode": 200, "dataMessage": "13/09/17"}

$ curl http://localhost?month=12
{"errorCode": 400, "dataMessage": "Bad Request"}

$ curl http://localhost?year=201
{"errorCode": 401, "dataMessage": "Unacceptable year format. Should be XXXX"}

$ curl http://localhost?year=201d
{"errorCode": 402, "dataMessage": "Unacceptable year format. Should be all numbers"}
