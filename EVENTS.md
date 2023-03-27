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