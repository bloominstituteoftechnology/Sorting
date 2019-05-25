The length of the initial loop range has to be set to the length minus one (Array length - 1)
or else we will get an out of bounds error. This happens because our second loop in smallest index list
looks at the next index of the Array passed into our function.
