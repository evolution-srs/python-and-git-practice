# Hands on Lab, Sets

# Sets in Python is a data structure that stores an unordered collection of unique items.

# --- Key Characteristics of Sets ---
# 1. Unordered: Items in a set do not have a defined order. You cannot access items by index.
# 2. Unique: Sets do not allow duplicate elements.
# 3. Mutable: You can add or remove items from a set. However, the elements themselves must be immutable (e.g., numbers, strings, tuples).

# --- Creating a Set ---

# Create a set from a list of items
album_list = ["Michael Jackson", "Thriller", 1982, "Pop", 1, 42.4, 66, "30-Nov-82"]
album_set = set(album_list)
print("Original list:", album_list)
print("Converted set:", album_set) # Notice the order might change and duplicates (if any) would be removed.

# Create a set directly with curly braces
music_genres = {"Pop", "Rock", "Soul", "Hard Rock", "R&B", "Pop"}
print("\nMusic genres set:", music_genres) # Notice "Pop" only appears once.

# --- Set Operations ---

# Let's define two sets
set_A = {"AC/DC", "Back in Black", "Thriller"}
set_B = {"AC/DC", "Back in Black", "The Dark Side of the Moon"}

# Add an element to a set
print("\nOriginal Set A:", set_A)
set_A.add("NSYNC")
print("Set A after adding 'NSYNC':", set_A)

# Remove an element from a set
# .remove() will raise an error if the item doesn't exist.
set_A.remove("NSYNC")
print("Set A after removing 'NSYNC':", set_A)

# .discard() will NOT raise an error if the item doesn't exist.
set_A.discard("Made up band") # No error

# Verify if an element is in the set
print("\nIs 'AC/DC' in Set A?", "AC/DC" in set_A)
print("Is 'Who?' in Set A?", "Who?" in set_A)

# --- Set Logic Operations ---

# Intersection: Find elements that are in both sets
intersection_set = set_A & set_B
print("\nIntersection of A and B:", intersection_set)
# Alternative method:
# intersection_set = set_A.intersection(set_B)

# Union: Combine all unique elements from both sets
union_set = set_A.union(set_B)
print("Union of A and B:", union_set)

# Alternative method (using the | operator):
# union_set = set_A | set_B

# Difference: Find elements that are in set_A but NOT in set_B
difference_set = set_A.difference(set_B)
print("Difference (A - B):", difference_set)
# Alternative method (using the - operator):
# difference_set = set_A - set_B

# Symmetric Difference: Find elements that are in either set, but NOT in both
symmetric_diff_set = set_A.symmetric_difference(set_B)
print("Symmetric Difference of A and B:", symmetric_diff_set)
# Alternative method (using the ^ operator):
# symmetric_diff_set = set_A ^ set_B

# --- Subsets and Supersets ---

# Check if a set is a subset of another
# Is {"Back in Black", "AC/DC"} a subset of set_A?
print("\nIs {'Back in Black', 'AC/DC'} a subset of A?", {"Back in Black", "AC/DC"}.issubset(set_A))

# Check if a set is a superset of another
# Is set_A a superset of {"Back in Black", "AC/DC"}?
print("Is A a superset of {'Back in Black', 'AC/DC'}?", set_A.issuperset({"Back in Black", "AC/DC"}))

# --- Use Case: Finding Unique Items ---

email_list = ["user1@example.com", "user2@example.com", "user1@example.com", "user3@example.com"]
unique_emails = set(email_list)
print(f"\nFound {len(unique_emails)} unique email addresses.")
print(unique_emails)


# --- Understanding Set .add() vs. Dictionary Assignment ---

# Question: V={'A','B'}, what is the result of V.add('C')?
# IMPORTANT: V={'A','B'} creates a SET, not a dictionary, because it lacks key:value pairs.
# The .add() method is for sets.
V={'A','B'}
V.add('C')
# The arrangement is NOT guaranteed. Sets are UNORDERED.
# The output could be {'A', 'C', 'B'} or {'C', 'A', 'B'}, etc.
print(V)

visitors = {'user123', 'user456'}
visitors.add('user789')
print(visitors)

# For comparison: How to add to a DICTIONARY
# Dictionaries use key:value pairs and maintain insertion order (since Python 3.7).
print("\n--- Dictionary Example ---")
user_ages = {'user123': 34, 'user456': 28}
print("Original dictionary:", user_ages)
# You add items using key assignment, not .add()
user_ages['user789'] = 41
print("Dictionary after adding an item:", user_ages)