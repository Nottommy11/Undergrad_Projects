#include "cuda_runtime.h"
#include "device_launch_parameters.h"

#include <stdio.h>

// Kernel function
__global__ void vectorAdd(int * a, int * b, int * c) {
    int i = threadIdx.x;
    c[i] = a[i] + b[i];

    return;
}

int main() {

    int a[] = {1,2,3, 4,5,6, 7,8,9, 10,11,12, 13, 14, 15, 16, 17, 18};
    int b[] = {4,5,6, 7,8,9, 10,11,12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22};

    int c[sizeof(a)/sizeof(int)] = {0};

    // CPU example
    /*
    for(int i = 0; i < sizeof(c)/sizeof(int); i++) {
        c[i] = a[i] + b[i];
    }

    return;
     */

    // GPU example
    // Create pointers into the GPU memory
    int * cudaA = 0;
    int * cudaB = 0;
    int * cudaC = 0;

    // Allocate memory on the GPU
    cudaMalloc(&cudaA, sizeof(a));
    cudaMalloc(&cudaB, sizeof(b));
    cudaMalloc(&cudaC, sizeof(c));

    // Copy data from the CPU to the GPU
    cudaMemcpy(cudaA, a, sizeof(a), cudaMemcpyHostToDevice);
    cudaMemcpy(cudaB, b, sizeof(b), cudaMemcpyHostToDevice);

    // Launch the kernel
    // vectorAdd<<<GRID_SIZE, BLOCK_SIZE>>>(cudaA, cudaB, cudaC);
    vectorAdd<<<1, sizeof(a)/sizeof(int)>>>(cudaA, cudaB, cudaC);

    // Copy data from the GPU to the CPU
    cudeMemcpy(c, cudaC, sizeof(c), cudaMemcpyDeviceToHost);

    return;
}
