# trading_bot

Different projects around cryptocurrency trading. From a trade tracking system, to a customizable trading-bot and simulator.<br>

Look inside the appropriate folder to learn more about a specific project.

## Documentation
### Vocabulary
#### API
Application programmable interfaces, allow connexion between two applications.<br>
The application where the API is from, allows the application using the API access to some of its data.<br>
Plus it potentially allows to take actions on that application through the other application.

#### REST API
Representational state transfer is a software architectural style that defines a set of constraints to be used for creating Web services. Web services that conform to the REST architectural style, called RESTful Web services, provide interoperability between computer systems on the Internet.<br>
Contains HTTP verbs or commands, that we call CRUD (Create, Read, Update, Delete).<br>
Tons of APIs already exist, that have their own commands based on the CRUD commands.<br>
To connect with rest APIs through the web you need to use HTTP. As you make an HTTP request to the server, the server will return you a BODY containing data in JSON and a HEADER, that contains additional information like an error code.<br>
Each API has own specific rules that should be explained in its API documentation.<br>
An API endpoint URL is the place that APIs send requests and where the resource lives, you need to use the CRUD commands to this URL to interact with API.

#### Web
A computer contains an internet browser. The web browser is a client that is used to connect to a server. You can connect to the server by using an universal resource locator (URL).<br>
An URL starts with http (hypertext transfer protocol), http is like a language that servers can read, here the http makes a request and the server will return a response. The most important part of the response is the body or html, that allows for page rendering.<br>
Each time you click on an url you make a http or GET or read request of a specific page to the web server.<br>
Often times the server returns his answer or data in JSON (Javascript object notation), this allows to structure the data and is also called the resource.<br>
Here is a list of all HTTP verbs: GET, PUT, PATCH, POST, DELETE.

#### Call API
To call your API you should always use HTTP. You can use it in different ways, one way is through `curl`.<br>
If you `curl` an URL, you will get as output all the frontend code of that page.<br>
`curl -o filename` allowa you to put the output inside a file.<br>
To do an HTTP command: `curl -X httpcommand`.<br>
To use authentication: `curl -u authentifications`. Or if you need to authentificate via a header: `curl -H authentifications`.

#### SDK
A software development kit is a collection of software development tools in one installable package.<br>
They ease creation of applications by having compiler, debugger and perhaps a software framework.

### Cryptocurrency trading
#### Do own research
Look at the reviews on coinmarketcap, if positive its value will probably increase in the long term.<br>
You can also look at the idea behind the coin and judge if it will have a bright future or not.<br>
You can also look at all of the coins historical values on coinmarketcap, on coinbase too.

#### Crytpo market explained
The market price of a coin is driven by supply and demand.<br>
Driven by availability, the scarcer a cryptocurrency, the higher its price levels.<br>
You can look at a particular coin's maximum supply.<br>
Best is to buy when marketprice is low.

#### Trends
Long-term trends that contain highs and lows where you can buy and sell, make small trades while the trend continues:
* upward trends (increasing average)
* downward trends (decreasing average)
* consolidation trends (same average)
-> 200day ema can be useful for long-term investments

#### Order book
In order book you can see total amounts of buying orders and selling orders, if more buying than selling orders, upward trend. This can change every second and give the most false signals.<br>
In order book you can see all prices and next to it total amount of coins to be sold or bought at that price.<br>
Order book should not really be taken into account for trading bot.

#### Profitable trading strategies
Always have an exit strategy in mind.

##### 100$ RISK
High risk - high reward<br>
Invest in new coins, that thus have a very low market price, during ICO (initial coin offering, similar to IPO in stocks).<br>
This coin could explode or fall, in worst case scenario you could lose 100$ and in best case scenario you could make an infinite gain.

##### Own multiple standard coins
You can use them to buy altcoins, if the standard coins are going low, you can use them to buy upgoing altcoins before they actually are low.

##### Allocate wisely
Use 50% funds into standard coins and 50% funds into altcoins for example.<br>
Always keep some standard coins (tether, btc, eth) so you can use them to buy altcoins when they go low.<br>
Use 10% funds for high-risk/high-reward investments.

#### Support and resistance
Or floors and ceilings, they are price areas that tend to act like barriers.<br>
Here we rely on what happened in the past with technical analysis.<br>
Support or floors, is where buying was interesting previously and resistance is where selling was interesting previously.<br>
You can look at weekly or even all graphs to find floor and ceilings, to look at potentially interesting long-term or short-term investments.

