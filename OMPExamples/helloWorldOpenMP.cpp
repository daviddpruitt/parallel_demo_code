#include <iostream>
#include <omp.h>

int main(int argc, char **argv)
{
  #pragma omp parallel
  {
    std::cout << "Hello world";
    std::cout << "from thread " << omp_get_thread_num() << " of ";
    std::cout << omp_get_num_threads() << std::endl;
  }
}
