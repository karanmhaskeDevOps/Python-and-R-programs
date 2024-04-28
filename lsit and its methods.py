# karan,Python program for list and its methods

l0 = ["Python", "HTML", "CSS", "Node.js", "Rust"]
l1 = ["Next.js", "R"]

# Adding an item to the list
l1.append("Java")
print(l1)

# Removing an item from the list
l0.remove("CSS")
print(l0)

# List concatenation
l2 = l0 + l1
print(l2)

# List splicing
print(l2[1:3])
print(l2[:4])
print(l2[1:4:2])
print(l2[-3:-1])
