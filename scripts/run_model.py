# Authors: The scikit-learn developers
# SPDX-License-Identifier: BSD-3-Clause

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

def run_model(x, y):
	X = x
	Y = y

	pca = PCA()
	scaler = StandardScaler()
	linear_reg = LinearRegression()
	pipe = Pipeline(steps=[("scaler", scaler), ("pca", pca), ("linear_reg", linear_reg)])

	param_grid = {
    	"pca__n_components": [2, 3, 4, 5, 6, 7, 8, 9, 10],
	}

	search = GridSearchCV(pipe, param_grid, n_jobs=2)
	search.fit(X, Y)

	best_score = search.best_score_
	best_params = search.best_params_

	print("REGRESSION RESULTS: Best parameter (CV score=%0.3f):" % search.best_score_)
	print(search.best_params_)

	return best_score, best_params
