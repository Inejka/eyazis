import numpy as np
from PIL import Image


def import_and_using_module():
    import pandas as pd
    dataset = pd.read_csv('test.csv')


def predefined_functions():
    object = 'words'
    pow(abs(len(object)), 2)


def cast_function():
    print(int(2.83925))
    print(float('13.345'))


def number_functions():
    print(pow(2, 3))
    round(5.24252)


def string_functions():
    print(chr(21))
    print(chr(289))


def data_processing_function():
    for i, c in enumerate("HELLO"):
        print(i, c)


def property_definitions():
    hello = "hello"
    print(hash(hello), id(hello))


def accessing_internal_structures():
    print(globals())


def building_function():
    a = 10
    b = 3
    for op in "+-*/%":
        print(eval("a " + op + " b"))


def input_output():
    f = open("file.txt", "r", 1)
    f.close()


def path_exists():
    import os
    os.path.exists("path")


def array_multiple():
    array = [0, 0, 0]
    tripled_array = [array] * 3
    tripled_array[0][1] = 1
    print(array)


def random():
    import random
    f = "asfasf"
    print(random.choice(f))


def getting_env():
    import os
    PATH = os.environ['PATH']
    print(PATH)


def module_time():
    import time
    print(time.localtime())


def locales():
    import time, locale
    locale.selocale(locale.LC_ALL, None)
    print(time.strftime("%d %B %Y", time.localtime(time.time())));


def gettext():
    str = 893
    print(gettext.gettext(str))


def math():
    import math
    math.sqrt(169)


def sys():
    import sys
    print(sys.platform)


def profile():
    import profile, sys
    profile.run("sys.platform")


# ---------------------------------
class Lab:
    def open_file(self, path):
        self.initial_matrix = np.asarray(Image.open(path)).astype('float')


    def pixel_transformation(self):
        for cell in np.nditer(self.initial_matrix, op_flags=['readwrite']):
            cell[...] = cell * 2 / 255 - 1

    def pixel_return(self):
        to_return = []
        for i in self.rectangles:
            temp = []
            for j in i:
                Y = np.dot(j, self.Wf)
                XX = np.dot(Y, self.Wb)
                temp.append(XX)
            to_return.append(temp)
        to_return = np.array(to_return)
        for cell in np.nditer(to_return, op_flags=['readwrite']):
            cell[...] = 255 * (min(1, max(-1, cell)) + 1) / 2.0

    def init_weight(self):
        self.Wf = (np.random.rand((self.m - 1) * (self.r - 1) * 3, self.p) + 0.01) * 2 - 1
        self.Wb = (np.random.rand(self.p, (self.m - 1) * (self.r - 1) * 3) + 0.01) * 2 - 1


    def train_coeff(self, matr):
        to_return = np.sum(np.square(matr))
        return 0.00007 if 1.0 / to_return == 0 else 1 / to_return

    def show_image(self, image):
        Image.fromarray(np.uint8(image)).save("unzip.bmp")

import sqlite3

def reset_db(self):
    conn = sqlite3.connect(self.path)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS keywords")
    c.execute("CREATE TABLE keywords (keyword TEXT,UNIQUE(keyword))")
    c.execute("DROP TABLE IF EXISTS tasks")
    # c.execute("CREATE TABLE tasks (task TEXT,time INTEGER, UNIQUE(task))")
    c.execute("CREATE TABLE tasks (task TEXT,time INTEGER)")
    conn.commit()
    conn.close()

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import cgi


class request_handler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        length = int(self.headers.get('content-length'))
        message = json.loads(self.rfile.read(length))
        print(message)
        ans = "ans"
        to_return = {'ans': ans}
        self._set_headers()
        self.wfile.write(json.dumps(to_return).encode('utf-8'))

def main():
    PORT = 8000
    server_address = ('localhost', PORT)
    server = HTTPServer(server_address, request_handler)
    print("Server running on port %s" % PORT)
    server.serve_forever()

if __name__ == "__main__":
    import_and_using_module()
    predefined_functions()
    cast_function()
    number_functions()
    string_functions()
    data_processing_function()
    property_definitions()
    accessing_internal_structures()
    building_function()
    input_output()
    path_exists()
    array_multiple()
    random()
    getting_env()
    module_time()
    locales()
    gettext()
    math()
    sys()
    profile()
    # ---------------------------------
