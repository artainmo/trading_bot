# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: artainmo <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/09 21:50:42 by artainmo          #+#    #+#              #
#    Updated: 2019/10/22 16:57:48 by artainmo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

SRC1 = ft_memset.c \
        ft_bzero.c \
        ft_memcpy.c \
        ft_memccpy.c \
        ft_memmove.c \
        ft_memchr.c \
        ft_memcmp.c \
        ft_strlen.c \
        ft_isalpha.c \
        ft_isdigit.c \
        ft_isalnum.c \
        ft_isascii.c \
        ft_isprint.c \
        ft_toupper.c \
        ft_tolower.c \
        ft_strchr.c \
        ft_strrchr.c \
        ft_strncmp.c \
        ft_strlcpy.c \
        ft_strlcat.c \
        ft_strnstr.c \
        ft_atoi.c \
        ft_calloc.c \
        ft_strdup.c \
        ft_substr.c \
        ft_strjoin.c \
        ft_strtrim.c \
        ft_itoa.c \
        ft_strmapi.c \
        ft_putchar_fd.c \
        ft_putstr_fd.c \
        ft_putendl_fd.c \
        ft_putnbr_fd.c \
        ft_split.c
SRC2 = ft_lstnew_bonus.c \
        ft_lstadd_front_bonus.c \
        ft_lstsize_bonus.c \
        ft_lstlast_bonus.c \
				ft_lstadd_back_bonus.c \
        ft_lstdelone_bonus.c \
        ft_lstclear_bonus.c \
        ft_lstiter_bonus.c \
        ft_lstmap_bonus.c
NAME = libft.a
OBJS = *.o
CFLAGS = -Wall -Wextra -Werror -I$(HEADER)
GCC = gcc
RM = rm -rf
HEADER = ./

all: $(NAME)

$(OBJS): $(SRC1)
	  		$(GCC) $(CFLAGS) -c $(SRC1)

$(NAME): $(OBJS)
	      ar rc $(NAME) $(OBJS)
	      ranlib $(NAME)

bonus:
	$(GCC) $(CFLAGS) -c $(SRC2)
	ar rc $(NAME) $(OBJS)
	ranlib $(NAME)

clean:
	    $(RM) $(OBJS)

fclean: clean
	    $(RM) $(NAME)

re: fclean all

.PHONY: all test clean fclean re bonus
