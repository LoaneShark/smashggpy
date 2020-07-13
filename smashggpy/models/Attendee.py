from smashggpy.common.Exceptions import DataMalformedException, NoAttendeeDataException


class Attendee(object):

    def __init__(self, id, gamer_tag, prefix, 
                 verified, user, connected_accounts,
                 contact_info, event_ids):
        self.id = id
        self.gamer_tag = gamer_tag
        self.prefix = prefix
        self.verified = verified
        self.user = user
        self.connected_accounts = connected_accounts
        self.contact_info = contact_info
        self.event_ids = event_ids

    def __eq__(self, other):
        if other is None:
            return False
        if type(other) != type(self):
            return False
        return hash(other) == hash(self)

    def __hash__(self):
        return hash((self.id, self.gamer_tag, self.prefix, self.verified,
                     self.user, self.connected_accounts, self.contact_info, self.event_ids))

    @staticmethod
    def validate_data(input: dict, id: int=0) -> None:
        if 'data' in input:
            raise DataMalformedException(input)
        if 'phaseGroup' in input:
            input = input['phaseGroup']

        if 'participant' not in input and 'paginatedSeeds' not in input:
            raise NoAttendeeDataException(id)

        if 'participant' in input and input['participant'] is None:
            raise NoAttendeeDataException(id)
        elif 'paginatedSeeds' in input and input['paginatedSeeds']['nodes'] is None:
            raise NoAttendeeDataException(id)

    @staticmethod
    def parse(data):
        assert (data is not None), 'Attendee.parse must not have a none data parameter'
        assert ('id' in data), 'Attendee.parse must have a id property in data parameter'
        assert ('gamerTag' in data), 'Attendee.parse must have a gamerTag property in data parameter'
        assert ('prefix' in data), 'Attendee.parse must have a prefix property in data parameter'
        assert ('verified' in data), 'Attendee.parse must have a verified property in data parameter'
        assert ('user' in data), 'Attendee.parse must have a user property in data parameter'
        assert ('connectedAccounts' in data), 'Attendee.parse must have a connectedAccounts property in data parameter'
        assert ('contactInfo' in data), 'Attendee.parse must have a contactInfo property in data parameter'
        assert ('events' in data), 'Attendee.parse must have a events property in data parameter'

        return Attendee(
            data['id'],
            data['gamerTag'],
            data['prefix'],
            data['verified'],
            data['user'],
            data['connectedAccounts'],
            data['contactInfo'],
            [ids for ids in data['events']]
        )

    # GETTERS
    def get_id(self):
        return self.id
    
    def get_gamer_tag(self):
        return self.gamer_tag
    
    def get_prefix(self):
        return self.prefix
    
    def get_created_at(self):
        return self.created_at
    
    def get_claimed(self):
        return self.claimed
    
    def get_verified(self):
        return self.verified
    
    def get_player_id(self):
        return self.player_id
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_connected_accounts(self):
        return self.connected_accounts
    
    def get_contact_info(self):
        return self.contact_info
    
    def get_event_ids(self):
        return self.event_ids
    