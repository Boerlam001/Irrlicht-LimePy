﻿import System
#------------------------------------------------------------------------------
# <auto-generated>
#     This code was generated by a tool.
#     Runtime Version:4.0.30319.225
#
#     Changes to this file may cause incorrect behavior and will be lost if
#     the code is regenerated.
# </auto-generated>
#------------------------------------------------------------------------------
class Settings(System.Configuration.ApplicationSettingsBase):
	defaultInstance = ((System.Configuration.ApplicationSettingsBase.Synchronized(Settings())))
	def __init__(self):
		pass
	def get_Default(self):
		return Settings.defaultInstance

	Default = property(fget=get_Default)