##### Levels
Different levels exist that all have their own floor and ceilings.<br>
They can be seen as consolidation trends that all have a floor and ceiling.<br>
First see in what level you are, then look if you are at floor or ceiling of this level.<br>
--> level size in % based on highest value: example min-floor:115 max-ceiling:140 -> 25/140 * 100  * 2(becuase 50% is considered 100% or 25%)| 0 - 25%<br>
--> position inside level | max-ceiling - mim-floor | 0 - 25%

Find levels<br>
--> Use the 26day ema, As long as 0,0012745% or less change/hour, you are inside the level where you can search for floor and ceiling, look only at last time you were in this level, the level should have a 24h range.

#### Continuous and reversal patterns
Are patterns that you can recognize from the beginning, knowing that the chance is high
of them continuing a certain way. If you know how they will evolve you can invest accordingly.

With image recognition, patterns could be found. Learn more about patterns in udemy course.

##### Dead cat bounce
Once a price strongly decreases in a short amount of time, you know it will bounce back up right after.<br>
If you recognize that you can quickly buy at the bottom and sell high at the bounce.<br>
--> descends more than 3% in 15min or 5% in 1h --> if technical analysis calls for a raise that will start buy<br>
--> skip levels if activated --> Do not buy as long as 1min ema crossover is not activated and to sell profit is not equal to al least 1%<br>
--> Once dead cat bounce found, use the 1min crossover strategy to buy and to sell

##### Head & shoulders
3 peaks, with the middle one being the highest, the last peak will be followed
by a strong descend.<br>
Inverse head & shoulders, 3 falls, with the middle one the lowest, the last descend
will be followed by a strong raise.<br>
The difference between between the highest and lowest point in the head (pipe), is often equal
to how much the price will descend or raise afterwards.

Once you recognize the third shoulder being as high as the first shoulder and starting to descend,
you should sell.<br>
If price has descended as much or lower than pipe and is raising again you should buy.<br>
Once you recognize the third shoulder being as low as the first shoulder and starting to raise,
you should buy.<br>
If price has raised as much or more than pipe and is lowering again you should buy.<br>
--> If EMA is correct, you can avoid small bumps, and buy/sell correctly in combination with the dead cat bounce.

##### Double tops & bottoms
Double tops:<br>
If price raises one time to a ceiling, goes back down at least more than half of how much it raised initially, and goes back up to that same ceiling before going back down, to right under the floor it started out with. Now you know that the price will continue to go down until it hits a low, all of this in a relatively low timeframe.

Double lows:<br>
If price lowers one time to a floor, goes back up at least more than half of how much it lowerd initially, and goes back down to that same floor before going back up, to right above the ceiling it started out with. Now you know that the price will continue to go up until it hits a high, all of this in a relatively low timeframe.

##### Rounding bottoms & tops
Not one peak but one half circle, thus meaning slow activity.<br>
The half circle should start and finish at same price.

If rounding top, the half circle will be followed by a price descend that should be as long as the round pipe (difference between lowest and highest point in the half circle).<br>
--> Sell at rounding top.<br>
--> Buy after steep price decrease.

If rounding bottom, the half circle will be followed by a price increase that should be as long as the round pipe.<br>
--> Buy at rounding bottom.<br>
--> Sell at following price increase.

##### Cup & handle
Here we do not talk about a half circle or peaks, but something in between those, followed by a small cup, that will be followed by a steep increase in price for cup.<br>
--> Thus you should buy in lowest point of second cup.

##### Wedges & triangles
Price compressing triangle:<br>
Peaks that start to have lower and lower ceilings and floors, once you hit 80% of the triangle it should break, it will break by descending as much as the height of the first peak.

Descending triangle:<br>
Peaks that start to have higher and higher floors, while the ceiling stays the same, once you hit 80% of the triangle it should break, it will break by raising as much as the height of the first peak.

Rising wedges:<br>
Ceiling price increasing more and more while floor price increasing more and more, once you hit 80% of the triangle it should break, it will break by descending until the initial starting point of the first peak.

Descending wedge:<br>
Ceiling price descending more and more while floor price descending more and more, once you hit 80% of the triangle it should break, it will break by raising until the initial peak.

##### Flags & pennants
Steep increase followed by consolidation trend (up & down peaks, staying the same) will be followed by the same steep increase again once consolidation stops.<br>
Steep decrease followed by consolidation trend (up & down peaks, staying the same) will be followed by the same steep decrease again once consolidation stops.

