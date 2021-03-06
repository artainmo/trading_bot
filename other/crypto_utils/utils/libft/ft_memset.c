/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   memset.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: artainmo <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/10/07 11:14:08 by artainmo          #+#    #+#             */
/*   Updated: 2019/10/10 19:40:10 by artainmo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memset(void *b, int c, unsigned int len)
{
	char *ptr;

	ptr = b;
	while (len)
	{
		*ptr = c;
		ptr++;
		len--;
	}
	return (b);
}
