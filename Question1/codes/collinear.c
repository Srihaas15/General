#include <stdio.h>
#include <stdlib.h>
#include "libs/matfun.h"
#include "libs/geofun.h"

// Function to calculate p and generate intermediate points
void calculate_p(double *p, double points[5][2]) {
    // Fixed points: (2, 1), (p, -1), (-1, 3)
    double x1 = 2.0, y1 = 1.0;
    double x3 = -1.0, y3 = 3.0;

    // Create a matrix to check collinearity
    double **matrix = createMat(3, 3);
    matrix[0][0] = x1; matrix[0][1] = y1; matrix[0][2] = 1.0; // Point (2, 1)
    matrix[1][0] = *p; matrix[1][1] = -1.0; matrix[1][2] = 1.0; // Point (p, -1)
    matrix[2][0] = x3; matrix[2][1] = y3; matrix[2][2] = 1.0; // Point (-1, 3)

    // Calculate the rank of the matrix
    int rank = 3; // Assume full rank initially

    // Perform Gaussian elimination to find the rank
    for (int i = 0; i < 3; i++) {
        // Check if the current row is zero
        if (matrix[i][0] == 0 && matrix[i][1] == 0 && matrix[i][2] == 0) {
            rank--;
            continue; // Skip zero rows
        }

        for (int j = i + 1; j < 3; j++) {
            if (matrix[j][i] != 0) {
                double ratio = matrix[j][i] / matrix[i][i];
                for (int k = 0; k < 3; k++) {
                    matrix[j][k] -= ratio * matrix[i][k];
                }
            }
        }
    }

    // Determine the value of p based on the rank
    if (rank < 3) {
        *p = (y3 - y1) / (x3 - x1) * (x3 - x1) + y1; // Calculate p based on line equation
    } else {
        *p = 5.0; // Default value if collinear
    }

    // Generate intermediate points
    for (int i = 0; i < 5; i++) {
        double t = (double)i / 4; // Generate 5 points
        points[i][0] = (1 - t) * x1 + t * x3; // x coordinate
        points[i][1] = (1 - t) * y1 + t * y3; // y coordinate
    }

    // Free allocated matrix memory
    for (int i = 0; i < 3; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

