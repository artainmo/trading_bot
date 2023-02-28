Different projects around cryptocurrency trading


SET
Set proper api authentification keys
Unzip coins_data in other/rem or elsewhere(too large dataset for git) and place it in trade_bot or simulation directory

TRADE_BOT ALGO:
Use python2.7 data_generator.py for constant uploading of coin data.
To restart the program from begin, meaning reuploading all the coins data use the start argument, make sure to delete all the actual coins data files first.
Use the cont argument to let the program continue with actual data.

Use python2.7 start_users.py to launch the client process that manages the crypto account given in the user.txt file.

SIMULATION ALGO:
Write down in user.txt your algo specifications, let it run with python2.7 user.py and see the result in the feedback directory.
