authorization_types = """
[TWITTER, TWITCH, DISCORD, MIXER]
"""

auth_stream_schema = """
id
isOnline
name
type
"""

authorization_schema = """
id
externalUsername
stream {{
	{0}
}}
type
url
""".format(auth_stream_schema)

location_schema = """
id
city
country
countryId
state
stateId
"""

player_schema = """
id
gamerTag
prefix
"""

user_schema = """
id
name
slug
birthday
genderPronoun
player {{
	{0}
}}
location {{
	{1}
}}
authorizations(types: {2}){{
	{3}
}}
""".format(player_schema, location_schema, authorization_types, authorization_schema)
# gamerTag
# gamerTagChangedAt
# region
# state
# country
# twitchStream
# twitterHandle
# youtube
# prefix
# color

tournament_schema = """
id
name
slug
city
postalCode
addrState
countryCode
venueAddress
venueName
lat
lng
timezone
startAt
endAt
owner{{
	{0}
}}
""".format(user_schema)
# gettingThere
# region
# contactEmail
# contactTwitter
# contactPhone
# ownerId -> owner

event_schema = """
id
name
slug
state
startAt
numEntrants
checkInBuffer
checkInDuration
checkInEnabled
isOnline
teamNameAllowed
teamManagementDeadline
videogame {
	id
	slug
	name
	displayName
}
"""

phase_schema = """
id
name
numSeeds
groupCount
bracketType
"""

phase_group_schema = """
id
displayIdentifier
firstRoundTime
state
phase {
	id
	name
}
wave {
	id
	identifier
}
tiebreakOrder
bracketType
"""

attendee_contact_info_schema = """
id
city
state
stateId
country
countryId
name
nameFirst
nameLast
zipcode
"""

attendee_schema = """
id
gamerTag
prefix
checkedInAt
verified
connectedAccounts
contactInfo{{
    {0}
}}
user {{
	{1}
}}
events{{
    id
}}
""".format(attendee_contact_info_schema, user_schema)

entrant_schema = """
id
name
event {{
	id
	name
	}}
skill
participants{{
    {0}
}}
""".format(attendee_schema)

gg_set_slot_schema = """
id
entrant {
    id
    name
    participants {
        id
    }
}
"""

gg_set_schema = """
id
event {{
	id
	name
}}
phaseGroup {{
	id
	displayIdentifier
}}
displayScore
fullRoundText
round
startedAt
completedAt
winnerId
totalGames
state
slots(includeByes: false){{
    {0}
}}
""".format(gg_set_slot_schema)

stream = """
id
eventId
tournamentId
streamName
numSetups
streamSource
streamType
streamTypeId
isOnline
enabled
followerCount
removesTasks
streamStatus
streamGame
streamLogo
"""