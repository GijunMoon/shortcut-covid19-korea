#-*- coding: utf-8 -*-
import os
import sys
import json

from flask import Flask, Response, request, jsonify
from urllib.request import urlopen
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/covid') #주소 뒤에 붙여야 함 [GET타입]
def covid():
    
    Res = list() #반환될 list

    html = urlopen("http://ncov.mohw.go.kr/bdBoardList.do") #코로나바이러스 실시간 현황 사이트
    bsObject = BeautifulSoup(html, "html.parser")
    #크롤링
    div_area = bsObject.find("div", {"class":"bv_content"})

    result = div_area.select('ul:nth-of-type(1)', {"class":"s_listin_dot"})

    for r in result: #반환 list에 크롤링한 데이터 입력
        Res.append(r.text)
    
    return json.dumps(Res, ensure_ascii=False, indent="\t").encode('utf8') #반환

    
 
if __name__ == "__main__":
    app.run()
