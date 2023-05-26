from flask import Flask 

FAI=Flask(__name__) 

@FAI.route('/wish')
def wish():
    return "Hello World"


if __name__=='__main__':    
    FAI.run(debug=True)
    