#### Candle sticks
A candlestick can be green (market increase) or red (market falling) plus it contains a body and a wick or even two wicks (one above and under body).<br>
Candlesticks are useful when trading as they show four price points (open, close, high, and low) throughout the period of time the trader specifies.<br>
Top body is opening/starting price, lowest body is closing/final price.<br>
Top wick is highest price and lowest wick is lowest price.

#### Risk management
Always put sell order at price 5-10% below long term floor level to avoid losing too much if market cap keeps descending under the floor level.<br>
If price 3% under the resistance level activate warning, sell once price descends 1% and warning is active. This will allow to maybe profit from a price that keeps raising above the resistance price.

#### exponential moving averages(EMA) - technical analysis
Gives coin market price overtime upwards or downwards trends.<br>
Simple moving average is similar, only difference is that SMA looks more at long term.<br>
The EMA puts more weight on the recent data.<br>
Calculate sma: the sum of the stock's closing prices for the number of time periods in question, divided by that same number of periods.<br>
To calculate ema, recent days have more weight.<br>
--> Very useful when in a down or upward market.<br>
EMAs with more days tend to look at long-term and won't signal for smaller bumps.<br>
50 day ema is a good long-term indicator for example.<br>
-> If ema is above actual curve, sign market will lower.<br>
-> If ema is lower than actual curve, sign market will increase.

##### EMA crossover strategy
Take 20day and 9day EMA or period not day, which means a certain period devided by 9 or 20.<br>
If 9day ema crosses over 20day ema + both emas have upward trend -> Time to buy<br>
If 9day ema crosses under 20day ema + both emas have downward trend -> Time to sell<br>
For daytrading you can even use 1h and 15min emas<br>
Most accurate for creating buying/selling signals<br>
-> moving upward 12ema(5%) + 26ema(5%)<br>
-> 12day ema over 26day ema (15%)<br>
--> the number 12 or 26 indicate the number of ema periods, one ema period can be a minute, hour, day, ....

#### Parabolic SAR
Able to find sudden changes in market price directions, good for daytrading.<br>
In graphs, comes as series of dots either above or under current price.<br>
If under price -> Uptrend -> buy<br>
If above price -> Downtrend -> sell<br>
Use it for daytrading or in combination with other techniques signals, because it can trigger alot of signals even when not necessary.<br>
--> Understand this better to combine it with emas as strategy.

#### MACD indicator
Moving average convergence divergence, is a trend-following indicator that shows the relationship between two exponential moving averages.<br>
The MACD line is calculated through substracting the ema26 from the ema12.<br>
The signal line is equal to a 9ema of the macd line.

Uptrend signal: MACD line crosses above signal line | Both lines slope upwards<br>
-> extra indicator strong upward MACD is above the zero line or simply a positive number

Downtrend signal: MACD line crosses below signal line | Both lines slope downwards<br>
If downtrend you need to sell, it means price will soon come down.

MACD can show a lot of false buy and sell signals, it should only be used to warn you about a potential market direction change, EMA crossover should be used to confirm the next market direction.<br>
If you want to create a maker and not taker trade (for lower fees), you need to predict if the price is going to increase, you can use the MACD as a second confirmation next to EMA for the price that will keep raising.<br>
--> MACD is not the best signal indicator. You can ignore it completely and focus instead on 20 - 9cross emas

#### Relative strenght index
RSI = 100 - 100/(1-RSI)<br>
RSI is the average gain of n periods minus the average loss of n periods.<br>
RSI provides, sell(>80%) or buy(<20%), signals when stock is oversold or overbought.<br>
--> Can give false signals, should be used with caution or maybe in combination with ema crossovers<br>
--> Can be used as extra confirmation of buying/selling if playing with probabilities.

#### Buy or sell conclusion
Make orders instead of take orders can be used to save on fees once you make 50k+ investments.<br>
FOR EACH COIN FIND IF A DEAL (90% - 125%)<br>
compare current price with max price last year of coin with high - low | 0 - 25%<br>
Check for any patterns | for buy pattern 0 - 25%:<br>
*Cat bounce --> 1min ema crossover (45%)<br>
*check where inside the level, floor - ceiling | -> 1h ema crossover(25%), 15min ema crossover(20%)<br>
*free / no pattern found = 12.5% -> 1h ema crossover(25%), 15min ema crossover(20%)<br>
--> Buy pattern is equal to resulting % and sell pattern is equal to 50 - resulting %<br>
After always check if technical analysis gives a flag -> parabolic SAR(15%) + emas crossover(45%) + RSI(15%)<br>
--> Check technical analysis separately for buy or sell<br>
AFTER COMPARE WHAT COIN HAS BEST DEAL BY CREATING A POINT SYSTEM IN %<br>
try also to diversify, thus do not invest everything in one deal<br>
If multiple above 90% take highest and divide to-buy-price between highest and those that are in 10% under range of highest.<br>

