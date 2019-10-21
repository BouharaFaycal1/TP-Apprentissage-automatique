head(iris)
names(iris) <- c("Sepal.Length", "Sepal.Width", "Petal.Length",
                 "Petal.Width", "Species")
head(iris)
iris
library(ggvis)

install.packages("ggvis")
library(ggvis)
iris %>% ggvis(~Sepal.Length, ~Sepal.Width, fill = ~Species) %>%
  layer_points()
#cette figure nous dit que ya deux class d'espéces 1ere class qui contient 
#l'espéce setosa et la 2éme class qui contients les deux éspéce versicolor et virginica 
#nous remerquons dans cette figures que lespéce setosa est plus grande dans la largeur
#de sepal et plus petite e,n longeur de sépale 
# contrairemnt aux 2 éspece versicolor et virginica qui sont plus grnade en longeur de sépal 

iris %>% ggvis(~Petal.Length, ~Petal.Width, fill = ~Species) %>%
  layer_points()

#dans cette figure on pourra differencié 3 class 
#lespéce setosa est plus petite en largeur et en longeur de pétal 
#l'espèce versicolor et plus grande que virginica en largeur de pétal 
#virginica est plus grande en largeur et en longeur de pétal 
#par contre on remarque deeux point d'extrimité entre les deux espéce virginica et versicolor
cor(iris$Petal.Length, iris$Petal.Width)
cor(iris$Petal.Length, iris$Petal.Width)
#la correlation est 0.96 positive car lorsqu'une variable augmente, 
#l'autre variable augmente aussi.

x=levels(iris$Species)
print(x[1])
cor(iris[iris$Species==x[1],1:4])

print(x[2])
cor(iris[iris$Species==x[2],1:4])

print(x[3])
cor(iris[iris$Species==x[3],1:4])
#la corrélation 
#Setosa: on remarque y'a un fort lien de laison entre le longeur de sépal 
#et la largeur de sépal contrairement au longeur de petal et la largeur de sépal qui sont moins liées 

#versicolor 
#virginica
table(iris$Species)
round(prop.table(table(iris$Species)) * 100, digits = 1)
set.seed(1234)
ind <- sample(2, nrow(iris), replace=TRUE, prob=c(0.67, 0.33))

iris.training <- iris[ind==1, 1:4]
iris.test <- iris[ind==2, 1:4]


iris.trainLabels <- iris[ind==1,5]
iris.testLabels <- iris[ind==2,5]
print(iris.trainLabels)


install.packages("class")
library(class)
#apprentissage n'utilise pas les étiquette 
iris_pred <- knn(train = iris.training, test = iris.test, cl =
                   iris.trainLabels, k=3)
iris_pred
irisTestLabels <- data.frame(iris.testLabels)

merge <- data.frame(iris_pred, iris.testLabels)
names(merge) <- c("Predicted Species", "Observed Species")
merge
#on a 150 espèce on teste 40 on remarque a la 29 ya une erreur 

#nbr erreur /ndecision * 100 
#1/40 * 100 = 2.5
