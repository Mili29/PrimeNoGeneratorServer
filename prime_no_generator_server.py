# -*- coding: utf-8 -*-
"""
Created on Tue Mar 9 21:52:21 2021

@author: Mili
"""

from flask import Flask,jsonify,request
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    if(request.method=='POST'):
        some_json=request.get_json();
        return jsonify({'you sent' : some_json}),201
    else:
        return jsonify({"about":"Sup Mili!"})

@app.route('/multi/<int:num>',methods=['GET'])
def get_prime(num):
    for i in range(1,num):
        for j in range(2,x):
            if i%j==0:
                break
            else:
                return jsonify({"Prime numbers from 1 to num":concat("",i,"")})

if __name__=='__main__':
    app.run(debug=True)
