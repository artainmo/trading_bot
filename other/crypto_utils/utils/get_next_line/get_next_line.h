/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cacharle <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/10/09 13:52:59 by cacharle          #+#    #+#             */
/*   Updated: 2019/11/03 22:43:18 by cacharle         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_H
# define GET_NEXT_LINE_H

# include <limits.h>

# ifndef BUFFER_SIZE
#  define BUFFER_SIZE 32
# endif

# define STATUS_LINE 1
# define STATUS_EOF 0
# define STATUS_ERROR -1

# define TRUE 1
# define FALSE 0

# define FT_STRNCPY_BUF(dest, src) (ft_strncpy(dest, src, BUFFER_SIZE + 1))

typedef int	t_bool;

/*
** get_next_line.c
*/

int		get_next_line(int fd, char **line);
int		read_line(int fd, char **line, char *rest);
int		find_newline(char *str);
int		free_return(char **ptr, char **rest, int ret);

/*
** get_next_line_utils.c - helper functions
*/

char	*ft_strappend(char *dest, char *src);
char	*ft_strncpy(char *dest, const char *src, int n);
int		ft_strlen(const char *str);
char	*ft_strcpy(char *dest, const char *src);
char	*ft_strdup(const char *s);

#endif
