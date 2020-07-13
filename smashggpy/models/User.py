
class User(object):

    def __init__(self, id, name, slug, gender_pronoun,
                 player, location, authorizations):
        self.id = id
        self.name = name
        self.slug = slug
        self.gender_pronoun = gender_pronoun
        self.player = player
        self.location = location
        self.authorizations = authorizations

    def __eq__(self, other):
        if other is None:
            return False
        if type(other) != type(self):
            return False
        return hash(other) == hash(self)

    def __hash__(self):
        return hash((self.id, self.name, self.slug, self.gender_pronoun,
                     self.player['id']))

    @staticmethod
    def parse(data):
        assert (data is not None), 'User.parse must not have a none data parameter'
        assert ('id' in data), 'User.parse must have an id property in data parameter'
        assert ('name' in data), 'User.parse must have a name property in data parameter'
        assert ('slug' in data), 'User.parse must have a slug property in data parameter'
        assert ('genderPronoun' in data), 'User.parse must have a genderPronoun property in data parameter'
        assert ('player' in data), 'User.parse must have a player dict in data parameter'
        assert ('location' in data), 'User.parse must have a location dict in data parameter'
        assert ('authorizations' in data), 'User.parse must have an authorizations dict in data parameter'

        return User(
            data['id'],
            data['name'],
            data['slug'],
            data['genderPronoun'],
            data['player'],
            data['location'],
            data['authorizations']
        )

    # GETTERS
    def get_id(self):
        return self.id

    def get_gamer_tag(self):
        return self.gamer_tag

    def get_prefix(self):
        return self.prefix

    def get_color(self):
        return self.color

    def get_twitch_stream(self):
        return self.twitch_stream

    def get_twitter_handle(self):
        return self.twitter_handle

    def get_youtube(self):
        return self.youtube

    def get_region(self):
        return self.region

    def get_state(self):
        return self.state

    def get_country(self):
        return self.country

    def get_gamer_tag_changed_at(self):
        return self.gamer_tag_changed_at
