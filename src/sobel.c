// sobel.c

#include "sobel.h"
#include <stdlib.h>

void sobel_edge_detection_c(unsigned char *input, unsigned char *result, int width, int height)
{
    // sobel edge detection kernel
    int sobel_kernel_x[3][3] = {
        {-1, 0, 1}, 
        {-2, 0, 2}, 
        {-1, 0, 1}
    };

    int sobel_kernel_y[3][3] = {
        {-1, -2, -1}, 
        {0, 0, 0}, 
        {1, 2, 1}
    };

    // apply Sobel edge detection
    for (int y = 1; y < height - 1; ++y)
    {
        for (int x = 1; x < width - 1; ++x)
        {
            int gx = 0, gy = 0;

            // convolution with sobel kernels
            for (int ky = 0; ky < 3; ++ky)
            {
                for (int kx = 0; kx < 3; ++kx)
                {
                    int pixel_value = input[(y + ky - 1) * width + (x + kx - 1)];
                    gx += sobel_kernel_x[ky][kx] * pixel_value;
                    gy += sobel_kernel_y[ky][kx] * pixel_value;
                }
            }

            // compute gradient magnitude
            int gradient_magnitude = abs(gx) + abs(gy);

            // ensure the value is within 0-255
            result[y * width + x] = (unsigned char)(gradient_magnitude > 255 ? 255 : gradient_magnitude);
        }
    }
}
