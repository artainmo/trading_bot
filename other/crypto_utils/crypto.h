#ifndef CRYPTO_H
#define CRYPTO_H

typedef struct s_portfolio
{
  char *currency;
  float price;
  struct s_portfolio *next;
  struct s_portfolio *start;
} t_p;

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include "utils/get_next_line/get_next_line.h"
#include "utils/libft/libft.h"

#endif
