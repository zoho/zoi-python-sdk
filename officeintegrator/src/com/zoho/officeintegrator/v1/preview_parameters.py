try:
	from officeintegrator.src.com.zoho.officeintegrator.exception.sdk_exception import SDKException
	from officeintegrator.src.com.zoho.officeintegrator.util import StreamWrapper, Constants
except Exception:
	from ..exception import SDKException
	from ..util import StreamWrapper, Constants


class PreviewParameters(object):
	def __init__(self):
		"""Creates an instance of PreviewParameters"""

		self.__url = None
		self.__document = None
		self.__document_info = None
		self.__permissions = None
		self.__key_modified = dict()

	def get_url(self):
		"""
		The method to get the url

		Returns:
			string: A string representing the url
		"""

		return self.__url

	def set_url(self, url):
		"""
		The method to set the value to url

		Parameters:
			url (string) : A string representing the url
		"""

		if url is not None and not isinstance(url, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: url EXPECTED TYPE: str', None, None)
		
		self.__url = url
		self.__key_modified['url'] = 1

	def get_document(self):
		"""
		The method to get the document

		Returns:
			StreamWrapper: An instance of StreamWrapper
		"""

		return self.__document

	def set_document(self, document):
		"""
		The method to set the value to document

		Parameters:
			document (StreamWrapper) : An instance of StreamWrapper
		"""

		if document is not None and not isinstance(document, StreamWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: document EXPECTED TYPE: StreamWrapper', None, None)
		
		self.__document = document
		self.__key_modified['document'] = 1

	def get_document_info(self):
		"""
		The method to get the document_info

		Returns:
			PreviewDocumentInfo: An instance of PreviewDocumentInfo
		"""

		return self.__document_info

	def set_document_info(self, document_info):
		"""
		The method to set the value to document_info

		Parameters:
			document_info (PreviewDocumentInfo) : An instance of PreviewDocumentInfo
		"""

		try:
			from officeintegrator.src.com.zoho.officeintegrator.v1.preview_document_info import PreviewDocumentInfo
		except Exception:
			from .preview_document_info import PreviewDocumentInfo

		if document_info is not None and not isinstance(document_info, PreviewDocumentInfo):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: document_info EXPECTED TYPE: PreviewDocumentInfo', None, None)
		
		self.__document_info = document_info
		self.__key_modified['document_info'] = 1

	def get_permissions(self):
		"""
		The method to get the permissions

		Returns:
			dict: An instance of dict
		"""

		return self.__permissions

	def set_permissions(self, permissions):
		"""
		The method to set the value to permissions

		Parameters:
			permissions (dict) : An instance of dict
		"""

		if permissions is not None and not isinstance(permissions, dict):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: permissions EXPECTED TYPE: dict', None, None)
		
		self.__permissions = permissions
		self.__key_modified['permissions'] = 1

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
