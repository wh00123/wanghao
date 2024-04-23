class SeqString:
    def __init__(self, init_str=None):
        if init_str:
            self.str = list(init_str)
        else:
            self.str = []

    def __str__(self):
        return ''.join(self.str)

    def __len__(self):
        return len(self.str)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return SeqString(''.join(self.str[index]))
        else:
            return self.str[index]

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            self.str[index] = list(value)
        else:
            self.str[index] = value

    def __eq__(self, other):
        if isinstance(other, SeqString):
            return self.str == other.str
        else:
            return False

    def __add__(self, other):
        return SeqString(str(self) + str(other))

    def __mul__(self, times):
        return SeqString(str(self) * times)


# Create a SeqString object
s = SeqString()

# Insert 1, 2, 3, 4, 5, 6 into the SeqString object using the extend method
s.str.extend(['1', '2', '3', '4', '5', '6'])

# Reverse the SeqString object using the reverse method
s.str.reverse()

# Remove the last element of the SeqString object using the pop method
s.str.pop()

# Insert '7' at index 3 using the insert method
s.str.insert(3, '7')

# Replace the element at index 2 with '8' using indexing and assignment
s.str[2] = '8'

# Print the SeqString object to verify the operations
print(s)
