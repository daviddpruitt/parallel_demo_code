#pragma once
#include <cstddef>
#include <iostream>
#include <array>

#define ARRAY_SIZE 10240

using namespace std;

void linearAdd(const std::array<int, ARRAY_SIZE> &a,
	       const std::array<int, ARRAY_SIZE> &b,
	       std::array<int, ARRAY_SIZE> &c);
