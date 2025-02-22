try:
	from officeintegrator.src.com.zoho.officeintegrator.exception.sdk_exception import SDKException
	from officeintegrator.src.com.zoho.officeintegrator.util.constants import Constants
	from officeintegrator.src.com.zoho.officeintegrator.v1.writer_response_handler import WriterResponseHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .writer_response_handler import WriterResponseHandler


class FillableLinkResponse(WriterResponseHandler):
	def __init__(self):
		"""Creates an instance of FillableLinkResponse"""
		super().__init__()

		self.__fillable_form_url = None
		self.__key_modified = dict()

	def get_fillable_form_url(self):
		"""
		The method to get the fillable_form_url

		Returns:
			string: A string representing the fillable_form_url
		"""

		return self.__fillable_form_url

	def set_fillable_form_url(self, fillable_form_url):
		"""
		The method to set the value to fillable_form_url

		Parameters:
			fillable_form_url (string) : A string representing the fillable_form_url
		"""

		if fillable_form_url is not None and not isinstance(fillable_form_url, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: fillable_form_url EXPECTED TYPE: str', None, None)
		
		self.__fillable_form_url = fillable_form_url
		self.__key_modified['fillable_form_url'] = 1

	def is_key_modified(self, key):
		"""
		The method to check if the user has modified the given key

		Parameters:
			key (string) : A string representing the key

		Returns:
			int: An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if key in self.__key_modified:
			return self.__key_modified.get(key)
		
		return None

	def set_key_modified(self, key, modification):
		"""
		The method to mark the given key as modified

		Parameters:
			key (string) : A string representing the key
			modification (int) : An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if modification is not None and not isinstance(modification, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modification EXPECTED TYPE: int', None, None)
		
		self.__key_modified[key] = modification
