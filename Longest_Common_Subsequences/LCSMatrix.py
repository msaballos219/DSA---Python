"""
The LCSMatrix class implements the Longest Common Subsequences (LCS) algorithm using dynamic programming.
It computes a matrix that represents the length of the LCS for substrings of two input strings and provides
methods to retrieve the matrix entries and the set of all distinct LCS.

Key Features:
1. Matrix Construction:
   - The matrix is built using a bottom-up dynamic programming approach.
   - Each cell stores the length of the LCS for substrings up to that point.
   - Rules:
     a) If characters match, matrix[R][C] = 1 + matrix[R-1][C-1].
     b) If not, matrix[R][C] = max(matrix[R-1][C], matrix[R][C-1]).

2. LCS Retrieval:
   - Uses backtracking to find all distinct LCS from the computed matrix.
   - Handles cases with multiple LCS or no common subsequences.

3. Methods:
   - `get_entry(row_index, column_index)`: Retrieves a specific matrix entry or 0 if out of bounds.
   - `get_longest_common_subsequences()`: Returns a set of all distinct LCS between the two strings.
   - `get_row_count()` and `get_column_count()`: Provide dimensions of the matrix.

This implementation handles edge cases such as empty strings and strings with no common characters.
"""


class LCSMatrix:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.row_count = len(str1)
        self.column_count = len(str2)
        self.matrix = [[0] * (self.column_count + 1) for _ in range(self.row_count + 1)]
        self._compute_matrix()

    def _compute_matrix(self):
        # Fill the matrix using dynamic programming
        for i in range(1, self.row_count + 1):
            for j in range(1, self.column_count + 1):
                if self.str1[i - 1] == self.str2[j - 1]:
                    self.matrix[i][j] = 1 + self.matrix[i - 1][j - 1]
                else:
                    self.matrix[i][j] = max(self.matrix[i - 1][j], self.matrix[i][j - 1])

    def get_entry(self, row_index, column_index):
        # Return matrix entry or 0 if indices are out of bounds
        if 0 <= row_index < self.row_count and 0 <= column_index < self.column_count:
            return self.matrix[row_index + 1][column_index + 1]
        return 0

    def get_longest_common_subsequences(self):
        # Backtrack to find all LCS
        lcs_set = set()
        self._find_lcs(self.row_count, self.column_count, "", lcs_set)
        return lcs_set

    def _find_lcs(self, i, j, current_lcs, lcs_set):
        # Base case: If we reach the top-left corner of the matrix
        if i == 0 or j == 0:
            if current_lcs:  # Only add non-empty LCS
                lcs_set.add(current_lcs[::-1])  # Add reversed LCS to the set
            return

        if self.str1[i - 1] == self.str2[j - 1]:
            # Characters match; move diagonally up-left
            self._find_lcs(i - 1, j - 1, current_lcs + self.str1[i - 1], lcs_set)
        else:
            # Move in the direction of the maximum value
            if i > 0 and self.matrix[i][j] == self.matrix[i - 1][j]:
                self._find_lcs(i - 1, j, current_lcs, lcs_set)
            if j > 0 and self.matrix[i][j] == self.matrix[i][j - 1]:
                self._find_lcs(i, j - 1, current_lcs, lcs_set)

    def get_row_count(self):
        return self.row_count

    def get_column_count(self):
        return self.column_count
