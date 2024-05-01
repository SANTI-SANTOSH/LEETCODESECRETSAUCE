in Twosum problem, better to create an empty hashmap
Now check through iteration if target-array[0], available in hashmap, obviously NO, so add array[0] with index 0
Now go over element by element in array and if it's already not there in hashmap, add it to hashmap with index.
When target e.g.4, and array element e.g. 2, 4-2=2 if already available in hashmap, provide result as index of available number and value
