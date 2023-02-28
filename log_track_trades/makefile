NAME = trade_log

NAME2 = portfolio

SRC = trade_history.c

SRC2 = portfolio_history.c

OBJ = $(SRC:.c=.o)

OBJ2 = $(SRC2:.c=.o)

LIBFLAGS = -I . -L . -I ./utils/libft -L ./utils/libft -I ./utils/get_next_line -L ./utils/get_next_line ./utils/get_next_line/*.c


GCC = gcc -Wall -Wextra -Werror -fsanitize=address
RM = rm -rf

all: libft_all $(NAME)
portfolio: libft_all $(NAME2)


$(NAME): $(OBJ)
	$(GCC) $(LIBFLAGS) libft.a $(OBJ) -o $(NAME)

$(NAME2): $(OBJ2)
	$(GCC) $(LIBFLAGS) libft.a $(OBJ2) -o $(NAME2)

# WALL WEXTRA WERROR ARE CURRENTLY NOT APPLIED UNCOMMENT THOSE 2 LINES TO APPLY FLAGSS
%.o: %.c
	$(GCC) -c -o $@ $?

bonus: all

clean: libft_fclean
	$(RM) $(OBJ)
	$(RM) $(OBJ2)

fclean: clean
	$(RM) $(NAME)
	$(RM) $(NAME2)

re: fclean all
re2: fclean portfolio

# In this last section we make other makefiles compile with the -C flag
# The -C flag makes you go to the appropriate path and do the asked command
libft_all:
	make -C ./utils/libft all
	cp ./utils/libft/libft.a libft.a
libft_clean:
	make -C ./utils/libft clean
libft_fclean:
	make -C ./utils/libft fclean
	$(RM) libft.a

.PHONY: all test clean fclean re bonus
# Phony targets can exs->plicitly tell Make they're not associated with files but with make commands
