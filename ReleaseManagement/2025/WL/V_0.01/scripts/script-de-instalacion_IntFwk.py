#Author: Vicky Naveju Rodriguez

import wlstModule
import time
import getopt
import sys
import re

# Get location of the properties file.
properties = ''
try:
   opts, args = getopt.getopt(sys.argv[1:],"p:h::",["properies="])
except getopt.GetoptError:
   print 'set_datasource.py -p <path-to-properties-file>'
   sys.exit(2)
for opt, arg in opts:
   if opt == '-h':
      print 'set_datasource.py -p <path-to-properties-file>'
      sys.exit()
   elif opt in ("-p", "--properties"):
      properties = arg
print 'properties=', properties

# Load the properties from the properties file.

from java.io import FileInputStream 

propInputStream = FileInputStream(properties)
configProps = Properties()
configProps.load(propInputStream)

# Set all variables from values in properties file.
adminUsername=configProps.get("admin.username")
adminPassword=configProps.get("admin.password")
adminURL=configProps.get("admin.url")
dsPassword=configProps.get("ds.passwordintfwk_user")
dsURL=configProps.get("ds.url")

# Display the variable values.
print 'adminUsername=', adminUsername
print 'adminURL=', adminURL

# Connect to the AdminServer.

connect(adminUsername, adminPassword, adminURL)

print ''
print '======================================================'
print 'The script has been send connect to server'
print '======================================================'
print ''

edit()
startEdit()
cd('/')
cmo.createJDBCSystemResource('jdbc.IntFwk')

cd('/JDBCSystemResources/jdbc.IntFwk/JDBCResource/jdbc.IntFwk')
cmo.setName('jdbc.IntFwk')

cd('/JDBCSystemResources/jdbc.IntFwk/JDBCResource/jdbc.IntFwk/JDBCDataSourceParams/jdbc.IntFwk')
set('JNDINames',jarray.array([String('jdbc.IntFwk')], String))

cd('/JDBCSystemResources/jdbc.IntFwk/JDBCResource/jdbc.IntFwk')
cmo.setDatasourceType('GENERIC')

print ''
print '======================================================'
print 'The script has been send Password to the jdbc'
print '======================================================'
print ''

cd('/JDBCSystemResources/jdbc.IntFwk/JDBCResource/jdbc.IntFwk/JDBCDriverParams/jdbc.IntFwk')
cmo.setUrl(dsURL)
cmo.setDriverName('oracle.jdbc.xa.client.OracleXADataSource')
set('Password', dsPassword)

print ''
print '======================================================'
print 'The script has been send setTestTableName to the Admin Server'
print '======================================================'
print ''


cd('/JDBCSystemResources/jdbc.IntFwk/JDBCResource/jdbc.IntFwk/JDBCConnectionPoolParams/jdbc.IntFwk')
cmo.setTestTableName('SQL ISVALID\r\n\r\n')

print ''
print '======================================================'
print 'The script has been sent value intfwk_user '
print '======================================================'
print ''

cd('/JDBCSystemResources/jdbc.IntFwk/JDBCResource/jdbc.IntFwk/JDBCDriverParams/jdbc.IntFwk/Properties/jdbc.IntFwk')
cmo.createProperty('user')

cd('/JDBCSystemResources/jdbc.IntFwk/JDBCResource/jdbc.IntFwk/JDBCDriverParams/jdbc.IntFwk/Properties/jdbc.IntFwk/Properties/user')
cmo.setValue('intfwk')


print ''
print '======================================================'
print 'The script has been send setGlobalTransactionsProtocol '
print '======================================================'
print ''


cd('/JDBCSystemResources/jdbc.IntFwk/JDBCResource/jdbc.IntFwk/JDBCDataSourceParams/jdbc.IntFwk')
cmo.setGlobalTransactionsProtocol('TwoPhaseCommit')

print ''
print '======================================================'
print 'The script has been sent value Targets '
print '======================================================'
print ''


cd('/JDBCSystemResources/jdbc.IntFwk')
set('Targets',jarray.array([ObjectName('com.bea:Name=jee_cluster,Type=Cluster')], ObjectName))

save()
activate()
disconnect()

