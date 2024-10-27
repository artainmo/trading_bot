# trading_bot

Different projects around cryptocurrency trading. From a trade tracking system, to a customizable trading-bot and simulator.<br>

Look inside the appropriate folder to learn more about a specific project.

To learn more about and understand the proposed trading algorithm elements, see 'documentation/crypto_trading.txt'.

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
