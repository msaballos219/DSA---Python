from LCSMatrix import LCSMatrix

# LCSTestCase represents a test for LCSMatrix class functionality. Expected
# vs. actual LCS strings sets are compared and optionally the numerical
# matrices as well.
class LCSTestCase:
    def __init__(self, string1, string2, expected_LCSs,
        expected_LCS_matrix = [], test_matrix_only = False) :
        self.string1 = string1
        self.string2 = string2
        self.expected_LCS_set = expected_LCSs
        self.expected_matrix = expected_LCS_matrix
        self.matrix_only = test_matrix_only
    
    # Converts an LCSMatrix to a list of integer list, representing the
    # numerical matrix. Uses an LCSMatrix's get_eentry() method to retrieve
    # each entry.
    def convert_LCS_matrix(self, user_matrix):
        result = []
        for row_index in range(user_matrix.get_row_count()):
            row = []
            for col_index in range(user_matrix.get_column_count()):
                value = user_matrix.get_entry(row_index, col_index)
                row.append(value)
            result.append(row)
        return result
    
    def execute(self, test_feedback):
        # Build the LCSMatrix
        user_matrix = LCSMatrix(self.string1, self.string2)
        #
        # Get the set of longest common subsequences from the matrix
        actual = user_matrix.get_longest_common_subsequences()
        #
        # If this test case includes an expected matrix, then build the
        # numerical matrix from userMatrix and compare the result against the
        # expected matrix
        actual_matrix = []
        if len(self.expected_matrix) > 0:
            # Build the numerical matrix from the user's LCSMatrix object
            actual_matrix = self.convert_LCS_matrix(user_matrix)
            #
            # The test fails if the matrices are not equal
            if self.expected_matrix != actual_matrix:
                test_feedback.write(f"FAIL: \"{self.string1}\" and ")
                test_feedback.write(f"\"{self.string2}\"\n")
                #
                # Show expected and actual numerical matrices
                test_feedback.write("  Expected matrix:\n")
                self.print_matrix(test_feedback, self.expected_matrix, "    ")
                test_feedback.write("  Actual matrix:\n")
                self.print_matrix(test_feedback, actual_matrix, "    ")
                return False
        # Compare the expected and actual LCS sets
        passes = True
        if not self.matrix_only:
            if self.expected_LCS_set != actual:
                passes = False
        # Output final results
        test_feedback.write("PASS" if passes else "FAIL")
        test_feedback.write(f": \"{self.string1}\" and \"{self.string2}\"")
        if self.matrix_only:
            test_feedback.write(" (matrix generation only)")
        test_feedback.write("\n")
        if len(self.expected_matrix) > 0:
            # Show expected and actual numerical matrices
            test_feedback.write("  Expected matrix:\n")
            self.print_matrix(test_feedback, self.expected_matrix, "    ")
            test_feedback.write("  Actual matrix:\n")
            self.print_matrix(test_feedback, actual_matrix, "    ")
        if not self.matrix_only:
            test_feedback.write("  Expected LCS set:\n")
            test_feedback.write(f"    {self.expected_LCS_set}\n")
            test_feedback.write("  Actual LCS set:\n")
            test_feedback.write(f"    {actual}\n")
        return passes
    
    def print_matrix(self, test_feedback, matrix, indent=""):
        for row in matrix:
            test_feedback.write(f"{indent}{row}\n")