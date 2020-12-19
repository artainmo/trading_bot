#include "crypto.h"

/*
** Example of what arguments to write when buying and selling cryptos
** A BUY 100€ BTC
** A SELL 115€ 100% BTC
** A ADD 200€ Coinbase
*/

static void	ft_cat(char const *s1, char *str, int *i)
{
	while (s1[*i])
	{
		str[*i] = s1[*i];
		*i = *i + 1;
	}
}

static char		*ft_strjoin_f(char *s1, char *s2)
{
	char	*str;
	int		i;
	int		l;

	i = 0;
	l = 0;
	if (!s1 && !s2)
		return (0);
	if (!s1)
		return (ft_strdup(s2));
	if (!s2)
		return (ft_strdup(s1));
	if (!(str = malloc(sizeof(char) * (ft_strlen(s1) + ft_strlen(s2) + 1))))
		return (0);
	ft_cat(s1, str, &i);
	while (s2[l])
	{
		str[i + l] = s2[l];
		l++;
	}
	free(s1);
	str[i + l] = '\0';
	return (str);
}

int error_management(int argc)
{
  if (argc != 5 && argc != 6)
  {
    printf("Wrong number of arguments\n");
    return (1);
  }
  return (0);
}

char *ft_join_double_str(char **argv)
{
	char *phrase;
	int i;

	i = 2;
	phrase = NULL;
	while(argv[i])
	{
		phrase = ft_strjoin_f(phrase, argv[i]);
		phrase = ft_strjoin_f(phrase, " ");
		i++;
	}
	i = ft_strlen(phrase) - 1;
	phrase[i] = '\n';
	return (phrase);
}

int open_fd(char *portfolio)
{
	int fd;
	char *tmp;

	portfolio = ft_strjoin(portfolio, "_trade_log.txt");
	tmp = portfolio;
	portfolio = ft_strjoin("trade_logs/", portfolio);
	free(tmp);
	fd = open(portfolio, O_CREAT|O_RDWR|O_APPEND, 0666);
	if (fd == -1)
		printf("Error during file opening");
	return (fd);
}

char *number_lines(int fd)
{
	int lines_counter;
	char *line;

	lines_counter = 0;
	while(get_next_line(fd, &line) > 0)
		lines_counter++;
	line = ft_strjoin(ft_itoa(lines_counter), ": ");
	return (line);
}

void write_to_file(int fd, char **argv)
{
	char *phrase;
	char *number;

	number = number_lines(fd);
	write(fd, number, ft_strlen(number));
	phrase = ft_join_double_str(argv);
	write(fd, phrase, ft_strlen(phrase));
}

int main(int argc, char **argv)
{
	int fd;

	if (error_management(argc))
    return (0);
	if ((fd = open_fd(argv[1])) == -1)
		return (0);
	write_to_file(fd, argv);
	return (0);
}
