# Structure : 

## Event
### Base Attributes : 
- ID 
- NameEvent 
- description
- DateStart
- isAllDay
- dateEnd
- ageRestriction
### FK to other tables : 
- IDCreator     FK => USER
- IDCategory    FK => EventCategory
- IDAgeCategory FK => AgeCategory
- IDLocation    FK => Location

## User
### Base Attributes : 
- ID
- username
- age
- passwordHash
- email

## Location
### Base Attributes : 
- ID
- StreetName
- StreetNumber
### FK to other tables : 
- IDCity    FK=> CITY

## City
### Base Attributes : 
- ID
- Name
- PostalCode
### FK to other tables : 
- IDCanton    FK=> Canton

## Canton
### Base Attributes : 
- ID
- Name
- shortName

## AgeCategory
### Base Attributes : 
- ID
- minAge

## EventCategory
### Base Attributes : 
- ID
- name
- description

## Participants
### FK to other tables : 
- IDEvent
- IDUser

## Commentary 
### Base Attributes : 
- ID
- texte
### FK to other tables : 
- IDEvent
- IDUser
- IDCommentAnswering

## Association class between event and user with the RATINGS :
### Base Attributes : 
- hasLiked
### FK to other tables : 
- IDEvent
- IDUser

# Example : 

## Event
### Base Attributes : 
- ID : 123
- NameEvent : "Music Festival"
- description : "The best music festival in the world"
- DateStart : "2023-07-21"
- isAllDay : false
- dateEnd : "2023-07-23"
- ageRestriction : 18
### FK to other tables : 
- IDCreator : 456       FK => USER
- IDCategory : 789      FK => EventCategory
- IDAgeCategory : 101   FK => AgeCategory
- IDLocation : 111      FK => Location

## User
### Base Attributes : 
- ID : 456
- username : "johndoe"
- age : 25
- passwordHash : "3a52c6f8b1..."
- email : "johndoe@example.com"

## Location
### Base Attributes : 
- ID : 111
- StreetName : "Rue de la gare"
- StreetNumber : 12
### FK to other tables : 
- IDCity : 222  FK=> CITY

## City
### Base Attributes : 
- ID : 222
- Name : "Lausanne"
- PostalCode : "10001"
### FK to other tables : 
- IDCanton : 333        FK=> Canton

## Canton
### Base Attributes : 
- ID : 333
- Name : "Vaud"
- shortName : "VD"

## AgeCategory
### Base Attributes : 
- ID : 101
- minAge : 18

## EventCategory
### Base Attributes : 
- ID : 789
- Name : "Music"
- description : "Events related to music"

## Participants
### FK to other tables : 
- IDEvent : 123
- IDUser : 456

## Commentary 
### Base Attributes : 
- ID : 1
- texte : "This event is awesome !"
### FK to other tables : 
- IDEvent : 123
- IDUser : 456
- IDCommentAnswering : 2

## Association class between event and user with the RATINGS :
### Base Attributes : 
- hasLiked : true
### FK to other tables : 
- IDEvent : 123
- IDUser : 456