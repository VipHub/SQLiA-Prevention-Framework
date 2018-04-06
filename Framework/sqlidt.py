
from bottle import run, post, request, response, get, route



def init():
		
	# coding: utf-8

	# #### Data source :https://archive.ics.uci.edu/ml/machine-learning-databases/00228/

	# In[42]:


	import numpy as np
	import pandas as pd
	from sklearn.cross_validation import train_test_split
	from sklearn.feature_extraction.text import TfidfVectorizer
	from sklearn import svm


	# In[2]:


	df=pd.read_csv('dataset',sep=',',names=['Status','Message'])


	# In[3]:


	df.head()


	# In[4]:


	len(df)


	# In[5]:


	len(df[df.Status=='Spam'])


	# In[6]:


	len(df[df.Status=='Ham'])


	# In[7]:


	df.loc[df["Status"]=='Ham',"Status",]=0


	# In[8]:


	df.loc[df["Status"]=='Spam',"Status",]=1


	# In[9]:


	df.head()


	# In[10]:


	df_x=df["Message"]
	df_y=df["Status"]


	# In[11]:


	x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)


	# In[12]:


	x_train.head()


	# In[13]:


	global cv1
	cv1 = TfidfVectorizer(min_df=1,stop_words=None)


	# In[14]:


	x_traincv=cv1.fit_transform(x_train.values.astype(str))


	# In[15]:


	x_testcv=cv1.transform(x_test)


	# In[16]:


	x_testcv.toarray()


	# In[17]:

	global clf
	clf = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
	   decision_function_shape='ovr', degree=3, gamma='auto', kernel='linear',
	   max_iter=-1, probability=True, random_state=None, shrinking=True,
	   tol=0.001, verbose=False)


	# In[18]:


	y_train=y_train.astype('int')


	# In[19]:


	clf.fit(x_traincv,y_train)


	# In[20]:


	predictions=clf.predict(x_testcv)
	print("**************Predictions of test set****************************")
	print("##################################################################################")
	print(predictions)
	print("##################################################################################")    


	# In[39]:


	print("**************Predictions of user defined input****************************")
	newb=cv1.transform(["vipul"]) #"1' OR '1'='1"
	print(newb)
	predict2=clf.predict(newb)
	print("##################################################################################")
	print(predict2)
	print("##################################################################################")


	# In[36]:


	a=np.array(y_test)


	# In[37]:


	a


	# In[38]:


	count=0
	print("##Loading##")


	# In[25]:


	for i in range (len(predictions)):
		print("#",end='')
		if predictions[i]==a[i]:
			count=count+1


	# In[26]:


	count


	# In[27]:


	j=len(predictions)


	# In[41]:


	accuracy=(count/j)
	print("Total Predictions:",j," Accurate Predictions:",count," Accuracy:",accuracy," Approximation:",accuracy*100,"%")

init()

# @route('/<path>',method = 'GET')
# def process(path):

# 	print("**************Predictions of user defined input****************************")
# 	newb=cv1.transform([""+path]) #"1' OR '1'='1"
# 	print(newb)
# 	predict2=clf.predict(newb)
# 	print("##################################################################################")
# 	print(predict2)
# 	print("##################################################################################")

# 	return str(predict2)
	
def str2bool(v):
  return v in ("[1]")


@post('/val') # or @route('/login', method='POST')
def val():
	par = request.forms.get('par')
	print("**************Predictions of user defined input****************************")
	newb=cv1.transform([""+par]) #"1' OR '1'='1"
	print(newb)
	predict2=clf.predict(newb)
	print("##################################################################################")
	print(predict2) #retuns predited decision
	print("##################################################################################")

	file  = open('newdata', 'a+') #where file_object is the variable to add the file object. 
	if(str2bool(str(predict2))):
		file.write('Ham,'+par+'\n')
	else:
		file.write('Spam,'+par+'\n')
	file.close()

	return str(predict2)[1]

run(host='localhost', port=5000, debug=True)
