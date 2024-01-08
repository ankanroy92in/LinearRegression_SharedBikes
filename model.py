from sklearn.model_selection import train_test_split
# Libraries for model creation, training and calculating VIF(for Multicollinearity)
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

bikes_train, bikes_test = train_test_split(bikes,train_size=0.7,test_size=0.3,random_state=100)
y_train = bikes_train.pop('cnt')
X_train = bikes_train

y_test = bikes_test.pop('cnt')
X_test = bikes_test


# Function to create model
def model_creation(X,y):
    model = sm.OLS(y,X).fit()
    print(model.summary())
    return model


# Function to calculate VIF
def vif_calculator (X):
    vif = pd.DataFrame()
    vif['Variables'] = X.columns
    vif['VIF'] = [variance_inflation_factor(X.values,i) for i in range(X.shape[1])]
    vif = vif.sort_values(by = "VIF", ascending = False)
    print(vif)