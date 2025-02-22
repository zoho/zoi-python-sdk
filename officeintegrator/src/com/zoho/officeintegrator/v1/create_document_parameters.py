try:
	from officeintegrator.src.com.zoho.officeintegrator.exception.sdk_exception import SDKException
	from officeintegrator.src.com.zoho.officeintegrator.util import StreamWrapper, Constants
except Exception:
	from ..exception import SDKException
	from ..util import StreamWrapper, Constants


class CreateDocumentParameters(object):
	def __init__(self):
		"""Creates an instance of CreateDocumentParameters"""

		self.__url = None
		self.__document = None
		self.__callback_settings = None
		self.__document_defaults = None
		self.__editor_settings = None
		self.__permissions = None
		self.__document_info = None
		self.__user_info = None
		self.__ui_options = None
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

	def get_callback_settings(self):
		"""
		The method to get the callback_settings

		Returns:
			CallbackSettings: An instance of CallbackSettings
		"""

		return self.__callback_settings

	def set_callback_settings(self, callback_settings):
		"""
		The method to set the value to callback_settings

		Parameters:
			callback_settings (CallbackSettings) : An instance of CallbackSettings
		"""

		try:
			from officeintegrator.src.com.zoho.officeintegrator.v1.callback_settings import CallbackSettings
		except Exception:
			from .callback_settings import CallbackSettings

		if callback_settings is not None and not isinstance(callback_settings, CallbackSettings):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: callback_settings EXPECTED TYPE: CallbackSettings', None, None)
		
		self.__callback_settings = callback_settings
		self.__key_modified['callback_settings'] = 1

	def get_document_defaults(self):
		"""
		The method to get the document_defaults

		Returns:
			DocumentDefaults: An instance of DocumentDefaults
		"""

		return self.__document_defaults

	def set_document_defaults(self, document_defaults):
		"""
		The method to set the value to document_defaults

		Parameters:
			document_defaults (DocumentDefaults) : An instance of DocumentDefaults
		"""

		try:
			from officeintegrator.src.com.zoho.officeintegrator.v1.document_defaults import DocumentDefaults
		except Exception:
			from .document_defaults import DocumentDefaults

		if document_defaults is not None and not isinstance(document_defaults, DocumentDefaults):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: document_defaults EXPECTED TYPE: DocumentDefaults', None, None)
		
		self.__document_defaults = document_defaults
		self.__key_modified['document_defaults'] = 1

	def get_editor_settings(self):
		"""
		The method to get the editor_settings

		Returns:
			EditorSettings: An instance of EditorSettings
		"""

		return self.__editor_settings

	def set_editor_settings(self, editor_settings):
		"""
		The method to set the value to editor_settings

		Parameters:
			editor_settings (EditorSettings) : An instance of EditorSettings
		"""

		try:
			from officeintegrator.src.com.zoho.officeintegrator.v1.editor_settings import EditorSettings
		except Exception:
			from .editor_settings import EditorSettings

		if editor_settings is not None and not isinstance(editor_settings, EditorSettings):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: editor_settings EXPECTED TYPE: EditorSettings', None, None)
		
		self.__editor_settings = editor_settings
		self.__key_modified['editor_settings'] = 1

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

	def get_document_info(self):
		"""
		The method to get the document_info

		Returns:
			DocumentInfo: An instance of DocumentInfo
		"""

		return self.__document_info

	def set_document_info(self, document_info):
		"""
		The method to set the value to document_info

		Parameters:
			document_info (DocumentInfo) : An instance of DocumentInfo
		"""

		try:
			from officeintegrator.src.com.zoho.officeintegrator.v1.document_info import DocumentInfo
		except Exception:
			from .document_info import DocumentInfo

		if document_info is not None and not isinstance(document_info, DocumentInfo):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: document_info EXPECTED TYPE: DocumentInfo', None, None)
		
		self.__document_info = document_info
		self.__key_modified['document_info'] = 1

	def get_user_info(self):
		"""
		The method to get the user_info

		Returns:
			UserInfo: An instance of UserInfo
		"""

		return self.__user_info

	def set_user_info(self, user_info):
		"""
		The method to set the value to user_info

		Parameters:
			user_info (UserInfo) : An instance of UserInfo
		"""

		try:
			from officeintegrator.src.com.zoho.officeintegrator.v1.user_info import UserInfo
		except Exception:
			from .user_info import UserInfo

		if user_info is not None and not isinstance(user_info, UserInfo):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: user_info EXPECTED TYPE: UserInfo', None, None)
		
		self.__user_info = user_info
		self.__key_modified['user_info'] = 1

	def get_ui_options(self):
		"""
		The method to get the ui_options

		Returns:
			UiOptions: An instance of UiOptions
		"""

		return self.__ui_options

	def set_ui_options(self, ui_options):
		"""
		The method to set the value to ui_options

		Parameters:
			ui_options (UiOptions) : An instance of UiOptions
		"""

		try:
			from officeintegrator.src.com.zoho.officeintegrator.v1.ui_options import UiOptions
		except Exception:
			from .ui_options import UiOptions

		if ui_options is not None and not isinstance(ui_options, UiOptions):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: ui_options EXPECTED TYPE: UiOptions', None, None)
		
		self.__ui_options = ui_options
		self.__key_modified['ui_options'] = 1

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
