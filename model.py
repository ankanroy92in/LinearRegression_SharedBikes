from sklearn.model_selection import train_test_split

bikes_train, bikes_test = train_test_split(bikes,train_size=0.7,test_size=0.3,random_state=100)
y_train = bikes_train.pop('cnt')
X_train = bikes_train

y_test = bikes_test.pop('cnt')
X_test = bikes_test