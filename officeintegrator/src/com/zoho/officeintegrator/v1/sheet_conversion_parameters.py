try:
	from officeintegrator.src.com.zoho.officeintegrator.exception.sdk_exception import SDKException
	from officeintegrator.src.com.zoho.officeintegrator.util import StreamWrapper, Constants
except Exception:
	from ..exception import SDKException
	from ..util import StreamWrapper, Constants


class SheetConversionParameters(object):
	def __init__(self):
		"""Creates an instance of SheetConversionParameters"""

		self.__url = None
		self.__document = None
		self.__output_options = None
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

	def get_output_options(self):
		"""
		The method to get the output_options

		Returns:
			SheetConversionOutputOptions: An instance of SheetConversionOutputOptions
		"""

		return self.__output_options

	def set_output_options(self, output_options):
		"""
		The method to set the value to output_options

		Parameters:
			output_options (SheetConversionOutputOptions) : An instance of SheetConversionOutputOptions
		"""

		try:
			from officeintegrator.src.com.zoho.officeintegrator.v1.sheet_conversion_output_options import SheetConversionOutputOptions
		except Exception:
			from .sheet_conversion_output_options import SheetConversionOutputOptions

		if output_options is not None and not isinstance(output_options, SheetConversionOutputOptions):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: output_options EXPECTED TYPE: SheetConversionOutputOptions', None, None)
		
		self.__output_options = output_options
		self.__key_modified['output_options'] = 1

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
