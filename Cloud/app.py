#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
import joblib

@app.route("/", methods =["GET","POST"]) ##must type this line 1st
def idx():
    if request.method == "POST":
        Income = request.form.get("Income")
        Age = request.form.get("Age")
        Loan = request.form.get("Loan")
        print(Income,Age,Loan)
        model = joblib.load("Credit Default Prediction_nnet")
        pred = model.predict([[float(Income),float(Age),float(Loan)]])
        s = "The predicted default score is : " + str(pred)
        return(render_template("index.html",result = s))
    else:
        return(render_template("index.html",result = "error"))


# In[ ]:


if __name__ == "__main__": #only run for my document! underscore means specific
    app.run()


# In[ ]:




