library(Matrix)

#Read in data
data2 <- read.csv(file = 'data/all_seasons.csv')
players_data <- data2[data2$draft_round != "Undrafted", ]
players_data$draft_round <- as.numeric(players_data$draft_round)
players_data <- players_data[,c("net_rating", "age", "player_height", "player_weight", "pts", "reb", "ast","oreb_pct","dreb_pct","usg_pct","ts_pct","ast_pct")]

X <- cbind(1, as.matrix(players_data[, 2:12]))
y <- players_data[, 1]
XX <- crossprod(X)
XX.lu <- expand(lu(XX))
L <- XX.lu$L
U <- XX.lu$U
P <- XX.lu$P
bs <- forwardsolve(L, crossprod(P, crossprod(X, y)))
betahat <- backsolve(U, bs)
betahat