#include "linearAdd.hpp"

void linearAdd(const std::array<int, ARRAY_SIZE> &a,
	       const std::array<int, ARRAY_SIZE> &b,
	       std::array<int, ARRAY_SIZE> &c)
{
  size_t idx;

  #pragma omp parallel for
  for (idx = 0; idx < ARRAY_SIZE; idx++) {
    c[idx] = a[idx] + b[idx] * 2;
  }

}
