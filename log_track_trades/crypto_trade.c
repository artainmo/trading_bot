#include "crypto.h"

/*
** First arg currency in three letters and second arg its current price
*/

int error_management(int argc)
{
  if (system("clear") !=  0)
  {
    printf("An error has occured in the shell\n");
    return (1);
  }
  if (argc != 3)
  {
    printf("Wrong number of arguments\nFirst argument is abbreviated crypto name and second is current value\n");
    return (1);
  }
  return (0);
}

void get_opportunity_analysis(float current, float last_year_highest, float corona_financial_crisis_lowest)
{
  float potential_roi;

  potential_roi = (last_year_highest/current) * 100;
  printf("Realistic roi in the coming year: %f%%\n", potential_roi);
  if (potential_roi >= 400)
    printf("Potential roi above 400%% this is totally worth it\n");
  else if (potential_roi >= 300)
    printf("Potential roi above 300%% this is an interesting deal\n");
  else
    printf("Less than 300%% this is not particularly interesting\n");
  printf("Lowest during corona financial bear market: %f\n\n", corona_financial_crisis_lowest);
}

void test_cryptocurrencies(const char **argv)
{
  if (!strcmp("EOS", argv[1]))
    get_opportunity_analysis(atof(argv[2]), 7.9, 1.0);
  else if (!strcmp("BTC", argv[1]))
    get_opportunity_analysis(atof(argv[2]), 12193.0, 4024.0);
  else if (!strcmp("XRP", argv[1]))
    get_opportunity_analysis(atof(argv[2]), 0.45, 0.1157);
  else if (!strcmp("LTC", argv[1]))
    get_opportunity_analysis(atof(argv[2]), 128.59, 26.9);
  else if (!strcmp("ETH", argv[1]))
    get_opportunity_analysis(atof(argv[2]), 319.0, 92.21);
  else if (!strcmp("TRX", argv[1]))
    get_opportunity_analysis(atof(argv[2]), 0.0367, 0.0079);
  else if (!strcmp("BCH", argv[1]))
    get_opportunity_analysis(atof(argv[2]), 459, 134.76);
  else if (!strcmp("BSV", argv[1]))
    get_opportunity_analysis(atof(argv[2]), 396.23, 91.45);
  else if (!strcmp("OXT", argv[1]))
    get_opportunity_analysis(atof(argv[2]), 0.2968, 0.1088);
  else if (!strcmp("ATOM", argv[1]))
    get_opportunity_analysis(atof(argv[2]), 6.82, 1.85);
  else if (!strcmp("XLM", argv[1]))
    get_opportunity_analysis(atof(argv[2]), 0.1466, 0.0284);
  else if (!strcmp("XTZ", argv[1]))
    get_opportunity_analysis(atof(argv[2]), 3.65, 1);
  else if (!strcmp("ETC", argv[1]))
    get_opportunity_analysis(atof(argv[2]), 11.99, 3.71);
  else if (!strcmp("ZRX", argv[1]))
    get_opportunity_analysis(atof(argv[2]), 0.3499, 0.1151);
  else
      printf("Cryptocurrency not found\n");
}

int main(int argc, const char **argv)
{
  int ret;

  if (error_management(argc))
    return (0);
  else
    test_cryptocurrencies(argv);
  return (0);
}
