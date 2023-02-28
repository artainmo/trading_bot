#include "crypto.h"

int error_management(int argc)
{
  if (system("clear") !=  0)
  {
    printf("An error has occured in the shell\n");
    return (1);
  }
  if (argc != 3)
  {
    printf("Wrong number of arguments\n");
    return (1);
  }
  return (0);
}

int main(int argc, const char **argv)
{
	float from;
	float to;
	float profit;

	if (error_management(argc))
    return (0);
	from = atof(argv[1]);
	to = atof(argv[2]);
	if (from < to)
	{
		profit = ((to/from)*100);
		printf("This is the made profit: %f%%\n", profit);
	}
	else
	{
		profit = ((from/to)*100);
		printf("This is the made loss: %f%%\n", profit);
	}
	return (0);
}
