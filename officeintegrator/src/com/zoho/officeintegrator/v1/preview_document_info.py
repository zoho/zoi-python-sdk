try:
	from officeintegrator.src.com.zoho.officeintegrator.exception.sdk_exception import SDKException
	from officeintegrator.src.com.zoho.officeintegrator.util.constants import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class PreviewDocumentInfo(object):
	def __init__(self):
		"""Creates an instance of PreviewDocumentInfo"""

		self.__document_name = None
		self.__key_modified = dict()

	def get_document_name(self):
		"""
		The method to get the document_name

		Returns:
			string: A string representing the document_name
		"""

		return self.__document_name

	def set_document_name(self, document_name):
		"""
		The method to set the value to document_name

		Parameters:
			document_name (string) : A string representing the document_name
		"""

		if document_name is not None and not isinstance(document_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: document_name EXPECTED TYPE: str', None, None)
		
		self.__document_name = document_name
		self.__key_modified['document_name'] = 1

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
