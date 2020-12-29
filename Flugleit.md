# Flugleit

## The Get me home flight app

### Project overview:
The purpose of the application is to create an easy to use interface that allows someone to find all the flights within the next twelve to twenty-four hours from one airport to another. 

### User story:
As an airline pilot or other flight crew, you generally fly 'space available.' This is great in that it is generally free or heavily dicounted. It can be maddening though, because it means nothing is ever 'confirmed' or a 'sure thing.' You often find yourself in an airport far from home. Sometimes a trip that you are on cancels at an unscheduled outstation; or you and your family are non-revving on vacation and the flight you were planning to take is in an oversell situation; or which is very common for many flight crews, you live in another city from where you are based. Often times, you will find yourself getting off one airplane and you want to know when the next plane is leaving for your home city. Flugeliet ideally solves this. With a simple to use interface, you can quickly input your destination airport and it will return all of the flights from that airport in the next 12-24 hours.

### Basic Functionality Tasks: 
- The user should be able to input any departure and any arrival city
- The app will return a time table of flights
- If the fligth desired is in the next 12 hours, the app will give specific terminal and gate information
- The app will store a "home base" that is a default. It can be clicked with a simple check box
- The app will store user inputs and return recent flight searches

### Nice to have tasks (eventually to integrate):
- Real time flight alerts, that indicate whether a flight is delayed or cancelled
- Real time airport information that can alert user if there are weather or other delays to an airport
- Geo location integrated, so that departure airport populates with closest viable airport
- "Nearby" feature that returns flights from other airports that are in the geographic vicinity (ex: Orange county if at LAX)
- Multi-leg search, that recommends alternative routes to get home
- Flight probability indicator, that offers some indication on the number of relative seats availiable on a flight
- Airport information, that can populate with nearby restraunts, coffee, and other available facilities.
- Social aspect that allows a user to communicate with other users about possible disruptions or other unforeseen circumstances that might effect a given flight, "Hey, we are bringing this airplane in from Houston, the gate hasn't cancelled it yet, but the plane is hard broke and won't be doing the next flight."

### Models and databases
I plan on using the Django REST framework to integrate the front and back ends.
- In the Django app itself, the main model would be the user model, which would have the following:
    - user name
    - home airport
    - airline that they work for

The heavy lifting will come from mulitple API's and will be processed by Vue and REST
    - Cirium flight stats has a large api with timetables and other airport information. It has a limited amount functionality in it's 'evaluation' format, but for the scope of this project, with a limited number of actual users, it should work fine.
    - AeroDatabox is another API, that has some crossover information and other data that I might integrate as well. It has a limited amount of requests that can be made when using its "freemium" offering. Again though witht the scope of this project it should work. 

### Schedule

- January 6th: Have Django model complete with first basic iteration of flight look up function, along with user log on.  It willl be able to query the flight schedule API and return desired information, with a minimally styled interface, optimized for a phone-size interaction.

- January 8th: Intergrate "Home base" functionality along with displaying gate information

- January 12th: Have recent search capibility intergrated/ begin incorporating nice to have features

- January 14th: Integrate geo-location/delays functionality

- January 19th: Integrate "nearby" and "multi-leg function", airpory amenities if there is time

- January 20th and 21st: Error test and refine styling

- January 22nd: Present/Create timeline of future integrations/new ideas and possibilities.