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
"""

phase_schema = """
id
name
numSeeds
groupCount
"""

phase_group_schema = """
id
displayIdentifier
firstRoundTime
state
phaseId
waveId
tiebreakOrder
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
createdAt
claimed
verified
playerId
phoneNumber
connectedAccounts
contactInfo{{
    {0}
}}
events{{
    id
}}
""".format(attendee_contact_info_schema)

entrant_schema = """
id
name
eventId
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
eventId
phaseGroupId
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