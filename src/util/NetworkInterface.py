import json
import requests

class NetworkInterface(object):

	API_URL='https://api.smash.gg/gql/alpha'

	@staticmethod
	def get_headers():
		return {
			'X-Source': 'smashgg.py',
			'Content-Type': 'application/json',
			'Authorization': 'Bearer {}'.format(TokenHandler.get_token())
		}

	@staticmethod
	def query(query_string: str, variables: dict):
		Logger.debug('NetworkInterface.query: creating query object')
		query = QueryFactory.create(query_string, variables)
		Logger.debug('NetworkInterface.query: created query {}'.format(query))

		Logger.debug('NetworkInterface.query: sending query to queue')
		QueryQueue.get_instance().add(query)
		return NetworkInterface.execute_query(query)

	@staticmethod
	def paginated_query(query_string: str, variables: dict):
		Logger.debug('NetworkInterface.paginated_query: creating query object')
		query = QueryFactory.create(query_string, variables)
		Logger.debug('NetworkInterface.paginated_query: created query {}'.format(query))

		Logger.debug('NetworkInterface.paginated_query: sending query to queue')
		QueryQueue.get_instance().add(query)

		results = []
		initial_result = NetworkInterface.execute_query(query)
		main_key = list(initial_result['data'].keys())[0]
		secondary_key = list(initial_result['data'][main_key].keys())[0]
		base_data = initial_result['data'][main_key][secondary_key]
		results.append(base_data['nodes'])

		total_pages = base_data['pageInfo']['totalPages']
		for i in range(1, total_pages, 1):
			variables['page'] = i
			current_result = query(query_string, variables)
			results.append(current_result)

		return results

	@staticmethod
	def execute_query(query):
		log = Logger.get_instance()
		url = NetworkInterface.API_URL
		headers = NetworkInterface.get_headers()
		payload = query.get_query_dict()

		log.debug('NetworkInterface.query: Payload: {}'.format(payload))
		log.debug('NetworkInterface.query: Headers: {}'.format(headers))

		response = requests.post(url=url, headers=headers, json=payload)

		log.debug('NetworkInterface.query: {}'.format(response))
		log.debug('NetworkInterface.query: JSON Response: {}'.format(response.json()))
		return response.json()

# Path imports
from src.util.Logger import Logger
from src.util.TokenHandler import TokenHandler
from src.util.QueryFactory import QueryFactory
from src.util.QueryQueue import QueryQueue