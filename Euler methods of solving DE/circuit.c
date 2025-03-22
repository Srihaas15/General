#include <stdio.h>
#include <math.h>

#define V 10.0 
#define dt 0.001    

void euler(int steps, double R, double L, double alpha, double T, FILE *file) {
    double i = 0.0, v, di, tau = L / R;
    for (int n = 0; n < steps; n++) {
        double t = n * dt;
        if (fmod(t, T) < alpha * T) {
            v = V;
        } else {
            v = 0;
        }

        if (t < tau) {
            di = (v - R * i) / L;
            i = i + dt * di;
        }

        fprintf(file, "euler: t = %.3f s, i = %.5f A\n", t, i);
    }
}

void backeuler(int steps, double R, double L, double alpha, double T, FILE *file) {
    double i = 0.0, v, tau = L / R;
    for (int n = 0; n < steps; n++) {
        double t = n * dt;
        if (fmod(t, T) < alpha * T) {
            v = V;
        } else {
            v = 0;
        }

        if (t < tau) {
            i = (i + dt * v / L) / (1 + dt * R / L);
        } else if (fabs(t - tau) < 1e-6) {
            i = (i + dt * v / L) / (1 + dt * R / L);
        } else {
            i = (v / R) * (1 - exp(-t / tau));
        }

        fprintf(file, "backeuler: t = %.3f s, i = %.5f A\n", t, i);
    }
}

int main() {
    double R, L, a, T;
    int steps;
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        printf("Error opening file for writing.\n");
        return 1;
    }

    printf("Enter R, L, alpha, T: ");
    scanf("%lf %lf %lf %lf", &R, &L, &a, &T);

    if (a > 1 || a < 0) {
        printf("Enter valid alpha.\n");
        fclose(file);
        return 0;
    }

    steps = (int)(2 * T / dt);

    euler(steps, R, L, a, T, file);
    fprintf(file, "\n");
    backeuler(steps, R, L, a, T, file);

    fclose(file);
    return 0;
}

