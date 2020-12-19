#include "crypto.h"
/*
** As first argument the portfolio name like A
** Second argument the trade history line
** Potential third argument to specify with what you want to compare
*/

float portfolio_total(t_p *portfolio)
{
  float total;

  total = 0;
  portfolio = portfolio->start;
  while(portfolio->next)
  {
    total = total + portfolio->price;
    portfolio = portfolio->next;
  }
  total = total + portfolio->price;
  return (total);
}

void show_portfolio(t_p *portfolio)
{
  printf("TOTAL: %.0f\n", portfolio_total(portfolio));
  portfolio = portfolio->start;
  while(portfolio->next)
  {
    printf("%s: %.0f\n", portfolio->currency, portfolio->price);
    portfolio = portfolio->next;
  }
  printf("%s: %.0f\n", portfolio->currency, portfolio->price);
}

t_p *new_struct(t_p *portfolio, char *crypto)
{
  portfolio->next = malloc(sizeof(t_p));
  portfolio->next->start = portfolio->start;
  portfolio->next->currency = crypto;
  portfolio->next->next = NULL;
  portfolio->next->price = 0;
  return (portfolio->next);
}

t_p *goto_crypto(t_p *portfolio, char *crypto)
{
  portfolio = portfolio->start;
  while(portfolio->next && strcmp(portfolio->currency, crypto))
    portfolio = portfolio->next;
  if (strcmp(portfolio->currency, crypto))
    portfolio = new_struct(portfolio, crypto);
  return (portfolio);
}

t_p *ft_buy(char **words, t_p *portfolio)
{
  portfolio = goto_crypto(portfolio, words[3]);
  portfolio->price = portfolio->price + atof(words[2]);
  portfolio = portfolio->start;
  while(portfolio && strcmp(portfolio->currency, "EUR"))
    portfolio = portfolio->next;
  portfolio->price = portfolio->price - atof(words[2]);
  return (portfolio);
}

t_p *ft_sell(char **words, t_p *portfolio)
{
  portfolio = goto_crypto(portfolio, words[4]);
  portfolio->price = portfolio->price - (portfolio->price * (atof(words[3])/100));
  portfolio = portfolio->start;
  while(strcmp(portfolio->currency, "EUR"))
    portfolio = portfolio->next;
  portfolio->price = portfolio->price + atof(words[2]);
  return (portfolio);
}

t_p *ft_add(char **words, t_p *portfolio)
{
  portfolio = goto_crypto(portfolio, "EUR");
  portfolio->price = portfolio->price + atof(words[2]);
  return (portfolio);
}

t_p *parse_line(char *line, t_p *portfolio)
{
  char **words;

  words = ft_split(line, ' ');
  if (!strcmp(words[1], "ADD"))
    portfolio = ft_add(words, portfolio);
  else if (!strcmp(words[1], "SELL"))
    portfolio = ft_sell(words, portfolio);
  else if (!strcmp(words[1], "BUY"))
    portfolio = ft_buy(words, portfolio);
  else
  {
    printf("ERROR, line %s non-existing command\n", words[0]);
    return (0);
  }
  return (portfolio);
}

int get_fd(char **argv)
{
  char *portfolio;
  char *tmp;
  int fd;

  portfolio = ft_strjoin("trade_logs/", argv[1]);
  tmp = portfolio;
  portfolio = ft_strjoin(portfolio, "_trade_log.txt");
  free(tmp);
  if ((fd = open(portfolio, O_RDWR, 0666)) == -1)
    printf("Portfolio does not exist\n");
  return (fd);
}

t_p *init_struct(t_p *portfolio)
{
  portfolio = malloc(sizeof(t_p));
  portfolio->start = portfolio;
  portfolio->currency = ft_strdup("EUR");
  portfolio->next = NULL;
  portfolio->price = 0;
  return (portfolio);
}

int main(int argc, char **argv)
{
  char *line;
  int fd;
  int lines;
  int comp;
  t_p *portfolio;

  if (argc != 3 && argc != 4)
  {
    printf("Wrong number of arguments\n");
    return (0);
  }
  lines = atof(argv[2]) + 1;
  if (argc == 3)
    comp = 2;
  else
    comp = lines - atof(argv[3]);
  portfolio = NULL;
  portfolio = init_struct(portfolio);
  if ((fd = get_fd(argv)) == -1)
    return (0);
  while(lines)
  {
    if (get_next_line(fd, &line) <= 0)
    {
      printf("Error during file reading\n");
      return (0);
    }
    if (!(portfolio = parse_line(line, portfolio)))
      return (0);
    if (lines == comp)
      show_portfolio(portfolio);
    lines--;
  }
  printf("||\n");
  show_portfolio(portfolio);
  return (1);
}
