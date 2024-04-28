plot(1, 2)
plot(c(1, 9), c(3, 11))
plot(c(1, 2, 3, 4, 5), c(3, 7, 8, 9, 12))

x <- c(1, 2, 3, 4, 5)
y <- c(3, 7, 8, 9, 12)

plot(1:10)

plot(1:10, type="l")

plot(1:10, type="l", main="My Graph", xlab="The x-axis", ylab="The y axis")

plot(1:10, col="red")

plot(1:10, type="l", col="blue")

plot(1:10, type="l", lwd=6)

plot(1:10, type="l", lwd=5, lty=9)

plot(1:10, cex=3)

plot(1:10, pch=25, cex=2)


#multiple line
line1 <- c(1,2,3,4,5,10)
line2 <- c(2,5,7,8,9,10)
plot(line1, type = "l", col = "blue")
lines(line2, type="l", col = "red")



#scatterplot
x <- c(5,7,8,7,2,2,9,4,11,12,9,6)
y <- c(99,86,87,88,111,103,87,94,78,77,85,86)
plot(x, y, main="Observation of Cars", xlab="Car age", ylab="Car speed")



# day one, the age and speed of 12 cars:
x1 <- c(5,7,8,7,2,2,9,4,11,12,9,6)
y1 <- c(99,86,87,88,111,103,87,94,78,77,85,86)

# day two, the age and speed of 15 cars:
x2 <- c(2,2,8,1,15,8,12,9,7,3,11,4,7,14,12)
y2 <- c(100,105,84,105,90,99,90,95,94,100,79,112,91,80,85)

plot(x1, y1, main="Observation of Cars", xlab="Car age", ylab="Car speed", col="red", cex=2)
points(x2, y2, col="blue", cex=2)


##Pie Chart
# Create a vector of pies
x <- c(10,20,30,40)
# Display the pie chart
pie(x)

######
# Create a vector of pies
x <- c(10,20,30,40)
# Create a vector of labels
mylabel <- c("Apples", "Bananas", "Cherries", "Dates")
# Display the pie chart with labels
pie(x, label = mylabel, main = "Fruits")


# Create a vector of colors
colors <- c("blue", "yellow", "green", "black")

# Display the pie chart with colors
pie(x, label = mylabel, main = "Fruits", col = colors)



######
# Create a vector of labels
mylabel <- c("Apples", "Bananas", "Cherries", "Dates")

# Create a vector of colors
colors <- c("blue", "yellow", "green", "black")

# Display the pie chart with colors
pie(x, label = mylabel, main = "Pie Chart", col = colors)

# Display the explanation box
legend("bottomright", mylabel, fill = colors)


########
# x-axis values
x <- c("A", "B", "C", "D")
# y-axis values
y <- c(12, 4, 6, 8)
barplot(y, names.arg = x)


###
x <- c("A", "B", "C", "D")
y <- c(2, 4, 6, 8)
barplot(y, names.arg = x, col = "red")

####
x <- c("A", "B", "C", "D")
y <- c(2, 4, 6, 8)
barplot(y, names.arg = x, horiz = TRUE)