Sell protection rule, sell if 1% under bought price.<br>
Each time a deal is bought print sreen in, coins class have a dictionary that contains reason of buy or sell.

##### algorithm
Take crypto history of all cryptos wanting to be traded -> BTC, ETH, EOS, XRP, LTC<br>
Enter loop with 5s delays<br>
Capture all cryptos prices and add those to price history with specific trading time<br>
Check if any good deal for Selling<br>
Check if any good deal for Buying<br>
Loop again<br>

Latest algo:<br>
Complicated algorithm isn't necessarily better and increases chances of mistakes, for now this simpler algorithm will be used.<br>
- RSI is a buy and sell signal.<br>
- 1h + 15min ema12-26 crossover is buy and sell signal.<br>
- cat_bounce  + 1min 12-26ema crossover is signal to buy and has specific sell signal, 1min ema12-26 crossover.<br>

Latest algo:<br>
Complicated algorithm isn't necessarily better and increases chances of mistakes, for now this simpler algorithm will be used.<br>
- 1h + 15min ema12-26 crossover is buy and sell signal.<br>
- For even more security but potential opportunity losses, you could add a second condition looking at the 1day emas, to see if you are in an up or down trend market more in longer term.

#### FINAL GOAL
When investing more than 50k, maker fees become interesting and you can set limit orders in place, small time after signal has been set to continuum price.<br>
IMPLEMENT AI<br>
--> give AI ema-crossovers (day, 15min, 1h, 1min), sar and sri data too next to the general data, try to maximize the data you get.<br>
--> Use image recognition on the market graphs so that the AI can recognize trends.<br>

However, more and more trading bots are coming to the market. If they all follow the same algorithm, no one will win. Only the best will win who can adapt to the behavior of other trading bots. This may be an impossible race to win without more investment.

#### Other
Coinbase is used to look at the different cryptocurrencies with clear graphs.<br>
Coinbase pro is used to do the actual trading.<br>
Delta is used to get custom notifications for all cryptocurrencies when they reach a certain price.

##### Two techniques are used
Those two techniques can be used together, initial buy with long term intent and in the meanwhile do medium-term trading.

LONGTERM<br>
Buy when in bear market, very low and sell when in bull market.

MEDIUMTERM<br>
Look at common ups and down of the moment, sell when high and you know it will lower afterward. If it lowers until a certain amount buy back at that lower amount, otherwise buy back at same price.<br>
Use limit orders to do things in advance. Each night put buying limit as the lowest of prior 24h and selling limit as highest of prior 24hours.

##### General Advice
Never be emotional about trading.<br>
Don’t follow others' advice look at facts yourself.

##### Coinbase Pro trading
Lower fees than with coinbase.

You can invest in two different ways, either as a taker or as a maker.<br>
Makers pay between 0.04-0.5%fees.<br>
Takers pay between 0-0.5%fees.<br>
To pay less in fees with taker invest you should invest at least 50k.

You are a taker when your order gets filled immediately.

You are a maker when your order is not immediately matched but put into an order book, waiting for another customer to match your order. You can use this method, which is favorable due to less fees, when you are waiting in advance for a certain price point and know for sure you want to buy at that price point.

Three types of orders:<br>
Market order - general order that gets filled immediately<br>
Stop order - Choose price (stop price) at which order (limit price) should be executed<br>
Limit order - Choose price at which order should be executed with additional settings<br>

Limit order settings<br>
Post only - allow taker<br>
If to-be-filled order already exists, and your order will be filled immediately, thus you will pay taker fees. Post only protects against that while allow taker not.<br>

When selecting a limit order, expand the Advanced section to reveal the following Time in Force policies:<br>
Good 'Til Canceled (GTC) - This order will be placed on the order book and remain valid until you cancel it.<br>
Good Til Tine (GTT) - This order will be placed on the order book and remain valid until you cancel it or the timing you indicated ended.<br>
Immediate or Cancel (IOC) - This order will be placed and if it is not immediately filled, it will automatically be cancelled and removed from the order book.<br>
Fill or Kill (FOC) - This order will only complete if the entire amount can be matched. Partial matches are not filled with this order type and will not execute
