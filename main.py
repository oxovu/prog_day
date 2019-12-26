from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.command == 'GET':
            if self.path[2:6] == 'year':
                if len(self.path[7:]) == 4:
                    try:
                        year = int(self.path[7:])
                        short_year = int(self.path[9:])
                    except:
                        self.response(402, "Unacceptable year format. Should be all numbers")
                else:
                    self.response(401, "Unacceptable year format. Should be XXXX")
            else:
                self.response(400, "Bad request")
        else:
            self.response(400, "Bad request")
        if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
            self.response(200, "13/09/%d" % short_year)
        else:
            self.response(200, "12/09/%d" % short_year)

    def response(self, errorCode, dataMessage):
        self.send_response(200)
        self.send_header('content-type', 'text/json')
        self.end_headers()
        self.wfile.write(json.dumps({"errorCode": errorCode, "dataMessage": dataMessage}).encode())


def main():
    server = HTTPServer(('', 8080), HttpProcessor)
    server.serve_forever()


if __name__ == '__main__':
    main()
