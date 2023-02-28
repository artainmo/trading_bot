# trade_bot

The default algorithm is profitable in bull markets based on the simulator. Still the possibility exist to customize the algorithm.

## Use
In 'users_data/users.txt' set the proper coinbase API authentification keys.<br>
If coins_data.zip is already present, unzip it and put it in this directory. Else coins_data has to be generated with `./gen_data.sh`, which can take time.

To continue uploading the latest data `./gen_data.sh`. And finally launch the trading-bot `./start_user.sh cont`.<br>
By writing `./start_user.sh start` after deleting all the coins_data, the program will restart from the beginning regenerating all the data.
