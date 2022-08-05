#include "linearAdd.hpp"

int main(int argc, char **argv)
{
  size_t idx;
  array<int, ARRAY_SIZE> a;
  array<int, ARRAY_SIZE> b;
  array<int, ARRAY_SIZE> c;

  a.fill(1);
  b.fill(1);
  c.fill(0);

  linearAdd(a, b, c);
  
  cout << "First 8 elements\n";
  for (idx = 0; idx < 8; idx++) {
    cout << c[idx] << " ";
  }

  cout << endl;
  
  cout << "Last 8 elements\n";
  for (idx = ARRAY_SIZE - 8; idx < ARRAY_SIZE; idx++) {
    cout << c[idx] << " ";
  }
  cout << endl;

  return 0;
}
