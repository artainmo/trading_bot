/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cacharle <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/10/08 08:52:59 by cacharle          #+#    #+#             */
/*   Updated: 2019/11/03 22:57:39 by cacharle         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "get_next_line.h"

char	*ft_strappend(char *dest, char *src)
{
	void	*copy;
	int		dest_len;

	dest_len = ft_strlen(dest);
	if ((copy = (char*)malloc(sizeof(char) * (dest_len + 1))) == NULL)
		return (NULL);
	ft_strcpy(copy, dest);
	free(dest);
	dest = (char*)malloc(sizeof(char) * (dest_len + ft_strlen(src) + 1));
	if (dest == NULL)
		return (NULL);
	ft_strcpy(dest, copy);
	free(copy);
	ft_strcpy(dest + dest_len, src);
	return (dest);
}

char	*ft_strncpy(char *dest, const char *src, int n)
{
	int	i;

	i = 0;
	while (src[i] && i < n)
	{
		dest[i] = src[i];
		i++;
	}
	while (i < n)
		dest[i++] = '\0';
	return (dest);
}

int		ft_strlen(const char *str)
{
	int counter;

	counter = 0;
	while (str[counter])
		counter++;
	return (counter);
}

char	*ft_strcpy(char *dest, const char *src)
{
	int i;

	i = 0;
	while (src[i])
	{
		dest[i] = src[i];
		i++;
	}
	dest[i] = '\0';
	return (dest);
}

char	*ft_strdup(const char *s)
{
	char	*clone;
	size_t	i;
	size_t	len;

	len = ft_strlen((char*)s);
	if ((clone = (char*)malloc(sizeof(char) * (len + 1))) == NULL)
		return (NULL);
	i = 0;
	while (i < len)
	{
		clone[i] = s[i];
		i++;
	}
	clone[i] = '\0';
	return (clone);
}
