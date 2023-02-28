/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_decimal_to_hexadecimal_lowercase.c              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: artainmo <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/23 20:18:40 by artainmo          #+#    #+#             */
/*   Updated: 2019/11/23 20:56:47 by artainmo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
**Converts a decimal(10-base) into a hexadecimal(16-base),
**and puts the hexadecimal into a string,
**checks the precision flags and adds 0s in the string accordingly
*/

static int	ft_count_dec_to_hex(unsigned long i)
{
	int counter;

	counter = 0;
	while (i)
	{
		i = i / 16;
		counter++;
	}
	return (counter);
}

static void	ft_norm(int *remainder, unsigned long *s, int *i, char *temp_rev)
{
	*remainder = *s % 16;
	if (*remainder < 10)
		*remainder = *remainder + 48;
	else
		*remainder = *remainder + 87;
	temp_rev[*i] = *remainder;
	*i = *i + 1;
	*s = *s / 16;
}

char		*ft_dec_to_hexa(unsigned long s)
{
	char	*hexadecimal;
	char	*temp_rev;
	int		i;
	int		l;
	int		remainder;

	i = 0;
	l = 0;
	remainder = 0;
	if (!(temp_rev = malloc(sizeof(char) * ft_count_dec_to_hex(s))))
		return (0);
	if (!(hexadecimal = malloc(sizeof(char) * ft_count_dec_to_hex(s))))
		return (0);
	while (s)
		ft_norm(&remainder, &s, &i, temp_rev);
	temp_rev[i] = '\0';
	while (i--)
	{
		hexadecimal[l] = temp_rev[i];
		l++;
	}
	hexadecimal[l] = '\0';
	return (hexadecimal);
}
