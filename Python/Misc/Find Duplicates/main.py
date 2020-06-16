# Finds duplicates in an array and returns an array with duplicated values
def find_dupes(s1):
    # Define seen values and duplicates return array
    seen = set()
    dupes = []

    # Loop through all values in array
    for val in s1:
        # Value not already seen in set, add it to set
        if val not in seen:
            seen.add(val)
        # Value already seen in set
        else:
            # If value is not in duplicates array already, add it
            if val not in dupes:
                dupes.append(val)
    return dupes

if __name__ == '__main__':
    # Define array and print which numbers are duplicates
    s1 = [5, 10, 14, 23, 45, 98, 10, 10, 234, 14, 23, 23, 23, 5, 10, 42]
    print(find_dupes(s1))
