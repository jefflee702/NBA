import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA

nba_df = pd.read_csv('all_seasons.csv')
nba_df

nba_df['draft_round'] = nba_df['draft_round'].apply(lambda x: 'undrafted' if x == 'undrafted' else 'drafted')
nba_df['draft_number'] = nba_df['draft_number'].apply(lambda x: 'undrafted' if x == 'undrafted' else 'drafted')

X = nba_df[['player_height', 'player_weight', 'draft_round', 'draft_number',
            'net_rating', 'oreb_pct', 'dreb_pct', 'usg_pct',
            'ts_pct', 'ast_pct', 'college', 'team_abbreviation', 'country', 'draft_year']]

le = LabelEncoder()
X['draft_round'] = le.fit_transform(X['draft_round'])
X['draft_number'] = le.fit_transform(X['draft_number'])
X['college'] = le.fit_transform(X['college'].astype(str))
X['team_abbreviation'] = le.fit_transform(X['team_abbreviation'].astype(str))
X['country'] = le.fit_transform(X['country'].astype(str))
X['draft_year'] = le.fit_transform(X['draft_year'].astype(str))


numerical_cols = ['player_height', 'player_weight', 'net_rating', 'oreb_pct', 
                  'dreb_pct', 'usg_pct', 'ts_pct', 'ast_pct']
X[numerical_cols] = StandardScaler().fit_transform(X[numerical_cols])

# Perform PCA
pca = PCA(n_components=10)
principal_components = pca.fit_transform(X)

# explained variance of each principal component
explained_variance = pca.explained_variance_ratio_
print("Explained variance: ", explained_variance)

# Identify the top factors
loadings = pd.DataFrame(pca.components_.T, columns=['PC1', 'PC2', 'PC3', 'PC4', 'PC5', 
                                                    'PC6', 'PC7', 'PC8', 'PC9', 'PC10'], 
                        index=X.columns)
print("Loadings: \n", loadings)

# Get the top three factors
top_factors = loadings.abs().sum(axis=1).nlargest(3).index
print("Top three factors: ", top_factors)

# Create a scatter plot to visualize the first two principal components
import matplotlib.pyplot as plt
plt.scatter(principal_components[:, 0], principal_components[:, 1])
plt.xlabel('PC1 ({}%)'.format(round(explained_variance[0]*100, 2)))
plt.ylabel('PC2 ({}%)'.format(round(explained_variance[1]*100, 2)))
plt.show()

# Create a scree plot to visualize the explained variance of each principal component
n_components = len(explained_variance)
plt.plot(range(1, n_components + 1), explained_variance, 'o-', label='Explained variance')
plt.plot(range(1, n_components + 1), explained_variance.cumsum(), 'o-', label='Cumulative explained variance')
plt.xlabel('Number of principal components')
plt.ylabel('Explained variance ratio')
plt.legend()
plt.show()

# Encode 'undrafted' values in draft_round and draft_pick columns as a separate category
nba_df['draft_round'] = nba_df['draft_round'].apply(lambda x: 'undrafted' if x == 'undrafted' else 'drafted')
nba_df['draft_number'] = nba_df['draft_number'].apply(lambda x: 'undrafted' if x == 'undrafted' else 'drafted')

# Extract the features we want to use for PCA and standardize the data
X = nba_df[['player_height', 'player_weight', 'draft_round', 'draft_number',
            'net_rating', 'oreb_pct', 'dreb_pct', 'usg_pct',
            'ts_pct', 'ast_pct', 'college', 'team_abbreviation', 'country', 'draft_year']]

# Encode categorical variables using label encoding
le = LabelEncoder()
X['draft_round'] = le.fit_transform(X['draft_round'])
X['draft_number'] = le.fit_transform(X['draft_number'])
X['college'] = le.fit_transform(X['college'].astype(str))
X['team_abbreviation'] = le.fit_transform(X['team_abbreviation'].astype(str))
X['country'] = le.fit_transform(X['country'].astype(str))
X['draft_year'] = le.fit_transform(X['draft_year'].astype(str))

# Standardize numerical variables
numerical_cols = ['player_height', 'player_weight', 'net_rating', 'oreb_pct', 
                  'dreb_pct', 'usg_pct', 'ts_pct', 'ast_pct', 'draft_year']
X[numerical_cols] = StandardScaler().fit_transform(X[numerical_cols])

# Perform PCA
pca = PCA(n_components=14)
principal_components = pca.fit_transform(X)

# Look at the explained variance of each principal component
explained_variance = pca.explained_variance_ratio_
print("Explained variance: ", explained_variance)

# Identify the top factors
loadings = pd.DataFrame(pca.components_.T, columns=['PC1', 'PC2', 'PC3', 'PC4', 'PC5', 
                                                    'PC6', 'PC7', 'PC8', 'PC9', 'PC10', 
                                                    'PC11', 'PC12', 'PC13', 'PC14'], 
                        index=X.columns)
print("Loadings: \n", loadings)

# Get the top three factors
top_factors = loadings.abs().sum(axis=1).nlargest(3).index
print("Top three factors: ", top_factors)

# Create a scatter plot to visualize the first two principal components
import matplotlib.pyplot as plt
plt.scatter(principal_components[:, 0], principal_components[:, 1])
plt.xlabel('PC1 ({}%)'.format(round(explained_variance[0]*100, 2)))
plt.ylabel('PC2 ({}%)'.format(round(explained_variance[1]*100, 2)))
plt.show()

# Create a scree plot to visualize the explained variance of each principal component
n_components = len(explained_variance)
plt.plot(range(1, n_components + 1), explained_variance, 'o-', label='Explained variance')
plt.plot(range(1, n_components + 1), explained_variance.cumsum(), 'o-', label='Cumulative explained variance')
plt.xlabel('Number of principal components')
plt.ylabel('Explained variance ratio')
plt.legend()
plt.show()

# Create a loading plot
fig, ax = plt.subplots(figsize=(10,6))

# Plot the loadings for the first three principal components
for i, column in enumerate(loadings.columns[:3]):
    ax.arrow(0, 0, loadings.loc['player_height', column], loadings.loc['player_weight', column], 
             head_width=0.1, head_length=0.1, fc='r', ec='r')
    ax.text(loadings.loc['player_height', column]*1.1, loadings.loc['player_weight', column]*1.1, 
            X.columns[0], color='r')
    ax.arrow(0, 0, loadings.loc['draft_round', column], loadings.loc['draft_number', column], 
             head_width=0.1, head_length=0.1, fc='b', ec='b')
    ax.text(loadings.loc['draft_round', column]*1.1, loadings.loc['draft_number', column]*1.1, 
            'Draft', color='b')
    ax.arrow(0, 0, loadings.loc['net_rating', column], loadings.loc['oreb_pct', column], 
             head_width=0.1, head_length=0.1, fc='g', ec='g')
    ax.text(loadings.loc['net_rating', column]*1.1, loadings.loc['oreb_pct', column]*1.1, 
            'Rating/Rebound', color='g')
    ax.arrow(0, 0, loadings.loc['dreb_pct', column], loadings.loc['usg_pct', column], 
             head_width=0.1, head_length=0.1, fc='c', ec='c')
    ax.text(loadings.loc['dreb_pct', column]*1.1, loadings.loc['usg_pct', column]*1.1, 
            'Defense/Usage', color='c')
    ax.arrow(0, 0, loadings.loc['ts_pct', column], loadings.loc['ast_pct', column], 
             head_width=0.1, head_length=0.1, fc='m', ec='m')
    ax.text(loadings.loc['ts_pct', column]*1.1, loadings.loc['ast_pct', column]*1.1, 
            'Shooting/Assist', color='m')

    # Set limits for the plot
    plt.xlim(-0.0005, 0.0005)
    plt.ylim(-0.0005, 0.0005)

    # Add labels for each axis
    ax.set_xlabel('PC{}'.format(i+1))
    ax.set_ylabel('')

    # Add a title
    ax.set_title('Loading Plot for PC{} and Top Features'.format(i+1))

    plt.show()
    
    # Perform PCA
pca = PCA(n_components=11)
principal_components = pca.fit_transform(X)

# Get eigenvalues
eigenvalues = pca.explained_variance_

# Create a scree plot to visualize eigenvalues of each principal component
plt.plot(range(1, 12), eigenvalues, 'o-')
plt.xlabel('Number of principal components')
plt.ylabel('Eigenvalues')
plt.show()
